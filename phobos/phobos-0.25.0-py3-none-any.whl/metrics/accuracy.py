import torch


def Acc(y_pred, y_true, mask=None, thresh=0.5):
    y_pred = (y_pred >= thresh).type(torch.float32)
    if mask is None:
        res = torch.all((y_true == y_pred), dim=-1)
        res = torch.mean(res.type(torch.float32))
        return res
    else:
        res = y_true == y_pred
        res[torch.logical_not(mask.type(torch.bool))] = True
        res = torch.all(res, dim=-1)
        mask = torch.logical_not(torch.all(torch.logical_not(mask), dim=-1))
        if mask.type(torch.float32).sum() == 0:
            return torch.tensor(0.0)
        res = torch.mean(res[mask].type(torch.float32))
        return res
