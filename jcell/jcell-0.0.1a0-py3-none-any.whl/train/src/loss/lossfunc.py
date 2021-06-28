from __future__ import division
import torch
import numpy as np
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from itertools import filterfalse as ifilterfalse

from netframework import save_defaults, load_defaults


class WCE_DICE(nn.Module):
    @save_defaults
    @load_defaults
    def __init__(self, power=1, smooth=0.00000001):
        super(WCE_DICE, self).__init__()
        self.power = power
        self.smooth = smooth

    def crop(self, w, h, target):
        nt, ht, wt = target.size()
        offset_w, offset_h = (wt - w) // 2, (ht - h) // 2
        if offset_w > 0 and offset_h > 0:
            target = target[:, offset_h:-offset_h, offset_w:-offset_w].clone()

        return target

    def to_one_hot(self, target, size):
        n, c, h, w = size

        ymask = torch.FloatTensor(size).zero_()
        new_target = torch.LongTensor(n, 1, h, w)
        if target.is_cuda:
            ymask = ymask.cuda(target.get_device())
            new_target = new_target.cuda(target.get_device())

        new_target[:, 0, :, :] = torch.clamp(target.detach(), 0, c - 1)
        ymask.scatter_(1, new_target, 1.0)

        return torch.autograd.Variable(ymask)

    def forward(self, input, target, weight=None):
        assert (
            input.dim() == 4
        ), "So far WCE+Dice is only supported for 2D data."

        smooth = self.smooth
        n, c, h, w = input.size()
        log_p = F.log_softmax(input, dim=1)

        target = self.crop(w, h, target)
        ymask = self.to_one_hot(target, log_p.size())

        if weight is not None:
            weight = self.crop(w, h, weight)
            for classes in range(c):
                ymask[:, classes, :, :] = ymask[:, classes, :, :].clone() * (
                    weight ** self.power
                )

        logpy = (log_p * ymask).sum(1)
        loss = -(logpy).mean()

        p = F.softmax(input, dim=1)

        iflat = p[:, 1].contiguous().view(-1)
        tflat = ymask[:, 1].contiguous().view(-1)
        intersection = (iflat * tflat).sum()
        lossd = 1 - (
            (2.0 * intersection + smooth)
            / (iflat.sum() + tflat.sum() + smooth)
        )

        iflat = p[:, 2].contiguous().view(-1)
        tflat = ymask[:, 2].contiguous().view(-1)
        intersection = (iflat * tflat).sum()
        if tflat.sum().item() > 0:
            lossd += 1 - (
                (2.0 * intersection + smooth)
                / (iflat.sum() + tflat.sum() + smooth)
            )

        return loss + lossd


class WCE_JReg(nn.Module):
    @save_defaults
    @load_defaults
    def __init__(
        self, lambda_dict=None, power=1, lambda_vect=None, lambda_const=None
    ):
        super(WCE_JReg, self).__init__()
        self.J2D = WCE_J_SIMPL(lambda_dict, power, lambda_vect, lambda_const)
        self.J3D = WCE_J_SIMPL3D(lambda_dict, power, lambda_vect, lambda_const)

    def forward(self, input, target, weight=None):
        if input.dim() == 4:
            return self.J2D(input, target, weight)
        elif input.dim() == 5:
            return self.J3D(input, target, weight)
        return torch.zeros((1,))


