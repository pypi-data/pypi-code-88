from art.attacks.evasion import *
from .array_utils import *


class TrojEpsAttack:
    def __init__(
        self,
        model,
        learning_rate=0.01,
        eps_steps=0.05,
        max_halving=10,
        max_doubling=10,
        num_iters=15,
        batch_size=128,
        norm=np.inf,
        method = 'minimum',
        k=5,
        use_all=False,
        use_model_preds=False
    ):
        '''

        :param model: Troj/ART classifier instance.
        :param learning_rate: The learning rate for CW L^inf. Only relevant if use_all = True
        :param eps_steps: Size of steps in FGSM and PGD.
        :param max_halving: The max_halving for CW L^inf. Only relevant if use_all = True
        :param max_doubling: The max_doubling for CW L^inf. Only relevant if use_all = True
        :param num_iters: Number of iterations for each attack.
        :param batch_size: Batch size for each attack.
        :param norm: The attack norm for PGD and FGSM.
        :param method: Whether to use the faster loss based method, or the slower minimum method. Argument is given as
        one of 'fast' or 'minimum'
        :param use_model_preds: if minimum is true, whether or not to use the true labels or the model preds for
        evauluating the minimum perturbation
        :param k: When using fast top-k method, this is the size of k.
        :param use_all: Whether to use all 3 basic attacks. Slows down computation, but results in a somewhat stronger
        evaluation.
        '''
        self.model = model
        self.budgets = np.arange(0.1, 1, 0.05)
        self.learning_rate = learning_rate
        self.eps_steps = eps_steps
        self.max_halving = max_halving
        self.max_doubling = max_doubling
        self.num_iters = num_iters
        self.batch_size = batch_size
        self.norm = norm
        self.method = method
        self.k = k
        self.use_all = use_all
        self.use_model_preds = use_model_preds

        #store instantiate attack instances in dictionary
        attack_dict = {}
        for i in range(self.budgets.shape[0]):
            cw_name = "cw_{}".format(i)
            fgm_name = "fgsm_{}".format(i)
            pgd_name = "pgd_{}".format(i)

            attack_dict[fgm_name] = FastGradientMethod(
                self.model,
                norm=self.norm,
                eps=self.budgets[i],
                eps_step=self.eps_steps,
                batch_size=self.batch_size,
            )
            if self.use_all:
                attack_dict[cw_name] = CarliniLInfMethod(self.model,
                                            learning_rate=self.learning_rate, max_iter=self.num_iters,
                                            max_halving=self.max_halving, max_doubling=self.max_doubling,
                                            eps=self.budgets[i], batch_size=self.batch_size, verbose=False)

                attack_dict[pgd_name] = ProjectedGradientDescent(self.model, norm=self.norm, eps=self.budgets[i],
                                                       eps_step=self.eps_steps,
                                                       batch_size=self.batch_size, max_iter=self.num_iters, verbose=False)
        self.attack_dict = attack_dict

    def generate(self, x, y):
        """
        :param x: inputs
        :param y: labels, either true labels or original unperturbed model labels. y might need to be expanded along
        the first dimension because of art bug.
        :return: adversarial examples, adversarial losses, adversarial predictions
        """
        generated_examples = []
        model_adv_losses = []
        model_adv_preds = []
        #For each attack method in the attack dictionary, generate adversarial examples, then compute the loss
        #and the class predictions.
        for attacker in list(self.attack_dict.values()):
            adv_x = attacker.generate(x, y)
            if len(y.shape) == 1:
                adv_losses, adv_preds = self.model.ComputeLoss(adv_x, y)
                if self.use_model_preds == True:
                    true_losses, true_preds = self.model.ComputeLoss(x, y)
            else:
                adv_losses, adv_preds = self.model.ComputeLoss(adv_x, np.squeeze(y, axis=1))
                if self.use_model_preds == True:
                    true_losses, true_preds = self.model.ComputeLoss(x, np.squeeze(y, axis=1))
            model_adv_losses.append(adv_losses)
            generated_examples.append(adv_x)
            model_adv_preds.append(adv_preds)
        #reshape arrays so that they each have shape [batch_size, num_attacks, *]
        generated_examples = np.stack(generated_examples)
        generated_examples = np.swapaxes(generated_examples, 0, 1)

        model_adv_losses = np.stack(model_adv_losses)
        model_adv_losses = np.swapaxes(model_adv_losses, 0, 1)

        model_adv_preds = np.stack(model_adv_preds)
        model_adv_preds = np.swapaxes(model_adv_preds, 0, 1)

        #Whether or not to compute the perturbations quickly, or in such a way as to minimize
        # the perturbation that flips the label.
        if self.method=='fast':
            high_loss_examples, losses, sorted_preds = AdvLossSort(generated_examples, model_adv_losses, model_adv_preds, k=self.k)
            output, preds, losses = get_min_pert(x, high_loss_examples, losses, sorted_preds, norm=self.norm)
        elif self.method=='minimum':
            if self.use_model_preds==True:
                labels = true_preds
            else:
                labels = y
            output, preds, losses = true_min_pert(labels, model_adv_preds, x, generated_examples, model_adv_losses)

        return output, preds, losses
