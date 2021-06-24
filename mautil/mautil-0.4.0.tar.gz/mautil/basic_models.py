import os, logging
from collections import namedtuple, defaultdict, OrderedDict
from copy import deepcopy
import pprint
import numpy as np

from . import util

logger = logging.getLogger(__name__)

InputFeature = namedtuple('InputFeature', ['name', 'shape', 'dtype', 'sparse'])
InputFeature.__new__.__defaults__ = (None, None, None, False)


class BasicCFG(object):
    def update(self, cfg):
        for k, v in cfg.items():
            attr = getattr(self, k, None)
            if isinstance(attr, dict):
                #attr.update(v)
                util.update_dict(attr, v)
            else:
                setattr(self, k, v)

    def dump(self, fpath):
        dirname = os.path.dirname(fpath)
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        save_dict = self.__dict__
        util.dump_json(save_dict, fpath, ensure_ascii=False)

    def load(self, fpath):
        cfg = util.load_json(fpath)
        self.update(cfg)

    def copy(self):
        return deepcopy(self)

    def __str__(self):
        return pprint.pformat(self.__dict__, indent=4)

class CFG(BasicCFG):
    N_INF = int(1e16)
    def __init__(self):
        self.seed = 9527
        self.show_cfg = False

        ## lr
        self.lr = 1e-3
        self.n_lr_warmup_step = 0
        self.n_lr_decay_step = self.N_INF
        self.lr_decay_rate = 1.0
        self.lr_scheduler = None
        self.lr_scheduler_paras = {}

        ## optimizer
        self.opt = 'adamW'
        self.opt_paras = {}

        ## deepspeed
        self.use_deepspeed = False
        self.deepspeed = {
            "fp16": {
                "enabled": False,
                #"loss_scale": 0,
                #"loss_scale_window": 1000,
                #"hysteresis": 2,
                #"min_loss_scale": 1
            },

            "zero_optimization": {
                "stage": 2,
                "allgather_partitions": True,
                "allgather_bucket_size": 5e8,
                "overlap_comm": True,
                "reduce_scatter": True,
                "reduce_bucket_size": 5e8,
                "contiguous_gradients": True,
                "cpu_offload": True
            },

           "optimizer": {
             "type": "AdamW",
           },
           "zero_allow_untested_optimizer": True,

        }


        # train
        self.patience = 1
        self.es_min_delta = 0.0005  ## early stop
        self.n_es_epoch = 1  ## early stop
        self.batch_size = 32
        self.val_batch_size = self.batch_size
        self.abnormal_loss_thr = 0.1 # minimum percentage train loss improvement
        self.n_init_epoch = 0
        self.n_save_step = self.N_INF
        self.n_save_epoch = self.N_INF
        self.n_epoch_step = self.N_INF
        self.n_train_step = self.N_INF
        self.weight_decay = 0
        self.validation_steps = None
        self.validation_freq = 1
        self.epochs = 2
        self.scoring = False
        self.save = False  # if save model after fit
        self.save_best = False  # if save  best model
        self.only_validate = False
        self.no_validate = False
        self.use_fp16 = False
        self.save_opt = False
        self.xla_share_model = False
        self.debug = False
        self.dropout = 0
        self.data_dir = '../data'
        self.output_dir = '../data'
        self.model_dir = None # use data_dir if None
        self.swa_start_epoch = 0 # stochastic weight average if >0. pt only.
        self.ema = None
        # gpu
        self.device = None
        # save and restore
        self.restored_epoch = None
        self.saved_epoch = None
        self.n_keep_ckpt = 1
        self.saved_ckpts = []
        self.restore = False
        self.restore_epoch= None
        self.restore_step = None
        self.restore_strict = False
        # predicting
        self.verbose = 32
        self.to_list = True
        self.do_concat = False
        self.batch_keys = []  # key to output for net output dict
        # self distill
        self.sd_weight = 0.0
        self.sd_warmup_step = 1000



class LossHist(defaultdict):
    def __init__(self, decimal_digits=8, *args, **kwargs):
        self._fstr = "{}:{:." + str(decimal_digits) + "f}"
        super(LossHist, self).__init__(list, *args, **kwargs)

    def append(self, losses):
        for name, loss in losses.items():
            self[name].append(loss)

    def get_avg(self):
        avg_loss = OrderedDict()
        keys = sorted(self.keys())
        for key in keys:
            avg_loss[key] = np.mean(self[key])
        return avg_loss

    def get_avg_sum(self):
        avg_loss = self.get_avg()
        return np.sum([v for k, v in avg_loss.items()])

    def avg_output(self):
        avg_loss = self.get_avg()
        #tot = np.sum(v for k, v in avg_loss.items())
        #avg_loss['tot'] = tot
        outstr = ', '.join(self._fstr.format(k, v) for k, v in avg_loss.items())
        return outstr