class WCE_J_SIMPL3D(nn.Module):
    def __init__(
        self, lambda_dict=None, power=1, lambda_vect=None, lambda_const=None
    ):
        super(WCE_J_SIMPL3D, self).__init__()
        self.power = power
        self.lambda_mat = dict()

        if (
            lambda_dict is not None
            and lambda_vect is not None
            and lambda_const is not None
        ):
            raise ValueError("Please provide only one lambda parameter")

        if lambda_dict is None and lambda_vect is None:
            self.lambda_mat = None

        if lambda_dict is not None:
            c = len(list(lambda_dict.keys()))
            self.lambda_mat = self.ones_dict(c, c)
            for key1, row in lambda_dict.items():
                if int(key1) not in list(self.lambda_mat.keys()):
                    self.lambda_mat[int(key1)] = dict()
                for key2, value in row.items():
                    self.lambda_mat[int(key1)][int(key2)] = float(value)

        elif lambda_vect is not None:
            llv = len(lambda_vect)
            if np.round(np.sqrt(llv)) ** 2 == llv:
                c = np.round(np.sqrt(llv)).astype(int)
                self.lambda_mat = self.ones_dict(c, c)
                k = 0
                for i in range(c):
                    for j in range(c):
                        self.lambda_mat[i][j] = lambda_vect[k]
                        k += 1
            else:
                c = -1
                for i in range(1000):
                    if ((2 * llv) / (i + 1)) == i:
                        c = i
                        break
                if c == -1:
                    raise ValueError("Please provide a valid lambda vector")

                self.lambda_mat = self.ones_dict(c, c)
                k = 0
                for i in range(c):
                    for j in range(i, c):
                        self.lambda_mat[i][j] = lambda_vect[k]
                        self.lambda_mat[j][i] = lambda_vect[k]
                        k += 1

        elif lambda_const is not None:
            self.const = lambda_const

        else:
            self.const = 0.5

    def ones_dict(self, d1, d2):
        lambda_mat = dict()
        for i in range(d1):
            if i not in list(lambda_mat.keys()):
                lambda_mat[i] = dict()
            for j in range(d2):
                lambda_mat[i][j] = float(1)
        return lambda_mat

    def zf_dict(self, d1, d2):
        lambda_mat = dict()
        for i in range(d1):
            if i not in list(lambda_mat.keys()):
                lambda_mat[i] = dict()
            for j in range(d2):
                lambda_mat[i][j] = float(self.const)
        return lambda_mat

    def crop(self, w, h, d, target):
        nt, dt, ht, wt = target.size()
        offset_w, offset_h, offset_d = (
            (wt - w) // 2,
            (ht - h) // 2,
            (dt - d) // 2,
        )
        if offset_w > 0 and offset_h > 0 and offset_d > 0:
            target = target[
                :, offset_d:-offset_d, offset_h:-offset_h, offset_w:-offset_w
            ].clone()

        return target

    def to_one_hot(self, target, size):
        n, c, d, h, w = size

        ymask = torch.FloatTensor(size).zero_()
        new_target = torch.LongTensor(n, 1, d, h, w)
        if target.is_cuda:
            ymask = ymask.cuda(target.get_device())
            new_target = new_target.cuda(target.get_device())

        new_target[:, 0, :, :, :] = torch.clamp(target.detach(), 0, c - 1)
        ymask.scatter_(1, new_target, 1.0)

        return torch.autograd.Variable(ymask)

    def forward(self, input, target, weight=None):
        eps = 0.00000001

        n, c, d, h, w = input.size()
        if self.lambda_mat is None:
            lamb = self.zf_dict(c, c)
        else:
            assert (
                len(list(self.lambda_mat.keys())) == c
            ), "Lambda is expected to have dimension {}x{} but got {}x{} instead".format(
                c,
                c,
                len(list(self.lambda_mat.keys())),
                len(list(self.lambda_mat.keys())),
            )
            lamb = self.lambda_mat

        log_p = F.log_softmax(input, dim=1)
        target = self.crop(w, h, d, target)
        ymask = self.to_one_hot(target, log_p.size()).float()

        p = F.softmax(input, dim=1)

        p = p.permute(0, 2, 3, 4, 1).reshape((-1, c))
        log_p = log_p.permute(0, 2, 3, 4, 1).reshape((-1, c))
        ymask = ymask.permute(0, 2, 3, 4, 1).reshape((-1, c))
        all_sums = ymask.sum(0)
        lossd = 0

        final_mat = torch.matmul(p.T, ymask)
        for i in range(c):
            ni = all_sums[i]
            for j in range(c):
                nj = all_sums[j]
                if i == j:
                    continue

                if (ni * nj).item() > 0:
                    tmp_loss = -lamb[i][j] * torch.log(
                        (
                            0.5 * (final_mat[i, i] / ni - final_mat[i, j] / nj)
                            + 0.5
                        )
                        ** self.power
                        + eps
                    )
                else:
                    tmp_loss = (
                        torch.zeros((1,)).float().to(final_mat.device)
                    )[0]

                lossd += tmp_loss

        # weighted cross entropy
        if weight is not None:
            weight = self.crop(w, h, d, weight).reshape((-1, 1))
            for classes in range(c):
                ymask[..., classes] = (
                    lamb[classes][classes]
                    * ymask[..., classes].clone()
                    * (weight)
                )

        loss = -((log_p * ymask).sum(1)).mean()

        return loss + lossd.squeeze()


