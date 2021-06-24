import logging, os, json
import random
from glob import glob
from collections import OrderedDict, defaultdict
import numpy as np
import inspect
from functools import partial
from tqdm import tqdm
from copy import deepcopy
import torch
import torch.nn.functional as F

try:
    import torch_xla.core.xla_model as xm, torch_xla.distributed.parallel_loader as pl, torch_xla.distributed.xla_multiprocessing as xmp
except Exception as e:
    pass

try:
    import torchcontrib
except:
    pass

from mautil.basic_models import CFG as BasicCFG, Model as BasicModel, LossHist
from mautil.pt import util as pt_util
from mautil import util

WEIGHT_SUFFIX = '.bin'


logger = logging.getLogger(__name__)


class CFG(BasicCFG):
    def __init__(self):
        super(CFG, self).__init__()
        self.loss = 'mse'
        self.global_step = None
        self.gradient_clip = None
        self.keep_checkpoint_every_n_hours = 1000000000
        self.save_keep = 1000000000
        self.save_summary_step = 1000000000
        self.use_tpu = False
        self.use_tffit = True
        self.opt = 'torch.optim.AdamW'
        self.tpu_name = None
        self.warm_start_path = None  # used by tpu
        self.tpu_zone = None
        self.gcp_project = None
        self.num_core_per_host = 1
        self.num_hosts = 1
        self.tpu_loop_iterations = 2
        self.run_eagerly = False
        self.accumulated_batch_size = 1
        self.compile_model = False
        # xla
        self.xla_procs = 8
        self.xla_spawn_method = 'fork'

        # dataset
        self.n_dl_worker = 0

        # swa
        self.swa_batch_size = None


#    def dump(self, fpath):
#        os.makedirs(os.path.dirname(fpath), exist_ok=True)
#        with open(fpath, 'w') as f:
#            json.dump(self.__dict__, f)


class XLA(object):
    def __init__(self, f):
        self.f = f

    def __get__(self, model, owner):
        def wrapper(*args, **kwargs):
            kwargs = util.fill_kwargs(self.f, args, kwargs)
            kwargs['self'] = model
            if model.cfg.use_tpu:
                xla_procs = kwargs.get('xla_procs', model.cfg.xla_procs)
                if xla_procs>1:
                    if model.cfg.xla_share_model:
                        kwargs['pt_model'] = xmp.MpModelWrapper(model.create_core_model())
                    return xmp.spawn(self.run, args=(model, kwargs), nprocs=xla_procs, start_method=model.cfg.xla_spawn_method)
                else:
                    kwargs = self.process_args(model, kwargs)
                    return self.f(**kwargs)
            else:
                return self.f(**kwargs)
        return wrapper

    def process_args(self, model, kwargs):
        if self.f.__name__ == 'predict':
            ds, data_type = kwargs.get('ds'), kwargs.get('data_type')
            device = xm.xla_device()
            ds = model._gen_distribute_dl(ds, data_type)
            #ds = pl.ParallelLoader(ds, [device]).per_device_loader(device)
            kwargs['ds'] = ds
        else:
            # fit func
            train_ds, val_ds = kwargs.get('train_ds'), kwargs.get('val_ds')
            if train_ds is not None:
                train_ds = model._gen_distribute_dl(train_ds, 'train')
                kwargs['train_ds'] = train_ds
            if val_ds is not None:
                val_ds = model._gen_distribute_dl(val_ds, 'val')
                kwargs['val_ds'] = val_ds
        return kwargs

    def run(self, index, model, kwargs):
        kwargs = self.process_args(model, kwargs)
        return self.f(**kwargs, index=index)


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True

"""
swa related. should remove in future
"""
# BatchNorm utils
def _check_bn_apply(module, flag):
    if issubclass(module.__class__, torch.nn.modules.batchnorm._BatchNorm):
        flag[0] = True


def _check_bn(model):
    flag = [False]
    model.apply(lambda module: _check_bn_apply(module, flag))
    return flag[0]


def _reset_bn(module):
    if issubclass(module.__class__, torch.nn.modules.batchnorm._BatchNorm):
        module.running_mean = torch.zeros_like(module.running_mean)
        module.running_var = torch.ones_like(module.running_var)


def _get_momenta(module, momenta):
    if issubclass(module.__class__, torch.nn.modules.batchnorm._BatchNorm):
        momenta[module] = module.momentum