class Model(object):
    cfg = CFG()

    def __init__(self, name, cfg={}):
        self.name = name
        self.update_cfg = cfg
        self.cfg = deepcopy(self.cfg)
        self.cfg.update(self.update_cfg)
        util.update_deepspeed_cfg(self.cfg)
        self.restored_cfg = None

        self._rs = np.random.RandomState(self.cfg.seed)

        self._model = None

#        if self.cfg.save and not self.cfg.only_validate and not self.cfg.no_train and not self.cfg.restore:
#            fpath = self.gen_fname('cfg.json')
#            self.cfg.dump(fpath)

        if self.cfg.show_cfg:
            logging.info('model cfg is: %s', self.cfg)


    def create_model(self):
        return self

    def fit(self, train_dataset=None, val_dataset=None, **kwargs):
        best_loss = np.inf;
        best_epoch = -1;
        step = 0
        for epoch in range(self.cfg.epochs):
            if not self.cfg.only_validate:
                step = self.fit_epoch(train_dataset, epoch, step, **kwargs)
                if (epoch + 1) % (self.cfg.n_save_epoch) == 0:
                    logger.info('%%%% save model to %s for epoch:%s', self.cfg.output_dir, epoch)
                    self.save(self.cfg.output_dir, epoch=epoch)
            if val_dataset is not None:
                val_loss = self.val_epoch(val_dataset, epoch)
                if val_loss < best_loss:
                    best_loss = val_loss
                    best_epoch = epoch
                if self.should_stop(self.cfg.es, self.cfg.n_es_epoch, best_loss, val_loss, best_epoch, epoch):
                    break
                if self.cfg.only_validate:
                    break
            if not self.cfg.only_validate and step % self.cfg.n_train_step == 0:
                logger.info('total train step %s done', self.cfg.n_train_step)
                break
        if self.cfg.save and (epoch + 1) % (self.cfg.n_save_epoch) != 0 and (step % self.cfg.n_save_step != 0):
            logger.info('%%%% save model to %s', self.cfg.output_dir)
            self.save(self.cfg.output_dir)

    def _should_stop(self, best_val_loss, val_loss, best_epoch=-1, current_epoch=-1):
        stop = False
        if ((best_val_loss - val_loss) / val_loss < -self.cfg.es_min_delta) and (
                current_epoch - best_epoch) >= self.cfg.n_es_epoch:
            stop = True
        return stop


    def gen_fname(self, *paras, data_dir=None):
        """

        :param paras: subdirectories and/or file name
        :return:
        """
        name = self.name
        if self.cfg.debug:
            name = 'debug_' + name
        if data_dir is None:
            data_dir = self.cfg.output_dir
        fname = os.path.join(data_dir, name, *paras)
        return fname

    def restore(self, model_dir=None):
        if model_dir is None:
            fpath = None
        else:
            fpath = os.path.join(model_dir, 'cfg.json')
        self.restore_cfg(fpath)

    def restore_cfg(self, fpath=None):
        if fpath is None:
            fpath = self.gen_fname('cfg.json')
        self.cfg.load(fpath)
        self.restored_cfg = self.cfg.copy()
        self.cfg.update(self.update_cfg)
        if self.cfg.show_cfg:
            logging.info('model cfg after restore is: %s', self.cfg)

    def save(self):
        self.save_cfg()

    def save_cfg(self):
        fpath = self.gen_fname('cfg.json')
        dirname = os.path.dirname(fpath)
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        self.cfg.dump(fpath)

    def save_predict(self, pred, suffix=''):
        fpath = self.gen_fname('pred' + suffix + '.dump')
        util.dump(pred, fpath)
        logger.info('saved:%s', fpath)

    def load_predict(self, suffix=''):
        fpath = self.gen_fname('pred' + suffix + '.dump')
        pred = util.load_dump(fpath)
        return pred

    def predict(self, x):
        pred = self._model.predict(x)
        return pred

    def score(self, x, y):
        pass