class WCE_J_SIMPL(nn.Module):
    def __init__(
        self, lambda_dict=None, power=1, lambda_vect=None, lambda_const=None
    ):
        super(WCE_J_SIMPL, self).__init__()
        self.power = power
        self.lambda_mat = dict()

        if (
            lambda_dict is not None
            and lambda_vect is not None
            and lambda_const is not None
        ):
            raise ValueError("Please provide only one lambda parameter")

        if lambda_dict is None and lambda_vect is None:
            self.lambda_mat = None

        if lambda_dict is not None:
            c = len(list(lambda_dict.keys()))
            self.lambda_mat = self.ones_dict(c, c)
            for key1, row in lambda_dict.items():
                if int(key1) not in list(self.lambda_mat.keys()):
                    self.lambda_mat[int(key1)] = dict()
                for key2, value in row.items():
                    self.lambda_mat[int(key1)][int(key2)] = float(value)

        elif lambda_vect is not None:
            llv = len(lambda_vect)
            if np.round(np.sqrt(llv)) ** 2 == llv:
                c = np.round(np.sqrt(llv)).astype(int)
                self.lambda_mat = self.ones_dict(c, c)
                k = 0
                for i in range(c):
                    for j in range(c):
                        self.lambda_mat[i][j] = lambda_vect[k]
                        k += 1
            else:
                c = -1
                for i in range(1000):
                    if ((2 * llv) / (i + 1)) == i:
                        c = i
                        break
                if c == -1:
                    raise ValueError("Please provide a valid lambda vector")

                self.lambda_mat = self.ones_dict(c, c)
                k = 0
                for i in range(c):
                    for j in range(i, c):
                        self.lambda_mat[i][j] = lambda_vect[k]
                        self.lambda_mat[j][i] = lambda_vect[k]
                        k += 1

        elif lambda_const is not None:
            self.const = lambda_const

        else:
            self.const = 0.5

        if self.lambda_mat is not None:
            print("Using lambda matrix:")
            for key1, row in self.lambda_mat.items():
                for key2, value in row.items():
                    print(
                        "{0:.4f}".format(
                            self.lambda_mat[int(key1)][int(key2)]
                        ),
                        end=" ",
                    )
                print("")

    def ones_dict(self, d1, d2):
        lambda_mat = dict()
        for i in range(d1):
            if i not in list(lambda_mat.keys()):
                lambda_mat[i] = dict()
            for j in range(d2):
                lambda_mat[i][j] = float(1)
        return lambda_mat

    def zf_dict(self, d1, d2):
        lambda_mat = dict()
        for i in range(d1):
            if i not in list(lambda_mat.keys()):
                lambda_mat[i] = dict()
            for j in range(d2):
                lambda_mat[i][j] = float(self.const)
        return lambda_mat

    def crop(self, w, h, target):
        nt, ht, wt = target.size()
        offset_w, offset_h = (wt - w) // 2, (ht - h) // 2
        if offset_w > 0 and offset_h > 0:
            target = target[:, offset_h:-offset_h, offset_w:-offset_w].clone()

        return target

    def to_one_hot(self, target, size):
        n, c, h, w = size

        ymask = torch.FloatTensor(size).zero_().to(target.device)
        new_target = torch.LongTensor(n, 1, h, w).to(target.device)

        new_target[:, 0, :, :] = torch.clamp(target.detach(), 0, c - 1)
        ymask.scatter_(1, new_target, 1.0)

        return torch.autograd.Variable(ymask)

    def forward(self, input, target, weight=None):
        eps = 0.00000001

        n, c, h, w = input.size()
        if self.lambda_mat is None:
            lamb = self.zf_dict(c, c)
        else:
            assert (
                len(list(self.lambda_mat.keys())) == c
            ), "Lambda is expected to have dimension {}x{} but got {}x{} instead".format(
                c,
                c,
                len(list(self.lambda_mat.keys())),
                len(list(self.lambda_mat.keys())),
            )
            lamb = self.lambda_mat

        log_p = F.log_softmax(input + eps, dim=1)
        target = self.crop(w, h, target)
        ymask = self.to_one_hot(target, log_p.size()).float()

        p = F.softmax(input, dim=1)

        p = p.permute(0, 2, 3, 1).reshape((-1, c))
        log_p = log_p.permute(0, 2, 3, 1).reshape((-1, c))
        ymask = ymask.permute(0, 2, 3, 1).reshape((-1, c))
        all_sums = ymask.sum(0)
        lossd = 0

        final_mat = torch.matmul(p.T, ymask)
        for i in range(c):
            ni = all_sums[i]
            for j in range(c):
                nj = all_sums[j]
                if i == j:
                    continue

                if (ni * nj).item() > 0:
                    tmp_loss = -lamb[i][j] * torch.log(
                        (
                            0.5 * (final_mat[i, i] / ni - final_mat[i, j] / nj)
                            + 0.5
                        )
                        ** self.power
                        + eps
                    )
                else:
                    tmp_loss = (
                        torch.zeros((1,)).float().to(final_mat.device)
                    )[0]

                lossd += tmp_loss

        # weighted cross entropy
        if weight is not None:
            weight = self.crop(w, h, weight).reshape((-1, 1))
            for classes in range(c):
                ymask[..., classes] = (
                    ymask[..., classes].clone()
                    * lamb[classes][classes]
                    * (weight)
                )

        loss = -((log_p * ymask).sum(1)).mean()

        return loss + lossd


