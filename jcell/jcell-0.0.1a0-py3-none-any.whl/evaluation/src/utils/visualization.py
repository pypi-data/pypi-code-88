import warnings
import numpy as np
from tqdm import tqdm
from skimage.color import label2rgb
from skimage.segmentation import find_boundaries

from . import get_colors

colors = get_colors()


# Visualization
def visualization2D(seg, output_type, original_image=None, verbose=False):
    if verbose:
        print("Constructing visualizations")

    boundary = find_boundaries(seg, mode="thick").astype(np.uint8)

    seg_rgb = label2rgb(seg, bg_label=0, colors=colors)
    image_overlay = np.zeros_like(seg_rgb)
    boundary_overlay = np.zeros_like(seg_rgb)

    if (
        original_image is not None
        and original_image.ndim == 3
        and original_image.shape[2] == 1
    ):
        original_image = original_image[:, :, 0]

    if original_image is not None:
        if ("object_overlay" in output_type) or ("all" in output_type):
            image_overlay = label2rgb(
                seg,
                original_image,
                bg_label=0,
                colors=colors,
            )
            image_overlay[boundary == 1] = (0, 1, 0)

        if ("bound_overlay" in output_type) or ("all" in output_type):
            boundary_overlay = label2rgb(
                boundary,
                original_image,
                bg_label=0,
                colors=["red"],
            )
    elif (
        ("bound_overlay" in output_type)
        or ("object_overlay" in output_type)
        or ("all" in output_type)
    ):
        warnings.warn(
            "WARNING: invalid bound_overlay and/or object_overlay because the input image was not provided."
        )

    return image_overlay, boundary_overlay, boundary, seg_rgb


def visualization3D(seg, output_type, original_image=None, verbose=False):
    if verbose:
        print("Constructing visualizations")

    boundary = find_boundaries(seg, mode="thick").astype(np.uint8)

    seg_rgb = np.zeros((seg.shape[0], seg.shape[1], 3, seg.shape[2]))
    image_overlay = np.zeros((seg.shape[0], seg.shape[1], 3, seg.shape[2]))
    boundary_overlay = np.zeros((seg.shape[0], seg.shape[1], 3, seg.shape[2]))

    pbar3 = tqdm(
        total=seg.shape[-1],
        desc="Preparing output files -",
        position=2,
        leave=False,
    )

    for channel in range(seg.shape[-1]):
        ch_colors = [
            colors[c] for c in list(np.unique(seg[..., channel])) if c != 0
        ]
        seg_rgb[..., channel] = label2rgb(
            seg[..., channel], bg_label=0, colors=ch_colors
        )

        if original_image is not None:
            if (
                original_image[..., channel].ndim == 3
                and original_image.shape[2] == 1
            ):
                sliced_image = original_image[:, :, 0, channel]
            else:
                sliced_image = original_image[..., channel]

        if original_image is not None:
            if ("object_overlay" in output_type) or ("all" in output_type):
                image_overlay[..., channel] = label2rgb(
                    seg[..., channel],
                    sliced_image,
                    bg_label=0,
                    colors=ch_colors,
                )
                temp_image_overlay = image_overlay[..., channel]
                temp_image_overlay[boundary[..., channel] == 1] = (0, 1, 0)
                image_overlay[..., channel] = temp_image_overlay

            if ("bound_overlay" in output_type) or ("all" in output_type):
                boundary_overlay[..., channel] = label2rgb(
                    boundary[..., channel],
                    sliced_image,
                    bg_label=0,
                    colors=["red"],
                )
        elif (
            ("bound_overlay" in output_type)
            or ("object_overlay" in output_type)
            or ("all" in output_type)
        ):
            warnings.warn(
                "WARNING: invalid bound_overlay and/or object_overlay because the input image was not provided."
            )
        pbar3.update()
    pbar3.close()

    return image_overlay, boundary_overlay, boundary, seg_rgb
