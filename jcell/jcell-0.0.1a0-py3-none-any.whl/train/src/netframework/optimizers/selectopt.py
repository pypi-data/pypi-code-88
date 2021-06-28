import torch


def selectoptimizer(optimizername, net, experimentparams):
    if optimizername == "":
        optimizername = "Adam"

    if "lr" not in experimentparams:
        experimentparams["lr"] = 0.0001

    if optimizername == "Adam":
        optimizer = torch.optim.Adam(net.parameters(), **experimentparams)
    elif optimizername == "SGD":
        optimizer = torch.optim.SGD(net.parameters(), **experimentparams)
    elif optimizername == "RMSprop":
        optimizer = torch.optim.RMSprop(net.parameters(), **experimentparams)
    elif optimizername == "AdaBelief":
        try:
            from adabelief_pytorch import AdaBelief
        except Exception:
            raise ValueError(
                "AdaBelief not found. Please do a pip install adabelief-pytorch"
            )

        optimizer = AdaBelief(net.parameters(), **experimentparams)
    else:
        try:
            optline = (
                "torch.optim."
                + optimizername
                + "(net.parameters(), **experimentparams)"
            )
            optimizer = eval(optline)
        except Exception:
            raise ValueError("Optimizer {} not found".format(optimizername))

    print(optimizername)
    return optimizer