class WeightedCrossEntropy(nn.Module):
    @save_defaults
    @load_defaults
    def __init__(self, power=1, sum=False):
        super(WeightedCrossEntropy, self).__init__()
        self.WCE2D = WeightedCrossEntropy2d(power, sum)
        self.WCE3D = WeightedCrossEntropy3d(power, sum)

    def forward(self, input, target, weight=None):
        if input.dim() == 4:
            return self.WCE2D(input, target, weight)
        elif input.dim() == 5:
            return self.WCE3D(input, target, weight)
        return torch.zeros((1,))


class WeightedCrossEntropy3d(nn.Module):
    def __init__(self, power=1, sum=False):
        super(WeightedCrossEntropy3d, self).__init__()
        self.power = power
        self.sum = sum

    def to_one_hot(self, target, size):
        n, c, d, h, w = size

        ymask = torch.FloatTensor(size).zero_()
        new_target = torch.LongTensor(n, 1, d, h, w)
        if target.is_cuda:
            ymask = ymask.cuda(target.get_device())
            new_target = new_target.cuda(target.get_device())

        new_target[:, 0, :, :, :] = torch.clamp(target.detach(), 0, c - 1)
        ymask.scatter_(1, new_target, 1.0)

        return torch.autograd.Variable(ymask)

    def forward(self, input, target, weight=None):
        n, c, d, h, w = input.size()
        log_p = F.log_softmax(input, dim=1)

        ymask = self.to_one_hot(target, log_p.size())

        if weight is not None:
            for classes in range(c):
                ymask[:, classes, :, :, :] = ymask[
                    :, classes, :, :, :
                ].clone() * (weight ** self.power)

        logpy = (log_p * ymask).sum(1)
        if self.sum:
            loss = -(logpy).sum()
        else:
            loss = -(logpy).mean()

        return loss