def _set_momenta(module, momenta):
    if issubclass(module.__class__, torch.nn.modules.batchnorm._BatchNorm):
        module.momentum = momenta[module]

class PTModel(BasicModel):
    cfg = CFG()

    def __init__(self, name='PTModel', cfg={}):
        super(PTModel, self).__init__(name, cfg)
        self._restored = False
        self._restored_epoch = None
        self._accumulated_grads = None
        self._batch_id = None
        self._opt = None
        self._device = None
        self._is_cuda_available = None
        self._lr_scheduler = None
        self._grad_scaler = None
        self._ema_model = None
        set_seed(self.cfg.seed)

        if self.cfg.restore:
            # restore cfg first
            super(PTModel, self).restore(model_dir=self.cfg.model_dir)

    def create_core_model(self, **kwargs):
        pass

    def get_device(self):
        if self.cfg.use_tpu:
            device = xm.xla_device()
        elif self._is_cuda_available:
            if self.cfg.device is None:
                device = torch.device('cuda')
            else:
                device = torch.device('cuda:'+','.join(self.cfg.device))
        else:
            device = torch.device('cpu')
        return device

    def _create_grad_scaler(self):
        return torch.cuda.amp.GradScaler()

    def to_device(self):
        device = self._device
        if torch.cuda.device_count() > 1 and self.cfg.use_multiple_gpu:
            if self.cfg.device is not None and len(self.cfg.device)>1:
                self._model = nn.DataParallel(self._model, device_ids=self.cfg.device)
                logger.info("use GPUS:", self.cfg.device)
            else:
                self._model = torch.nn.DataParallel(self._model)
                logger.info("use %s GPUS!", torch.cuda.device_count())
        self._model = self._model.to(device)
        if self._ema_model is not None:
            self._ema_model.ema = self._ema_model.ema.to(device)
        logger.info('created model on device:%s', device)

    def create_model(self, opt=None, pt_model=None, **kwargs):
        self._is_cuda_available = torch.cuda.is_available()
        self._device = self.get_device()
        if self.cfg.use_fp16:
            self._grad_scaler = self._create_grad_scaler()
        if pt_model is None:
            self._model = self.create_core_model(**kwargs)
            if self.cfg.ema is not None and self.cfg.ema > 0:
                self._ema_model = ModelEma(self._model, decay=self.cfg.ema)
                logger.info('ema model created')
        else:
            self._model = pt_model

        self.to_device()
        # it is said for some optimizer like Adagrad need create opt after model.cuda()
        if opt is not None:
            self._opt = opt
        else:
            if self.cfg.use_deepspeed:
                self._ds_model, self._ds_opt, self._lr_scheduler = util.init_deepspeed(self.cfg.deepspeed, self._model)
                self._opt = self._ds_opt.optimizer
                self._model = self._ds_model.module
            else:
                self._opt, self._lr_scheduler = self._create_optimizer()

        if self.cfg.restore:
            self.restore(restore_epoch=self.cfg.restore_epoch, model_dir=self.cfg.model_dir)

        if self.cfg.use_tpu and xm.xrt_world_size()>1:
            xm.rendezvous('create model done')

    def _create_lr_scheduler(self, opt):
        if self.cfg.lr_scheduler is None:
            lr_scheduler = None
        elif self.cfg.lr_scheduler =='ld':
            lr_scheduler = pt_util.get_linear_decay_schedule_with_warmup(opt, self.cfg.n_lr_warmup_step, self.cfg.n_lr_decay_step, self.cfg.lr_decay_rate)
        else:
            lr_scheduler = util.dynamic_import(self.cfg.lr_scheduler)(opt, **self.cfg.lr_scheduler_ca_paras)
        return lr_scheduler

    def _create_optimizer(self, parameters=None, lr=None):
        if parameters is None:
            parameters = self._model.parameters()
        if lr is None:
            lr = self.cfg.lr
        # create after model.cuda()
