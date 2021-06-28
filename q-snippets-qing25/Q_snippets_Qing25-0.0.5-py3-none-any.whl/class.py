import torch
import torch.nn as nn
import torch.nn.functional as F
import pytorch_lightning as pl
# from tensor_ops import safesoftmax
# from q_snippets.tensor_ops import safesoftmax


class RoPE(pl.LightningModule):
    def __init__(self, dim, max_seq_len=513, device=None):
        """
            ref: https://kexue.fm/archives/8265
            创建最大长度，维度固定的pos_emebddings
        """
        super().__init__()
        self.dim = dim
        self.seq_len = max_seq_len
        # self.device = device
        self.embeddings = self._create_pos_embedding()

    def _create_pos_embedding(self):
        position_ids = torch.arange(0, self.seq_len, dtype=torch.float, device=self.device)[None]  # (1, seqlen)
        indices = torch.arange(0, self.dim//2, dtype=torch.float, device=self.device)  # odd not work?
        indices = torch.pow(10000.0, -2*indices/self.dim)
        
        embeddings = torch.einsum("bn,d->bnd", position_ids, indices)
        embeddings = torch.stack([torch.sin(embeddings), torch.cos(embeddings)], dim=-1)
        embeddings = torch.reshape(embeddings, (-1, self.seq_len, self.dim))
        return embeddings
    
    def add_pos_embedding(self,qw):
        """
            输入向量序列(bsz,seq_len,dim)，返回乘上了RoPE的结果
        """
        bsz, seq_len, dim = qw.size()
        pos = self.embeddings[:, seq_len, :]
        cos_pos = torch.repeat_interleave(pos[..., 1::2], 2, dim=-1).to(self.device)
        sin_pos = torch.repeat_interleave(pos[..., ::2], 2, dim=-1).to(self.device)
        qw2 = torch.stack([-qw[...,1::2], qw[...,::2]], dim=-1)
        qw2 = torch.reshape(qw2, qw.shape)
        # print(self.device, qw.device, qw2.device, cos_pos.device)
        qw = qw*cos_pos + qw2*sin_pos
        return qw


class CircleLoss(nn.Module):
    """ https://arxiv.org/abs/2002.10857v2  Equation.4 """
    def __init__(self, optim_pos=1, optim_neg=0, temperature=10):
        """ 做完softmax之后分类 最优情况下 optim_p,  optim_n = 1, 0 
            cosim 得分的话  optim_p,  optim_n = 1, -1
        """
        super().__init__()
        self.optim_pos = optim_pos
        self.optim_neg = optim_neg
        self.temperature = temperature

    def forward(self, pred, gold):
        """ replacing ce, pred should be softmaxed """
        # pred = safesoftmax(pred)
        pred = torch.softmax(pred, dim=-1)
        bsz, num_classes = pred.size()
        pos_ones = F.one_hot(gold, num_classes)
        neg_ones = torch.ones_like(pos_ones) - pos_ones
        
        alpha_p = torch.clamp_min(self.optim_pos - pred, min=0)
        alpha_n = torch.clamp_min(pred - self.optim_neg, min=0)
        p_dists = torch.exp(-pred * self.temperature * alpha_p) * pos_ones
        n_dists = torch.exp(pred * self.temperature * alpha_n ) * neg_ones

        p_dists = torch.sum(p_dists, 1, True)
        n_dists = torch.sum(n_dists, 1, True)
        loss = torch.log(1+ (n_dists)*(p_dists))
        loss = loss.mean()
        return loss

class FocalLoss(nn.Module):
    def __init__(self, gamma=1.6, alpha=0.4, size_average=True):
        """ alpha 是乘到负样本的loss上的权重，正样本是(1-alpha); None的话，两者相同，或者设为0.5?
            取该类别样本数目比例的倒数？
        """
        super(FocalLoss, self).__init__()
        self.gamma = gamma
        self.alpha = alpha
        if isinstance(alpha, (float,int)): self.alpha = torch.Tensor([alpha,1-alpha])
        if isinstance(alpha, list): self.alpha = torch.Tensor(alpha)
        self.size_average = size_average

    def forward(self, input, target):
        if input.dim() > 2:
            input = input.view(input.size(0), input.size(1),-1)
            input = input.transpose(1, 2)
            input = input.contiguous().view(-1, input.size(2))
        target = target.view(-1, 1)

        logpt = F.log_softmax(input, dim=-1)
        logpt = logpt.gather(1, target)
        logpt = logpt.view(-1)
        pt = logpt.data.exp()

        if self.alpha is not None:
            if self.alpha.type() != input.data.type():
                self.alpha = self.alpha.type_as(input.data)
            at = self.alpha.gather(0, target.data.view(-1))
            logpt = logpt * at

        loss = -1 * (1-pt)**self.gamma * logpt
        if self.size_average: 
            return loss.mean()
        else: 
            return loss.sum()