class WeightedCrossEntropy2d(nn.Module):
    def __init__(self, power=1, sum=False):
        super(WeightedCrossEntropy2d, self).__init__()
        self.power = power
        self.sum = sum

    def crop(self, w, h, target):
        nt, ht, wt = target.size()
        offset_w, offset_h = (wt - w) // 2, (ht - h) // 2
        if offset_w > 0 and offset_h > 0:
            target = target[:, offset_h:-offset_h, offset_w:-offset_w].clone()

        return target

    def to_one_hot(self, target, size):
        n, c, h, w = size

        ymask = torch.FloatTensor(size).zero_()
        new_target = torch.LongTensor(n, 1, h, w)
        if target.is_cuda:
            ymask = ymask.cuda(target.get_device())
            new_target = new_target.cuda(target.get_device())

        new_target[:, 0, :, :] = torch.clamp(target.detach(), 0, c - 1)
        ymask.scatter_(1, new_target, 1.0)

        return torch.autograd.Variable(ymask)

    def forward(self, input, target, weight=None):
        n, c, h, w = input.size()
        log_p = F.log_softmax(input, dim=1)

        target = self.crop(w, h, target)
        ymask = self.to_one_hot(target, log_p.size())

        if weight is not None:
            weight = self.crop(w, h, weight)
            for classes in range(c):
                ymask[:, classes, :, :] = ymask[:, classes, :, :].clone() * (
                    weight ** self.power
                )

        logpy = (log_p * ymask).sum(1)
        if self.sum:
            loss = -(logpy).sum()
        else:
            loss = -(logpy).mean()

        return loss


class WeightedFocalLoss2d(nn.Module):
    @save_defaults
    @load_defaults
    def __init__(self, gamma=2, power=1):
        super(WeightedFocalLoss2d, self).__init__()
        self.gamma = gamma
        self.power = power

    def crop(self, w, h, target):
        nt, ht, wt = target.size()
        offset_w, offset_h = (wt - w) // 2, (ht - h) // 2
        if offset_w > 0 and offset_h > 0:
            target = target[:, offset_h:-offset_h, offset_w:-offset_w]

        return target

    def to_one_hot(self, target, size):
        n, c, h, w = size

        ymask = torch.FloatTensor(size).zero_()
        new_target = torch.LongTensor(n, 1, h, w)
        if target.is_cuda:
            ymask = ymask.cuda(target.get_device())
            new_target = new_target.cuda(target.get_device())

        new_target[:, 0, :, :] = torch.clamp(target.detach(), 0, c - 1)
        ymask.scatter_(1, new_target, 1.0)

        return torch.autograd.Variable(ymask)

    def forward(self, input, target, weight=None):
        assert (
            input.dim() == 4
        ), "So far WeightedFocalLoss is only supported for 2D data."

        n, c, h, w = input.size()
        log_p = F.log_softmax(input, dim=1)

        target = self.crop(w, h, target)
        ymask = self.to_one_hot(target, log_p.size())

        if weight is not None:
            weight = self.crop(w, h, weight)
            for classes in range(c):
                ymask[:, classes, :, :] = ymask[:, classes, :, :] * (
                    weight ** self.power
                )

        dweight = (1 - F.softmax(input, dim=1)) ** self.gamma
        logpy = (log_p * ymask * dweight).sum(1)
        loss = -(logpy).mean()

        return loss


class SoftDice(nn.Module):
    @save_defaults
    @load_defaults
    def __init__(self, smooth=1.0):
        super(SoftDice, self).__init__()
        self.smooth = smooth

    def crop(self, w, h, target):
        nt, ht, wt = target.size()
        offset_w, offset_h = (wt - w) // 2, (ht - h) // 2
        if offset_w > 0 and offset_h > 0:
            target = target[:, offset_h:-offset_h, offset_w:-offset_w]

        return target

    def to_one_hot(self, target, size):
        n, c, h, w = size

        ymask = torch.FloatTensor(size).zero_()
        new_target = torch.LongTensor(n, 1, h, w)
        if target.is_cuda:
            ymask = ymask.cuda(target.get_device())
            new_target = new_target.cuda(target.get_device())

        new_target[:, 0, :, :] = torch.clamp(target.detach(), 0, c - 1)
        ymask.scatter_(1, new_target, 1.0)

        return torch.autograd.Variable(ymask)

    def forward(self, input, target):
        assert (
            input.dim() == 4
        ), "So far SoftDice is only supported for 2D data."

        smooth = self.smooth
        loss = 0.0

        n, n_classes, h, w = input.size()
        target = self.crop(w, h, target)
        ymask = self.to_one_hot(target, input.size())

        p = F.softmax(input, dim=1)

        cw = 0
        for c in range(1, n_classes):
            iflat = p[:, c].contiguous().view(-1)
            tflat = ymask[:, c].contiguous().view(-1)
            intersection = (iflat * tflat).sum()

            cw += 1
            loss += 1 - (
                (2 * intersection + smooth)
                / (iflat.sum() + tflat.sum() + smooth)
            )
        loss /= cw
        return loss