#        if self.cfg.opt == 'adamW':
#            opt = torch.optim.AdamW(parameters, lr=self.cfg.lr, weight_decay=self.cfg.weight_decay)
#        elif self.cfg.opt == 'adam':
#            opt = torch.optim.Adam(parameters, lr=self.cfg.lr)
#        else:
#            opt = util.dynamic_import(self.cfg.opt)(parameters, lr=self.cfg.lr, **self.cfg.opt_paras)
        opt = util.dynamic_import(self.cfg.opt)(filter(lambda p:p.requires_grad, parameters), lr=lr, **self.cfg.opt_paras)
        if self.cfg.swa_start_epoch >0:
            opt = torchcontrib.optim.SWA(opt)

        lr_scheduler = self._create_lr_scheduler(opt)
        return opt, lr_scheduler

    def save(self, global_step=None, save_path=None, epoch=None, save_opt=False, **kwargs):
        if self.cfg.n_keep_ckpt>1:
            self.cfg.saved_epoch = epoch
        else:
            self.cfg.saved_epoch = None
        if save_path is None:
            save_name = 'model-{}{}'.format(epoch, WEIGHT_SUFFIX) if epoch and self.cfg.n_keep_ckpt>1 else 'model'+ WEIGHT_SUFFIX
            if self.cfg.model_dir is None:
                save_path = self.gen_fname(save_name)
            else:
                save_path = os.path.join(self.cfg.model_dir, save_name)
        to_save_model = self._model
        if not self.cfg.save_ema and self._ema_model is not None:
            to_save_model = self._ema_model.ema # switch ema
        if self.cfg.save_half:
            to_save_model = deepcopy(to_save_model).half()
        state_dict = {'epoch': epoch,
                      'global_step': global_step,
                      'model_state_dict': to_save_model.state_dict(),
                      'rng_state':torch.get_rng_state(),
                      }
        if save_opt and not self.cfg.use_deepspeed:
            assert self.cfg.save_ema or self._ema_model is None, "should save ema for resume training"
            state_dict['optimizer_state_dict'] = self._opt.state_dict()
            if self._lr_scheduler is not None:
                state_dict['lr_scheduler_state_dict'] = self._lr_scheduler.state_dict()
        state_dict.update(kwargs)
        if self.cfg.save_ema and self._ema_model is not None:
            state_dict['ema_state_dict'] = self._ema_model.ema.state_dict()

        self.update_saved_ckpt([save_path], epoch)
        if self.cfg.use_tpu:
            if xm.is_master_ordinal():
                super(PTModel, self).save()
        else:
            super(PTModel, self).save()

        if self.cfg.use_tpu:
            xm.save(state_dict, save_path)
        else:
            torch.save(state_dict, save_path)
        if self.cfg.use_deepspeed:
            self._ds_model.save_checkpoint(self.gen_fname())
            logger.info('deepspeed model saved to %s', self.gen_fname())
        self.info("Model saved to file:{}".format(save_path))

    def update_saved_ckpt(self, save_paths, epoch):
        save_paths = [os.path.basename(save_path) for save_path in save_paths] # use rel path, not exposure private info
        self.cfg.saved_ckpts.append([epoch, save_paths])
        if len(self.cfg.saved_ckpts)>self.cfg.n_keep_ckpt:
            for save_path in self.cfg.saved_ckpts[0][1]:
                if os.path.exists(save_path):
                    os.remove(save_path)
            self.cfg.saved_ckpts = self.cfg.saved_ckpts[1:]
            #self.cfg.saved_ckpts = self.cfg.saved_ckpts[-self.cfg.n_keep_ckpt:]

    def get_checkpoint_path_bak(self, model_dir=None, restore_epoch=None):
        if model_dir is None:
            model_dir = self.gen_fname()
        if restore_epoch is None and self.cfg.saved_epoch is not None:
            restore_epoch = self.cfg.saved_epoch
        save_name = 'model-{}{}'.format(restore_epoch, WEIGHT_SUFFIX) if restore_epoch else 'model' + WEIGHT_SUFFIX
        model_path = os.path.join(model_dir, save_name)
        return model_path

    def get_checkpoint_path(self, model_dir=None, restore_epoch=None):
        if restore_epoch is None:
            restore_epoch, save_paths = self.cfg.saved_ckpts[-1]
        else:
            save_paths = None
            for i, (save_epoch, save_paths) in enumerate(self.cfg.saved_ckpts[::-1]):
                if save_epoch == restore_epoch:
                    break
                else:
                    save_paths = None

        if model_dir is None:
            model_dir = self.gen_fname()
        save_paths = [os.path.join(model_dir, save_path) for save_path in save_paths]
        return save_paths, restore_epoch

    def load_state_dict(self, model, state_dict):
        missing_keys, unexpected_keys = model.load_state_dict(state_dict, strict=self.cfg.restore_strict)
        if len(missing_keys) > 0:
            self.info('missing_keys %s', missing_keys)
        if len(unexpected_keys) > 0:
            self.info('unexpected_keys %s', unexpected_keys)


    def restore(self, restore_epoch=None, epoch=None, model_dir=None):
        if self._model is None:
            self.create_model()

        if not self._restored:
            model_paths, restore_epoch = self.get_checkpoint_path(model_dir, restore_epoch)
            model_path = model_paths[0]
            ckpt = torch.load(model_path, map_location=torch.device('cpu'))
            self.load_state_dict(self._model, ckpt['model_state_dict'])
            if self._ema_model is not None and 'ema_state_dict' not in ckpt:
                self.load_state_dict(self._ema_model.ema, ckpt['model_state_dict'])
                self.info("copied ema model weights from model")
            if 'optimizer_state_dict' in ckpt:
                self._opt.load_state_dict(ckpt['optimizer_state_dict'])
                self.info("optimizer state restored")
            if 'lr_scheduler_state_dict' in ckpt:
                self._lr_scheduler.load_state_dict(ckpt['lr_scheduler_state_dict'])
                self.info("lr scheduler state restored")
            if 'ema_state_dict' in ckpt:
                self.info('restor ema model:%s', model_path)
                self.load_state_dict(self._ema_model.ema, ckpt['ema_state_dict'])
                self.info('ema model restored from %s', model_path)
            if 'rng_state' in ckpt:
                torch.set_rng_state(ckpt['rng_state'])
                self.info("torch random state restored")

            if 'epoch' in ckpt:
                self._restored_epoch = ckpt['epoch']
            else:
                self._restored_epoch = restore_epoch

            if self.cfg.use_deepspeed:
                self._ds_model.load_checkpoint(self.gen_fname(), load_optimizer_states=True, load_lr_scheduler_states=True)

            self._restored = True
            self.info('model restored from %s, epoch:%s', model_path, self._restored_epoch)

    def calc_loss(self, inputs, outputs, model=None):
        """

        :param inputs:
        :param outputs:
        :return:  dictionary of losses
        """
        if model is None:
            model = self._model
        if isinstance(model, torch.nn.DataParallel):
            model = model.module

        losses = model.calc_loss(inputs, outputs)
        return losses

    def _step_opt(self, opt, lr_scheduler=None):
        if self.cfg.use_deepspeed:
            self.deepspeed.step()
        else:
            if self.cfg.gradient_clip is not None:
                for gp in opt.param_groups:
                    torch.nn.utils.clip_grad_norm_(gp['params'], self.cfg.gradient_clip)
            if self.cfg.use_tpu:
                xm.optimizer_step(opt)
            elif self.cfg.use_fp16:
                self._grad_scaler.step(opt)
                self._grad_scaler.update()
            else:
                opt.step()
        if lr_scheduler is not None:
            lr_scheduler.step()
        opt.zero_grad()
        if self._ema_model is not None:
            self._ema_model.update(self._model)

    def fit_batch(self, batch, step=None, phase='train', model=None, opt=None, lr_scheduler=None):
        if model is None:
            model = self._model
        if opt is None:
            opt = self._opt
        if lr_scheduler is None:
            lr_scheduler = self._lr_scheduler
        if not self.cfg.use_tpu and self._is_cuda_available:
            pt_util.batch2device(batch, self._device)
        with torch.set_grad_enabled(phase == 'train'):
            if self.cfg.use_fp16:
                with torch.cuda.amp.autocast():
                    outputs = model(**batch, phase=phase)
            else:
                outputs = model(**batch, phase=phase)
            if phase != 'test':
                if self.cfg.use_fp16:
                    with torch.cuda.amp.autocast():
                        losses = self.calc_loss(batch, outputs, model=model)
                else:
                    losses = self.calc_loss(batch, outputs, model=model)
                loss = losses['loss']/self.cfg.accumulated_batch_size
            else:
                losses = None
            if phase == 'train':
                if self.cfg.use_fp16:
                    loss = self._grad_scaler.scale(loss)
                    loss.backward()
                elif self.cfg.use_deepspeed:
                    self._ds_model.backward(loss)
                else:
                    loss.backward()
                if step % self.cfg.accumulated_batch_size == 0:
                    self._step_opt(opt=opt, lr_scheduler=lr_scheduler)
        #if self.cfg.use_tpu and phase!='test':
        #    losses = xm.mesh_reduce('batch_loss_reduce', losses, pt_util.mesh_reduce_losses)
        return outputs, losses


    def tensor2numpy(self, tensor):
        if isinstance(tensor, list):
            return [self.tensor2numpy(t) for t in tensor]
        elif isinstance(tensor, np.ndarray):
            return tensor
        elif torch.is_tensor(tensor):
            return tensor.cpu().detach().numpy()
        else:
            return tensor

    def outputs2preds(self, outputs):
        preds = dict()
        for output in outputs:
            for k, v in output.items():
                if 'loss' not in k:
                    v = self.tensor2numpy(v)
                    if k not in preds:
                        preds[k] = []
                    if self.cfg.to_list:
                        preds[k].extend(list(v))
                    else:
                        preds[k].append(v)
        if self.cfg.do_concat:
            for k in preds:
                preds[k] = np.concatenate(preds[k],0)
        return preds

    @XLA
    def predict(self, ds, data_type='val', pt_model=None, **kwargs):
        if self._model is None:
            self.create_model(pt_model=pt_model)
        if self._ema_model is not None:
            model = self._ema_model.ema
            logger.info('use ema model to predict')
        else:
            model = self._model
        model.eval()
        if self.cfg.use_tpu:
            device = xm.xla_device()
            ds = pl.ParallelLoader(ds, [device]).per_device_loader(device)
        outputs = []
        if not isinstance(ds, tqdm):
            ds = tqdm(enumerate(ds), total=len(ds), desc="predict")
        for i, batch in ds:
            output, _ = self.run_batch(batch, phase='test', model=model, **kwargs)
            outputs.append(output)
        preds = self.outputs2preds(outputs)
        self.info('predict done')
        return preds

    def fit_epoch(self, ds, epoch, step, device=None, **kwargs):
        """

        :param ds:
        :param epoch:
        :param step: global step accross epochs
        :param opt:
        :param history:
        :param barlog:
        :param kwargs:
        :return:
        """
        loss_hist = LossHist()
        self._model.train()
        desc = 'Train Epoch:{}, lr:{:.8f}, loss:{}'
        miniters, verbose, is_master = self.cfg.verbose, self.cfg.verbose, True
        if hasattr(ds, 'sampler') and hasattr(ds.sampler, 'set_epoch'):
            ds.sampler.set_epoch(epoch)
        if self.cfg.use_tpu:
            device = xm.xla_device()
            ds = pl.ParallelLoader(ds, [device]).per_device_loader(device)

            if not xm.is_master_ordinal():
                is_master = False
                miniters = int(1e10)
                verbose = int(1e10)
                ds_itr = enumerate(ds)
            else:
                ds_itr = tqdm(enumerate(ds), total=len(ds), disable=verbose==0, miniters=miniters, desc=desc.format(epoch, self._opt.state_dict()['param_groups'][0]['lr'], ''))
        else:
            device = next(self._model.parameters()).device
            ds_itr = tqdm(enumerate(ds), total=len(ds), disable=verbose==0, miniters=miniters, desc=desc.format(epoch, self._opt.state_dict()['param_groups'][0]['lr'], ''))
        for i, batch in ds_itr:
            # do not know why miniters was reset to 1
            if isinstance(ds_itr, tqdm):
                ds_itr.miniters = miniters
            step += 1
            outputs, losses = self.fit_batch(batch, step)
            for k, v in losses.items():
                losses[k] = v.item()
            loss_hist.append(losses)
            #ds_itr.set_description()
            if step%verbose == 0 and is_master:
                ds_itr.set_description(desc.format(epoch, self._opt.state_dict()['param_groups'][0]['lr'], loss_hist.avg_output()))

            if step % (self.cfg.n_save_step) == 0:
                logger.info('%%%% save model to %s for step:%s', self.cfg.output_dir, step)
                self.save(global_step=step, save_opt=self.cfg.save_opt)

            if (i + 1) >= self.cfg.n_epoch_step:
                logger.info('max %s step per epoch reached', self.cfg.n_epoch_step)
                break
            if step % self.cfg.n_train_step == 0:
                break
        #logger.info('epoch:{}, '.format(epoch) + loss_hist.avg_output())
        losses = loss_hist.get_avg()
        if self.cfg.use_tpu:
            losses = xm.mesh_reduce('epoch loss reduce', losses, pt_util.mesh_reduce_losses)
        return step, losses

    def run_batch(self, batch, phase='val', model=None, **kwargs):
        outputs, losses = self.fit_batch(batch, phase=phase, model=model)
        new_outputs = dict()
        for k in self.cfg.batch_keys:
            if k in outputs:
                new_outputs[k] = outputs[k]
            elif k in batch:
                new_outputs[k] = batch[k]
        outputs = new_outputs
        if self.cfg.use_tpu and kwargs.get('xla_procs', self.cfg.xla_procs)>1:
            outputs = xm.mesh_reduce('run batch outputs reduce', outputs, pt_util.mesh_reduce_outputs)
        return outputs, losses

    def val_epoch(self, ds, epoch, model=None):
        loss_hist = LossHist()
        if model is None:
            model = self._model
            if self._ema_model is not None:
                model = self._ema_model.ema
                logger.info('use ema model for val')
        model.eval()
        outputs = []
        miniters, verbose, is_master = self.cfg.verbose, self.cfg.verbose, True
        desc = 'Val Epoch:{}, loss:{}'
        if self.cfg.use_tpu:
            device = xm.xla_device()
            ds = pl.ParallelLoader(ds, [device]).per_device_loader(device)
            if not xm.is_master_ordinal():
                miniters, verbose, is_master = int(1e10), int(1e10), False
                ds_itr = enumerate(ds)
            else:
                ds_itr = tqdm(enumerate(ds), disable=verbose==0, total=len(ds), miniters=miniters, desc=desc.format(epoch, ''))
        else:
            device = next(self._model.parameters()).device
            ds_itr = tqdm(enumerate(ds), total=len(ds), disable=verbose==0, miniters=miniters, desc=desc.format(epoch, ''))
        for i, batch in ds_itr:
            if isinstance(ds_itr, tqdm):
                ds_itr.miniters = miniters
            output, losses = self.run_batch(batch, phase='val', model=model)
            outputs.append(output)
            val_losses = OrderedDict([('val_' + key, v.item()) for key, v in losses.items()])
            loss_hist.append(val_losses)
            if (i+1)%verbose == 0 and is_master:
                ds_itr.set_description(desc.format(epoch, loss_hist.avg_output()))

        if self.cfg.predicting or self.cfg.scoring:
            preds = self.outputs2preds(outputs)
        else:
            preds = None

        losses = loss_hist.get_avg()
        if self.cfg.use_tpu:
            losses = xm.mesh_reduce('batch_loss_reduce', losses, pt_util.mesh_reduce_losses)
        return i+1, preds, losses

    def _gen_distribute_dl(self, dl, data_type):
        shuffle, drop_last, collate_fn = False, False, None
        if data_type=='train':
            shuffle, drop_last = True, True
        # use original configure
        collate_fn = getattr(dl, 'collate_fn', collate_fn)
        shuffle = getattr(dl, 'shuffle', shuffle)
        ds, drop_last = dl.dataset, dl.drop_last
        if isinstance(ds, torch.utils.data.IterableDataset):
            return dl
        else:
            sampler = torch.utils.data.distributed.DistributedSampler(ds, num_replicas=xm.xrt_world_size(), rank=xm.get_ordinal(), shuffle=shuffle)
            dl = torch.utils.data.DataLoader(ds, batch_size=self.cfg.batch_size//xm.xrt_world_size(), sampler=sampler, num_workers=self.cfg.n_dl_worker, drop_last=drop_last, collate_fn=collate_fn)
        return dl

    def info(self, text, *args):
        if self.cfg.use_tpu:
            if xm.is_master_ordinal():
                logger.info(text, *args)
        else:
            logger.info(text, *args)

    def gen_bn_loader(self, dl, batch_size):
        shuffle, drop_last, collate_fn = True, True, None
        collate_fn = getattr(dl, 'collate_fn', collate_fn)
        ds, drop_last = dl.dataset, dl.drop_last
        dl = torch.utils.data.DataLoader(ds, batch_size=self.cfg.swa_batch_size, num_workers=self.cfg.n_dl_worker, drop_last=drop_last, collate_fn=collate_fn)
        return dl

    def bn_update(self, loader, batch_size=None, pt_model=None, device=None):
        r"""Updates BatchNorm running_mean, running_var buffers in the model.
        It performs one pass over data in `loader` to estimate the activation
        statistics for BatchNorm layers in the model.
        Args:
            loader (torch.utils.data.DataLoader): dataset loader to compute the
                activation statistics on. Each data batch should be either a
                tensor, or a list/tuple whose first element is a tensor
                containing data.
            model (torch.nn.Module): model for which we seek to update BatchNorm
                statistics.
            device (torch.device, optional): If set, data will be trasferred to
                :attr:`device` before being passed into :attr:`model`.
        """
        logger.info('update batch normalization')
        if self._model is None:
            self.create_model(pt_model=pt_model)
        model = self._model
        if batch_size is not None and batch_size != loader.batch_size:
            loader = self.gen_bn_loader(loader, batch_size)

        if not _check_bn(model):
            logger.info('check bn failed, not update bn')
            return
        was_training = model.training
        model.train()
        momenta = {}
        model.apply(_reset_bn)
        model.apply(lambda module: _get_momenta(module, momenta))
        n = 0
        for i, input in enumerate(loader):
            if isinstance(input, dict):
                for k, v in input.items():
                    b = v.size(0)
                    break
            else:
                raise NotImplementedError

            momentum = b / float(n + b)
            for module in momenta.keys():
                module.momentum = momentum

            self.fit_batch(input, i, 'test')
            n += b

        model.apply(lambda module: _set_momenta(module, momenta))
        model.train(was_training)

    def swap_swa_sgd(self, ds, model):
        logger.info('swap swa weights')
        self._opt.swap_swa_sgd()
        if not self.cfg.swa_disable_bn:
            self.bn_update(ds, self.cfg.swa_batch_size)

    def get_start_epoch(self):
        start_epoch = 0
        if self._restored_epoch is not None:
            start_epoch = self._restored_epoch + 1
        return start_epoch

    @XLA
    def fit(self, train_ds=None, val_ds=None, opt=None, pt_model=None, **kwargs):
        self.info('start fit')
        if self._model is None:
            self.create_model(opt=opt, pt_model=pt_model, **kwargs)

        best_loss = np.inf;
        best_epoch, step, save_opt = -1, 0, self.cfg.save_opt
        start_epoch = self.get_start_epoch()
        for epoch in range(start_epoch, start_epoch + self.cfg.epochs):
            ## need this because numpy will use same random state for epoch fork subprocess
            np.random.seed(self.cfg.seed + epoch)
            random.seed(self.cfg.seed+epoch)

            self.info(os.linesep)
            loss = None
            if train_ds is not None and not self.cfg.only_validate:
                step, losses = self.fit_epoch(train_ds, epoch, step, **kwargs)
                loss = losses['loss']
                if (epoch+1)>=self.cfg.swa_start_epoch and self.cfg.swa_start_epoch>0:
                    if (epoch+1)==self.cfg.swa_start_epoch:
                        logger.info('start update swa')
                    self._opt.update_swa()
            preds = None
            if val_ds is not None and (epoch+1)>self.cfg.n_init_epoch and not self.cfg.no_validate:
                val_step, preds, val_losses = self.val_epoch(val_ds, epoch)
                val_loss = val_losses['val_loss']
                self.info('loss for epoch %s:, train: %s, val: %s', epoch,  loss, val_loss)
                if self.cfg.scoring:
                    s = self.score(val_ds, preds=preds)
                    if self.cfg.use_tpu:
                        s = xm.mesh_reduce('score reduce', s, np.mean)
                        self.info("reduced score is:%s", s)
                if val_loss < (best_loss*(1-self.cfg.es_min_delta)):
                    best_loss = val_loss
                    best_epoch = epoch
                    if self.cfg.save_best and (epoch+1)>self.cfg.n_init_epoch:
                        if self.cfg.swa_start_epoch>0:
                            self.swap_swa_sgd(train_ds, self._model)
                        self.save(save_opt=save_opt, epoch=epoch)
                if self._should_stop(best_loss, val_loss, best_epoch, epoch):
                    self.info(
                        "best_loss:%s, best_epoch:%s, current_epoch:%s, val_loss:%s, es_min_delta:%s, without improvement for %s epochs, train done",
                        best_loss, best_epoch, epoch, val_loss, self.cfg.es_min_delta, self.cfg.n_es_epoch)
                    save_opt = False
                    break
                elif self.cfg.only_validate:
                    break
                else:
                    self.info('best val loss:%s, best epoch:%s', best_loss, best_epoch)
            if ((epoch + 1) % (self.cfg.n_save_epoch) == 0) and (epoch+1)>self.cfg.n_init_epoch:
                if self.cfg.swa_start_epoch > 0:
                    self.swap_swa_sgd(train_ds, self._model)
                self.info('%%%% save model to %s for epoch:%s', self.cfg.output_dir, epoch)
                self.save(global_step=step, save_opt=save_opt, epoch=epoch)
            if not self.cfg.only_validate and step % self.cfg.n_train_step == 0:
                self.info('total train step %s done', self.cfg.n_train_step)
                break
        if self.cfg.save or self.cfg.save_best or (self.cfg.n_save_epoch < self.cfg.N_INF) or (self.cfg.n_save_step < self.cfg.N_INF):
            if not self.cfg.only_validate and not self.cfg.save_best:
                if self.cfg.swa_start_epoch > 0:
                    self.swap_swa_sgd(train_ds, self._model)
                self.save(save_opt=save_opt, epoch=epoch)
            if preds is not None and self.cfg.save_pred:
                self.save_predict(preds, '_val')

    def save_predict(self, pred, suffix=''):
        if not self.cfg.use_tpu:
            super(PTModel, self).save_predict(pred, suffix=suffix)
        else:
            if xm.is_master_ordinal():
                super(PTModel, self).save_predict(pred, suffix=suffix)

    def score(self, ds, preds=None):
        raise NotImplemented


class ModelEma:
    """ Model Exponential Moving Average
    ref:https://github.com/rwightman/efficientdet-pytorch
    Keep a moving average of everything in the model state_dict (parameters and buffers).

    This is intended to allow functionality like
    https://www.tensorflow.org/api_docs/python/tf/train/ExponentialMovingAverage

    A smoothed version of the weights is necessary for some training schemes to perform well.
    E.g. Google's hyper-params for training MNASNet, MobileNet-V3, EfficientNet, etc that use
    RMSprop with a short 2.4-3 epoch decay period and slow LR decay rate of .96-.99 requires EMA
    smoothing of weights to match results. Pay attention to the decay constant you are using
    relative to your update count per epoch.

    To keep EMA from using GPU resources, set device='cpu'. This will save a bit of memory but
    disable validation of the EMA weights. Validation will have to be done manually in a separate
    process, or after the training stops converging.

    This class is sensitive where it is initialized in the sequence of model init,
    GPU assignment and distributed training wrappers.
    I've tested with the sequence in my own train.py for torch.DataParallel, apex.DDP, and single-GPU.
    """
    def __init__(self, model, decay=0.9999, device='', resume=''):
        # make a copy of the model for accumulating moving average of weights
        self.ema = deepcopy(model)
        self.ema.eval()
        self.decay = decay
        self.device = device  # perform ema on different device from model if set
        if device:
            self.ema.to(device=device)
        self.ema_has_module = hasattr(self.ema, 'module')
        if resume:
            self._load_checkpoint(resume)
        for p in self.ema.parameters():
            p.requires_grad_(False)

    def _load_checkpoint(self, checkpoint_path):
        checkpoint = torch.load(checkpoint_path, map_location='cpu')
        assert isinstance(checkpoint, dict)
        if 'state_dict_ema' in checkpoint:
            new_state_dict = OrderedDict()
            for k, v in checkpoint['state_dict_ema'].items():
                # ema model may have been wrapped by DataParallel, and need module prefix
                if self.ema_has_module:
                    name = 'module.' + k if not k.startswith('module') else k
                else:
                    name = k
                new_state_dict[name] = v
            self.ema.load_state_dict(new_state_dict)
            logger.info("Loaded state_dict_ema")
        else:
            logger.warning("Failed to find state_dict_ema, starting from loaded model weights")

    def update(self, model):
        # correct a mismatch in state dict keys
        needs_module = hasattr(model, 'module') and not self.ema_has_module
        with torch.no_grad():
            msd = model.state_dict()
            for k, ema_v in self.ema.state_dict().items():
                if needs_module:
                    k = 'module.' + k
                model_v = msd[k].detach()
                if self.device:
                    model_v = model_v.to(device=self.device)
                ema_v.copy_(ema_v * self.decay + (1. - self.decay) * model_v)

