import torch
import torch.nn as nn
import torch.nn.functional as F

from netframework import save_defaults, load_defaults


class WeightedAccuracy(nn.Module):
    @save_defaults
    @load_defaults
    def __init__(self, class_id=None):
        super(WeightedAccuracy, self).__init__()
        self.cid = class_id

    def forward(self, input, target):
        with torch.no_grad():
            c = input.size(1)
            target = target.detach().view(-1).float()

            prob = F.softmax(input, dim=1)
            prob = prob.detach()
            _, maxprob = torch.max(prob, 1)
            maxprob = maxprob.view(-1).float()

            if self.cid is not None:
                classes = [self.cid]
            else:
                classes = list(range(c))
            correct = 0
            for cl in classes:
                n_i = target.eq(cl).sum(0).float()
                acc = (
                    ((maxprob.eq(cl).float() + target.eq(cl).float()).eq(2))
                    .sum(0)
                    .float()
                )
                correct += torch.where(
                    n_i > 0, acc / n_i, torch.ones((1,)).to(input.device)
                )

            correct = correct / len(classes)
            res = correct.mul_(100.0)

        return res


class FMeasure(nn.Module):
    @save_defaults
    @load_defaults
    def __init__(self, class_id=None):
        super(FMeasure, self).__init__()
        self.cid = class_id

    def forward(self, input, target):
        with torch.no_grad():
            c = input.size(1)
            target = target.detach().view(-1).float()

            prob = F.softmax(input, dim=1)
            prob = prob.detach()
            _, maxprob = torch.max(prob, 1)
            maxprob = maxprob.view(-1).float()

            if self.cid is not None:
                classes = [self.cid]
            else:
                classes = list(range(c))

            correct = 0
            for cl in range(c):
                TP = (
                    (maxprob.eq(cl).float() + target.eq(cl).float()).eq(2)
                ).sum(0)
                FP = (
                    (maxprob.eq(cl).float() + target.ne(cl).float()).eq(2)
                ).sum(0)
                FN = (
                    (maxprob.ne(cl).float() + target.eq(cl).float()).eq(2)
                ).sum(0)
                p = torch.where(
                    (TP + FP) > 0,
                    TP / (TP + FP),
                    torch.zeros((1,)).to(TP.device),
                )
                r = torch.where(
                    (TP + FN) > 0,
                    TP / (TP + FN),
                    torch.zeros((1,)).to(TP.device),
                )
                correct += torch.where(
                    (p + r) > 0,
                    (2 * p * r) / (p + r),
                    torch.zeros((1,)).to(input.device),
                )

            correct = correct / len(classes)

        return correct


class Jaccard(nn.Module):
    def __init__(self):
        super(Jaccard, self).__init__()

    def jaccard(self, x, y):
        z = x.eq(1).float() + y.eq(1).float()
        intersection = (z.eq(2).float()).sum()
        union = (z.ge(1).float()).sum()

        iou = torch.where(
            union > 0,
            intersection / union,
            torch.where(
                intersection > 0,
                torch.zeros((1,)).to(x.device),
                torch.zeros((1,)).to(x.device),
            ),
        )
        return iou

    def forward(self, input, target):
        with torch.no_grad():
            prob = F.softmax(input, dim=1)
            prob = prob.detach()
            _, maxprob = torch.max(prob, 1)
            target = (target == 1).float()
            maxprob = (maxprob == 1).float()

            iou = self.jaccard(target, maxprob)

        return iou
