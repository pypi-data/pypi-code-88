import torch

try:
    from ..netframework.netutil.NetFramework import NetFramework
    from ..netframework.dataloaders.imageutl import saveimage
    from ..netframework import save_defaults, load_defaults
except Exception:
    from netframework.netutil.NetFramework import NetFramework
    from netframework.dataloaders.imageutl import saveimage
    from netframework import save_defaults, load_defaults

import torch.nn.functional as F
import os


class SegmentNet(NetFramework):
    def __init__(self, default_path, parser=None, custom_folder=None):
        NetFramework.__init__(self, default_path, parser, custom_folder)

    @save_defaults
    @load_defaults
    def valid_visualization(self, current_epoch, index=0, save=False):
        with torch.no_grad():
            sample = self.testdataset[index]
            sample["image"].unsqueeze_(0)
            sample["label"].unsqueeze_(0)

            sample = self.warp_var_mod.warp_Variable(sample, self.device)
            images = sample["image"]
            labels = sample["label"]

            outputs = self.net(images)
            prob = F.softmax(outputs, dim=1)
            prob = prob.detach()[0]
            _, maxprob = torch.max(prob, 0)

            if maxprob.ndim == 3:
                z = maxprob.shape[0] // 2
                maxprob = maxprob[z, ...]
                prob = prob[:, z, ...]
                labels = labels[0, z, ...]
                images = images[0, 0, z, ...]
            else:
                labels = labels[0, ...]
                images = images[0, ...]

            scale = 1.0
            if max(maxprob.shape) > 512:
                scale = 512.0 / max(maxprob.shape)

            if self.visdom:
                self.visheatmap.show(
                    "Segmentation",
                    maxprob.cpu().numpy(),
                    colormap="Jet",
                    scale=scale,
                )

                for c in range(prob.shape[0]):
                    self.visheatmap.show(
                        "Prob Map " + str(c),
                        prob.cpu()[c].numpy(),
                        colormap="Jet",
                        scale=scale,
                    )

                self.visheatmap.show(
                    "Annotation",
                    labels.detach().cpu().numpy(),
                    colormap="Jet",
                    scale=scale,
                )

                self.visheatmap.show(
                    "Image",
                    images.detach().cpu().numpy(),
                    colormap="Greys",
                    scale=scale,
                )

            if (self.saveim_rate != 0) and (
                ((current_epoch) % self.saveim_rate) == 0
            ):
                saveimage(
                    prob.cpu().numpy(),
                    os.path.join(
                        self.folders["images_path"],
                        "image-{:d}-{:03d}.tif".format(index, current_epoch),
                    ),
                )

        return 1
