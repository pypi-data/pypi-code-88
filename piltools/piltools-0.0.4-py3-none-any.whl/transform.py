# Third Party
from PIL import Image


def ar_resize(im, scalar):
    """
    Args:
        im (PIL.Image.Image) - Image to be recropped
        scalar (Float) - Factor by which to resize image
    Returns:
        PIL.Image.Image - Image resized with aspect ratio maintained
    """
    width, height = im.size

    return im.resize((int(width*scalar), int(height*scalar)), Image.ANTIALIAS)


def grid_crop(im, target_dimensions, v_align="center", h_align="center"):
    """
    Args:
        im (PIL.Image.Image) - Image to be recropped
        target_dimensions ((Int, Int)) - Target image width, height in pixels
        v_align (String) - Vertical focus area ["top", "center", "bottom"]
        h_align (String) - Horizontal focus area ["left", "center", "right"]
    Returns:
        PIL.Image.Image - Image resized with aspect ratio maintained
    """
    width, height = im.size
    t_width, t_height = target_dimensions

    d_width = width - t_width
    d_height = height - t_height

    # Get vertical crop points
    if v_align == "top":
        top = 0
        bottom = height - d_height
    elif v_align == "center":
        top = int(d_height/2)
        bottom = height - top
    elif v_align == "bottom":
        top = d_height
        bottom = height

    # Get horizontal crop points
    if h_align == "left":
        left = 0
        right = height - d_width
    if h_align == "center":
        left = int(d_width/2)
        right = width - left
    if h_align == "right":
        left = d_width
        right = width

    return im.crop((left, top, right, bottom))


def recrop(im, target_dimensions, v_align="center", h_align="center"):
    """
    Args:
        im (PIL.Image.Image) - Image to be recropped
        target_dimensions ((Int, Int)) - Target image width, height in pixels
        v_align (String) - Vertical focus area ["top", "center", "bottom"]
        h_align (String) - Horizontal focus area ["left", "center", "right"]
    Returns:
        PIL.Image.Image - Dynamically resized and cropped copy of image
    """
    width, height = im.size
    t_width, t_height = target_dimensions

    # Determine resize scale
    s_factor = max([t_width/width, t_height/height])

    return grid_crop(
        ar_resize(im, s_factor),
        target_dimensions,
        v_align,
        h_align
    )
