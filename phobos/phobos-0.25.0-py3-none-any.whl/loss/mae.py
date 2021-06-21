import torch.nn as nn


class MAELoss(nn.Module):
    r"""Creates a criterion that minimizes Mean Absolute Error (with mask support) between the input :math:`X` and target :math:`Y`.

    Mean Squared Error between inputs :math:`X` and :math:`Y` with mask :math:`M` is computed as:

    .. math:: MAE(X,Y) = \frac{1}{n} \sum\limits_{i}^{n} | (X_i - Y_i) \cdot M_i |

    where :math: mask `M` is binary tensor.

    reduction='mean', If args.mask=True masked version will be used.

    If args.mask=False :math:`M`=torch.ones_like(:math:`X`).

    Parameters
    ----------
    args : list
        arguments list.

    References
    ----------
    https://pytorch.org/docs/stable/generated/torch.nn.L1Loss.html

    """
    def __init__(self, args):
        """
        Inside MAELoss module

        Parameters
        ----------
        args : list
            arguments list.
        """
        super(MAELoss, self).__init__()
        if args.mask:
            self.reg_fn = self.mae_masked()
        else:
            self.reg_fn = self.mae()

    def mae(self):
        mae_loss = nn.L1Loss()

        def loss(y_pred, y_true, mask=None):
            return mae_loss(y_pred, y_true)

        return loss

    def mae_masked(self):
        mae_loss = nn.L1Loss()

        def loss(y_pred, y_true, mask=None):
            return mae_loss(y_pred * mask, y_true * mask)

        return loss

    def forward(self, predicted, target, mask=None):
        """Compute loss between :attr:`predicted` and :attr:`target`.

        :attr:`predicted` and :attr:`target` are tensors of shape :math:`[B,None]`
        if args.mask=True in __init__ :attr:`mask` tensor for shape :math:`[B,None]` will be used for loss computation.

        Parameters
        ----------
        predicted : torch.Tensor
            Predicted output tensor from a model.
        target : torch.Tensor
            Ground truth tensor.
        mask : torch.Tensor
            (Optional) Mask tensor to constrain the loss computation.

        Returns
        -------
        torch.Tensor
            Mean Absolute Error loss computed between :attr:`predicted` and :attr:`target`.
        """
        return self.reg_fn(y_pred=predicted, y_true=target, mask=mask)