"""
Lovasz-Softmax and Jaccard hinge loss in PyTorch
Maxim Berman 2018 ESAT-PSI KU Leuven (MIT License)
https://github.com/bermanmaxim/LovaszSoftmax/blob/master/pytorch/lovasz_losses.py
"""

# --------------------------- HELPER FUNCTIONS ---------------------------
def isnan(x):
    return x != x


def mean(l, ignore_nan=True, empty=0):
    """
    nanmean compatible with generators.
    """
    l = iter(l)
    if ignore_nan:
        l = ifilterfalse(isnan, l)
    try:
        n = 1
        acc = next(l)
    except StopIteration:
        if empty == "raise":
            raise ValueError("Empty mean")
        return empty
    for n, v in enumerate(l, 2):
        acc += v
    if n == 1:
        return acc
    return acc / n


def lovasz_grad(gt_sorted):
    """
    Computes gradient of the Lovasz extension w.r.t sorted errors
    See Alg. 1 in paper
    """
    p = len(gt_sorted)
    gts = gt_sorted.sum()
    intersection = gts - gt_sorted.float().cumsum(0)
    union = gts + (1 - gt_sorted).float().cumsum(0)
    jaccard = 1.0 - intersection / union
    if p > 1:  # cover 1-pixel case
        jaccard[1:p] = jaccard[1:p] - jaccard[0:-1]
    return jaccard


# --------------------------- BINARY LOSSES ---------------------------


class LovaszHinge(nn.Module):
    def __init__(self):
        super(LovaszHinge, self).__init__()
        pass

    def crop(self, w, h, target):
        nt, ht, wt = target.size()
        offset_w, offset_h = (wt - w) // 2, (ht - h) // 2
        if offset_w > 0 and offset_h > 0:
            target = target[:, offset_h:-offset_h, offset_w:-offset_w]

        return target

    def forward(self, input, target):
        assert (
            input.dim() == 4
        ), "So far LovaszHinge is only supported for 2D data."
        n, n_classes, h, w = input.size()
        target = self.crop(w, h, target)

        return self.lovasz_hinge(logits=input, labels=target)

    def lovasz_hinge(self, logits, labels, per_image=True, ignore=None):
        """
        Binary Lovasz hinge loss
          logits: [B, H, W] Variable, logits at each pixel (between -\infty and +\infty)
          labels: [B, H, W] Tensor, binary ground truth masks (0 or 1)
          per_image: compute the loss per image instead of per batch
          ignore: void class id
        """
        if per_image:
            loss = mean(
                self.lovasz_hinge_flat(
                    *self.flatten_binary_scores(
                        log.unsqueeze(0), lab.unsqueeze(0), ignore
                    )
                )
                for log, lab in zip(logits, labels)
            )
        else:
            loss = self.lovasz_hinge_flat(
                *self.flatten_binary_scores(logits, labels, ignore)
            )
        return loss

    def lovasz_hinge_flat(self, logits, labels):
        """
        Binary Lovasz hinge loss
          logits: [P] Variable, logits at each prediction (between -\infty and +\infty)
          labels: [P] Tensor, binary ground truth labels (0 or 1)
          ignore: label to ignore
        """
        if len(labels) == 0:
            # only void pixels, the gradients should be 0
            return logits.sum() * 0.0
        signs = 2.0 * labels.float() - 1.0
        errors = 1.0 - logits * Variable(signs)
        errors_sorted, perm = torch.sort(errors, dim=0, descending=True)
        perm = perm.data
        gt_sorted = labels[perm]
        grad = lovasz_grad(gt_sorted)
        loss = torch.dot(F.relu(errors_sorted), Variable(grad))
        return loss

    def flatten_binary_scores(self, scores, labels, ignore=None):
        """
        Flattens predictions in the batch (binary case)
        Remove labels equal to 'ignore'
        """
        scores = scores.contiguous().view(-1)
        labels = labels.contiguous().view(-1)
        if ignore is None:
            return scores, labels
        valid = labels != ignore
        vscores = scores[valid]
        vlabels = labels[valid]
        return vscores, vlabels


