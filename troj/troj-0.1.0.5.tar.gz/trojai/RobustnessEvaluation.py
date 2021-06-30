from . import TrojEpsilon
import numpy as np
# import pandas as pd
from . import array_utils
from . import attack_utils
from . import ODAttack
import torch


class BasicRobustnessEvaluator:
    def __init__(
        self,
        classifier,
        learning_rate=0.01,
        eps_steps=0.05,
        max_halving=10,
        max_doubling=10,
        num_iters=15,
        batch_size=128,
        norm=np.inf,
        method="minimum",
        k=5,
        use_all=False,
        use_model_preds=False,
    ):
        self.classifier = classifier
        self.attacker = TrojEpsilon.TrojEpsAttack(
            self.classifier,
            learning_rate=learning_rate,
            eps_steps=eps_steps,
            max_halving=max_halving,
            max_doubling=max_doubling,
            num_iters=num_iters,
            batch_size=batch_size,
            norm=norm,
            method=method,
            k=k,
            use_all=use_all,
            use_model_preds=use_model_preds,
        )

    def attack(self, data, target, index, device=None):
        """
        This will work for pytorch, tensorflow has no device
        """
        # index = index.numpy()
        # send data and target to cpu, convert to numpy
        data = np.ascontiguousarray(data.astype(np.float32))
        test_loss, preds = self.classifier.ComputeLoss(data, target)
        preds = np.argmax(preds, axis=1)
        adv_x, adv_preds, adv_loss = self.attacker.generate(data, target)
        # adv_loss, adv_preds = self.classifier.ComputeLoss(adv_x, target)
        perturbation = array_utils.compute_Lp_distance(data, adv_x)
        adv_pred = np.argmax(adv_preds, axis=1)
        # generate the adversarial image using the data numpy array and label numpy array
        out_dict = {
            "Linf_perts": perturbation,
            "Loss": test_loss,
            "Adversarial_Loss": adv_loss,
            "prediction": preds,
            "Adversarial_prediction": adv_pred,
        }
        return (out_dict, index)


class BlackBoxODEvaluator:
    # different run form to classification
    def __init__(
        self,
        model,
        obj_class,
        loader,
        batch_iterator,
        df=None,
        device="cuda",
        iou_thresh=0.5,
        nms_thresh=0.05,
        step_size=0.1,
        verbose=True,
        return_prc=True,
        **attkwargs
    ):
        self.model = model
        self.obj_class = obj_class
        self.loader = loader
        self.batch_iterator = batch_iterator
        self.df = df
        if self.df == None:
            self.df = loader.dataframe
        self.device = device
        self.iou_thresh = iou_thresh
        self.nms_thresh = nms_thresh
        self.step_size = step_size
        self.attacker = ODAttack.EvoDAttack(self.model, self.obj_class, **attkwargs)
        self.verbose = verbose
        self.return_prc = return_prc

    def run(self, num_samples):
        # TODO: Should the dataset task checker be in here?
        tracker = 0
        attacked_ids = []
        batch_enum = enumerate(self.batch_iterator)

        while tracker < num_samples:
            batch_id, (ims, labs, ids) = next(batch_enum)

            if tracker > 0 and batch_id == 0:
                break

            for idx in range(len(labs)):
                sample_id = ids[idx]
                data_dict = {}
                perturb, gt, preds = self.attacker.attack(ims[idx], labs[idx])
                if gt != None:
                    pert_im = ims[idx] + perturb.to(self.device)
                    pert_preds = self.model([pert_im])[0]
                    nms_pert_preds = ODAttack.nms_pred_reduce(pert_preds, self.nms_thresh)
                    nms_preds = ODAttack.nms_pred_reduce(preds, self.nms_thresh)
                    flip = ODAttack.check_flip(nms_pert_preds, gt, self.obj_class, self.iou_thresh, self.nms_thresh)

                    if self.return_prc:
                        troj_map, perc, rec, thresh = ODAttack.mAP(nms_preds, labs[idx], self.step_size, self.iou_thresh)
                        adv_troj_map, adv_perc, adv_rec, adv_thresh = ODAttack.mAP(nms_pert_preds, labs[idx], self.step_size, self.iou_thresh)
                    else:
                        troj_map = ODAttack.mAP(nms_preds, labs[idx], self.step_size, self.iou_thresh)
                        adv_troj_map = ODAttack.mAP(nms_pert_preds, labs[idx], self.step_size, self.iou_thresh)
                        
                    pert_vec = perturb.view(-1)
                    linf_pert = torch.norm(pert_vec, p=np.inf)
                    tracker += 1

                    if self.return_prc:
                        data_dict = {
                            "flip": flip,
                            "TmAP": troj_map,
                            "Adv_TmAP": adv_troj_map,
                            "Linf": linf_pert.item(),
                            "precision": perc,
                            "recall": rec,
                            "thresh": thresh,
                            "adv_precision": adv_perc,
                            "adv_recall": adv_rec,
                            "adv_thresh": adv_thresh,
                        }
                    else:
                        data_dict = {
                            "flip": flip,
                            "TmAP": troj_map,
                            "Adv_TmAP": adv_troj_map,
                            "Linf": linf_pert.item(),
                        }

                    self.df = attack_utils.log_to_dataframe(self.df, sample_id, data_dict)
                    attacked_ids.append(sample_id)

        # Insert the model used into the df <- not going to work..
        # Inserting into DB would be nice, how to get dataset_uuid/max_metric_job_uuid ?
        # if "model_used" not in self.df:
        #     self.df["model_used"] = ""
        #     self.df["model_used"].astype("object")
        # dataframe.loc[index, key] = log_dict[key]
        # self.df["model_used"] = self.model.__class__.__name__
        return self.df, attacked_ids
