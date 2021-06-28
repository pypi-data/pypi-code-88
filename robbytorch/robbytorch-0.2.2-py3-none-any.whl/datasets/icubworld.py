import os
import os.path
import pathlib
import shutil
from typing import Callable, Dict, Optional, List, Tuple, Union

import numpy as np
import skimage.io
import torch
import torchvision.transforms
from torchvision.datasets.utils import download_and_extract_archive


class ICubWorldT(torch.utils.data.Dataset):
    """The iCubWorld Transformations (iCWT) dataset.

    See `https://robotology.github.io/iCubWorld/#icubworld-transformations-modal`.

    The dataset contains 20 * 10 * 5 * 2 * 2 = 4000 videos for each possible tuple
        (class, object, viewpoint, day, camera)
    These are:
    - 20 classes (in 4 parts):
        part1: book, cellphone, mouse, pencilcase, ringbinder
        part2: hairbrush, hairclip, perfume, sunglasses, wallet
        part3: flower, glass, mug, remote, soapdispenser
        part4: bodylotion, ovenglove, sodabottle, sprayer, squeezer
    - 10 objects per class: 1..10 (mapped to e.g. book1..book10 in the directory structure)
    - 5 viewpoint transformations: ROT2D, ROT3D, SCALE, TRANSL, MIX
    - 2 days: 0, 1 (mapped to e.g. day3, day4, depending on previous parameters)
    - 2 cameras, simultaneously recording: left, right
    Each of the 4000 tuples (class, object, transform, day, camera) defines a video.
    Each video is 20s (or 40s for MIX) of ~10fps film, for a total of ~100-500 frames per video.
    Each frame is 640x480 in the full version and 256x256 in the cropped version of the dataset.

    This dataset provides clips from these videos (tensors consisting of `clip_length` frames),
    or individual frames. By default all possible clips of `clip_length` consecutive frames
    are returned.

    Remarks:
        Some frames files were cropped smaller than 256x256, we pad them centrally with black.
        Some frames (<1%?) do not contain the object at all in their view.
        Note left/right videos in the same acquisition do not always have the same number of frames.
        This implementation does not allow getting aligned left/right frames from the two cameras.
        You'd have to read that from `img_info_LR.txt` in each `day` folder, as cameras seem to drop
        frames independently, and neither the file's name nor ordinal index inside each folder
        allows to recover an exact alignment.

    Args:
        root: Root directory where directory "icubworld" exists or will be created. E.g. you can
            download and extract the parts you need to `{root}/icubworld/part1_cropped/`.

        classes: List of class names to be used. This also becomes the index-to-label map
            (clips will be labelled with the index of their class in this list).
        objects: Object ids to be used, a subset of 1..10
        viewpoints: Transformations to be used, in `["ROT2D", "ROT3D", "SCALE", "TRANSL", "MIX"]`
        days: Days to be used, a subset of `[0, 1]`
        cameras: Cameras to be used, a subset of `["left", "right"]`

        clip_length: Length of every clip in frames. Ignored if `return_images` is true.
        clip_stride: Distance between first frames of consecutive clips. In other words,
            only clips whose first frame's index is divisible by `clip_stride` are used.
        clip_offset: Changes the behaviour of `clip_stride` so that only clips whose first
            frame's index is congruent to `clip_offset` mod `min(clip_stride, len(video))` are used.
            If None, randomly select an offset once at `__init__`, independently for each video.
        clip_dilation: Distance between consecutive frames taken into a clip.
        random_clip_per_video: If true, return only one random clip per video per epoch.
        return_images: If true, yield individual frames, without the time dimension.
            Overrides `clip_length=1`.
        cropped: If true, use the pre-cropped version of the dataset (256x256).

        transform: If given, takes a single ndarray frame and returns a transformed torch tensor.
            Default: `torchvision.transforms.ToTensor`, returns 3xHxW tensors in range 0.0..1.0.
            (Frames before `transform` are ndarrays of shape HxWx3, dtype=uint8, 0..255 RGB.)
        download: If true, downloads the missing, needed parts of the dataset from the internet and
            puts it in root directory. Each part of the full / cropped dataset is ~7GiB / ~2GiB.
    """
    PART1 = ["book", "cellphone", "mouse", "pencilcase", "ringbinder"]
    PART2 = ["hairbrush", "hairclip", "perfume", "sunglasses", "wallet"]
    PART3 = ["flower", "glass", "mug", "remote", "soapdispenser"]
    PART4 = ["bodylotion", "ovenglove", "sodabottle", "sprayer", "squeezer"]
    ALL_CLASSES = PART1 + PART2 + PART3 + PART4
    ALL_OBJECTS = list(range(1, 11))
    ALL_VIEWPOINTS = ["MIX", "ROT2D", "ROT3D", "SCALE", "TRANSL"]
    ALL_DAYS = [0, 1]
    ALL_CAMERAS = ["left", "right"]

    BASE_DIR = "icubworld"
    BASE_URL = "https://zenodo.org/record/835510/files/"
    _TGZ_MD5 = {
        "part1": "8b336a82c06df7d31ad2f33a38cbb5e0",
        "part2": "542977f7c7b67e7bd4eadaeb2e786a98",
        "part3": "eac3b7490098b08bb88efddd00fa67dd",
        "part4": "3f4d5bea79696722b8864750463bbbe8",
        "part1_cropped": "cf3dfe327c8bb1c447e918cec4f765e7",
        "part2_cropped": "4ed99dd72a3072d5252d5575c93e96c9",
        "part3_cropped": "0ebbc95ab39606d46a536f47e1d32dd7",
        "part4_cropped": "2a529bb60c06035175039925fa39b2aa"
    }

    def __init__(self,
                 root: Union[str, os.PathLike],
                 classes: List[str] = ALL_CLASSES,
                 objects: List[int] = ALL_OBJECTS,
                 viewpoints: List[str] = ALL_VIEWPOINTS,
                 days: List[int] = ALL_DAYS,
                 cameras: List[str] = ALL_CAMERAS,
                 clip_length: int = 8,
                 clip_stride: int = 1,
                 clip_offset: Optional[int] = 0,
                 clip_dilation: int = 1,
                 random_clip_per_video: bool = False,
                 return_images: bool = False,
                 cropped: bool = True,
                 transform: Optional[Callable[[np.ndarray], torch.Tensor]] = None,
                 clip_transform: Optional[Callable[[torch.Tensor], torch.Tensor]] = None,
                 download: bool = False):
        self.root = pathlib.Path(root).expanduser()

        self.classes = list(classes)
        self.objects = list(objects)
        self.viewpoints = list(viewpoints)
        self.days = list(days)
        self.cameras = list(cameras)

        self.clip_length = 1 if return_images else clip_length
        self.clip_stride = clip_stride
        self.clip_offset = clip_offset
        self.clip_dilation = clip_dilation
        self.return_images = return_images
        self.random_clip_per_video = random_clip_per_video
        self.cropped = cropped

        self.transform = transform
        self.clip_transform = clip_transform

        # A dictionary mapping a video_name to a list of frame names, e.g.
        #   `part1_cropped/book/book1/ROT2D/day6/left -> ['00005481.jpg', '00005482.jpg', ...]`
        # (a video_name is represented as PurePath, relative to BASE_DIR).
        self.videos: Dict[pathlib.PurePath, List[str]] = {}
        # A dictionary mapping a video_name to a list of indices of frames that can be used as
        # first frames of clips (as specified by `clip_stride`, `clip_offset`).
        self.first_frame_indices: Dict[pathlib.PurePath, List[int]] = {}
        # A list of all clips, as (video_name, first frame index) tuples.
        # If `random_clip_per_video` is True, this only lists video_name-s instead (the int is 0).
        self.clips: List[Tuple[pathlib.PurePath, int]] = []

        # Check arguments.
        for name, stuff, all_stuff in [
                ("classes", self.classes, self.ALL_CLASSES),
                ("objects", self.objects, self.ALL_OBJECTS),
                ("viewpoints", self.viewpoints, self.ALL_VIEWPOINTS),
                ("days", self.days, self.ALL_DAYS),
                ("cameras", self.cameras, self.ALL_CAMERAS)]:
            if not set(stuff) <= set(all_stuff):  # type: ignore
                raise ValueError(f"{name} should be a subset of {all_stuff}, got {stuff}.")
            if len(set(stuff)) < len(stuff):  # type: ignore
                raise ValueError(f"{name} should not contain duplicates, got {stuff}.")
        if min(self.clip_length, self.clip_stride, self.clip_dilation) < 1:
            raise ValueError("clip length, stride, duration should be >=1.")
        self.check_or_download(download)

        # Compute self.videos and self.clips.
        for c in self.classes:
            part = 'part' + str((self.ALL_CLASSES.index(c) // 5) + 1)
            if self.cropped:
                part += '_cropped'
            for o in self.objects:
                for v in self.viewpoints:
                    path = pathlib.PurePath(part, c, (c + str(o)), v)
                    dir = self.root / self.BASE_DIR / path
                    day_pair = [d_path.name for d_path in dir.glob("day*")]
                    assert len(day_pair) == 2, f"Dataset corrupt: {path}"
                    for d in self.days:
                        for cam in self.cameras:
                            self.add_video(path / day_pair[d] / cam)

    def add_video(self, video_name: pathlib.PurePath):
        """Add a video folder and its clips to the dataset.

        Args:
            video_name: a pure path of the form
                `part / class / object / viewpoint / day / camera`
                e.g. `part1_cropped/book/book1/ROT2D/day6/left`
        """
        dir = self.root / self.BASE_DIR / video_name
        video = sorted(p.name for p in dir.glob("*.jpg") if not p.name.startswith('.'))
        assert len(video) in range(100, 500), f"Dataset corrupt: {video_name} {len(video)}"
        self.videos[video_name] = video

        # Compute `first_frame_indices`.
        clip_span = (self.clip_length - 1) * self.clip_dilation + 1
        maximum = len(video) - clip_span  # last possible first-frame-index
        stride = min(self.clip_stride, maximum + 1)
        if self.clip_offset is not None:
            minimum = self.clip_offset % stride
        else:
            minimum = int(torch.randint(0, stride, (1,)).item())
        lst = list(range(minimum, maximum + 1, stride))
        assert lst, f"No clips got selected from a video of length {len(video)}."
        self.first_frame_indices[video_name] = lst

        if self.random_clip_per_video:
            self.clips.append((video_name, 0))
        else:
            for first_frame_index in self.first_frame_indices[video_name]:
                self.clips.append((video_name, first_frame_index))

    def __getitem__(self, key: int) -> Tuple[torch.Tensor, int]:
        """Return a `(clip, class_id)` dataitem for a given integer key.

        `class_id` is the class index in `self.classes`.
        `clip` is a torch tensor of shape `clip_length` x 3 x H x W, or just 3xHxW
            if `self.return_images` is True (assuming `transform` calls `ToTensor`).
        """
        video_name, first_frame_index = self.clips[key]
        class_id = self.classes.index(video_name.parts[1])
        video = self.videos[video_name]
        dir = self.root / self.BASE_DIR / video_name
        if self.random_clip_per_video:
            first_frame_index = self._get_random_first_frame(video_name)

        clip: List[torch.Tensor] = []
        for i in range(self.clip_length):
            frame_id = first_frame_index + i * self.clip_dilation
            frame_name = video[frame_id]
            frame_ndarray = self._pad(skimage.io.imread(dir / frame_name))
            if self.transform:
                frame_tensor = self.transform(frame_ndarray)
            else:
                frame_tensor = torchvision.transforms.ToTensor()(frame_ndarray)
            clip.append(frame_tensor)

        if self.return_images:
            return clip[0], class_id
        else:
            clip = torch.stack(clip)
            if self.clip_transform:
                clip = self.clip_transform(clip)
            return clip, class_id

    def __len__(self) -> int:
        return len(self.clips)

    def _pad(self, image: np.ndarray) -> np.ndarray:
        """Pad an image centrally with black pixels to 256x256 or 640x480."""
        proper_shape = (256, 256, 3) if self.cropped else (640, 480, 3)
        if image.shape == proper_shape:
            return image
        h_diff = proper_shape[0] - image.shape[0]
        w_diff = proper_shape[1] - image.shape[1]
        def halve(x): return (x // 2, (x + 1) // 2)
        pad = (halve(h_diff), halve(w_diff), (0, 0))
        return np.pad(image, pad)

    def _get_random_first_frame(self, video_name: pathlib.PurePath):
        lst = self.first_frame_indices[video_name]
        i = int(torch.randint(0, len(lst), (1,)).item())
        return lst[i]

    def check_or_download(self, download: bool) -> None:
        parts = sorted(set(str((self.ALL_CLASSES.index(c) // 5) + 1) for c in self.classes))
        parts = ["part" + p for p in parts]
        if self.cropped:
            parts = [p + "_cropped" for p in parts]
        part_size = 2 if self.cropped else 7  # rough size of each part, decompressed, in GiB

        if not self.root.is_dir():
            raise FileNotFoundError(f"root directory {self.root} should exist.")
        base_dir = self.root / self.BASE_DIR
        missing_parts = [p for p in parts if not (base_dir / p).is_dir()]
        if missing_parts:
            free_space = shutil.disk_usage(self.root).free / 1024 ** 3  # GiB
            if not download:
                if not base_dir.is_dir():
                    error = "Dataset not found. "
                    error += f"Root directory {self.root} should contain '{self.BASE_DIR}' dir. "
                else:
                    error = "Dataset incomplete. "
                    error += f"Directory {base_dir} should contain {', '.join(missing_parts)}. "
                error += f"You can use download=True, takes ~{part_size} GiB per part. "
                error += f"(You have {free_space:.1f} GiB free space.)"
                raise FileNotFoundError(error)
            else:
                base_dir.mkdir(exist_ok=True)
                size_needed = len(missing_parts) * part_size  # GiB
                print(f"Downloading ~{size_needed} GiB: {', '.join(missing_parts)}.")
                print(f"(You have {free_space:.1f} GiB free space).")
                if size_needed + part_size >= free_space:
                    raise RuntimeError("Not enough space to download and unpack the parts.")
                for part in missing_parts:
                    url = self.BASE_URL + part + ".tar.gz"
                    # `download_and_extract_archive` prints too, but sometimes after a huge delay
                    # (does it download the archive to memory by mistake when resolving redirects?)
                    print(f"Downloading {part}...", flush=True)
                    download_and_extract_archive(url, base_dir, md5=self._TGZ_MD5[part],
                                                 remove_finished=True)
                missing_parts = [p for p in parts if not (base_dir / p).is_dir()]
                if missing_parts:
                    RuntimeError(f"Download/extract failed, missing: {', '.join(missing_parts)}")
                else:
                    print("Download and extract successful.")