# --------------------------- MULTICLASS LOSSES ---------------------------


class LovaszSoftmax(nn.Module):
    @save_defaults
    @load_defaults
    def __init__(self, only_present=False, per_image=False, ignore=None):
        super(LovaszSoftmax, self).__init__()
        self.only_present = only_present
        self.per_image = per_image
        self.ignore = ignore

    def crop(self, w, h, target):
        nt, ht, wt = target.size()
        offset_w, offset_h = (wt - w) // 2, (ht - h) // 2
        if offset_w > 0 and offset_h > 0:
            target = target[:, offset_h:-offset_h, offset_w:-offset_w]

        return target

    def forward(self, input, target):
        assert (
            input.dim() == 4
        ), "So far LovaszSoftmax is only supported for 2D data."
        log_p = F.softmax(input, dim=1)
        n, n_classes, h, w = input.size()
        target = self.crop(w, h, target)

        return self.lovasz_softmax(
            probas=log_p,
            labels=target,
            only_present=self.only_present,
            per_image=self.per_image,
            ignore=self.ignore,
        )

    def lovasz_softmax(
        self, probas, labels, only_present=False, per_image=False, ignore=None
    ):
        """
        Multi-class Lovasz-Softmax loss
        probas: [B, C, H, W] Variable, class probabilities at each prediction (between 0 and 1)
        labels: [B, H, W] Tensor, ground truth labels (between 0 and C - 1)
        only_present: average only on classes present in ground truth
        per_image: compute the loss per image instead of per batch
        ignore: void class labels
        """
        if per_image:
            loss = mean(
                self.lovasz_softmax_flat(
                    *self.flatten_probas(
                        prob.unsqueeze(0), lab.unsqueeze(0), ignore
                    ),
                    only_present=only_present
                )
                for prob, lab in zip(probas, labels)
            )
        else:
            loss = self.lovasz_softmax_flat(
                *self.flatten_probas(probas, labels, ignore),
                only_present=only_present
            )
        return loss

    def lovasz_softmax_flat(self, probas, labels, only_present=False):
        """
        Multi-class Lovasz-Softmax loss
        probas: [P, C] Variable, class probabilities at each prediction (between 0 and 1)
        labels: [P] Tensor, ground truth labels (between 0 and C - 1)
        only_present: average only on classes present in ground truth
        """
        if probas.numel() == 0:
            # only void pixels, the gradients should be 0
            return probas * 0.0
        C = probas.size(1)

        C = probas.size(1)
        losses = []
        for c in range(C):
            fg = (labels == c).float()  # foreground for class c
            if only_present and fg.sum() == 0:
                continue
            errors = (Variable(fg) - probas[:, c]).abs()
            errors_sorted, perm = torch.sort(errors, 0, descending=True)
            perm = perm.data
            fg_sorted = fg[perm]
            losses.append(
                torch.dot(errors_sorted, Variable(lovasz_grad(fg_sorted)))
            )
        return mean(losses)

    def flatten_probas(self, probas, labels, ignore=None):
        """
        Flattens predictions in the batch
        """
        B, C, H, W = probas.size()
        probas = (
            probas.permute(0, 2, 3, 1).contiguous().view(-1, C)
        )  # B * H * W, C = P, C
        labels = labels.contiguous().view(-1)
        if ignore is None:
            return probas, labels
        valid = labels != ignore
        vprobas = probas[valid.nonzero().squeeze()]
        vlabels = labels[valid]
        return vprobas, vlabels
