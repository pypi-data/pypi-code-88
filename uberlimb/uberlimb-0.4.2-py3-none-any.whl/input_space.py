import numpy as np

from uberlimb.parameters import InputSpaceParams


class InputSpace:
    def __init__(self,
                 params: InputSpaceParams,
                 mask: np.ndarray = None):
        self.arr_x_resolution = round(params.x_resolution * params.resolution_factor)
        self.arr_y_resolution = round(params.y_resolution * params.resolution_factor)
        self.arr = self._create_input_array(params, mask)

    def _create_input_array(self,
                            params: InputSpaceParams,
                            mask: np.ndarray = None) -> np.ndarray:
        SIZE_CONSTANT = 1920

        # basic init
        # we use `params.x_resolution` to determine the "coordinates" of the image
        # if we'll use `self.arr_x_resolution` instead, `params.resolution_factor`
        # will start zooming in/out when applied
        x = params.x_resolution * params.scale / SIZE_CONSTANT
        x = np.linspace(-x, x, self.arr_x_resolution)
        y = params.y_resolution * params.scale / SIZE_CONSTANT
        y = np.linspace(-y, y, self.arr_y_resolution)

        # offset
        if params.offset_x:
            x_offset = x.ptp() * params.offset_x / x.size
            x += x_offset
        if params.offset_y:
            y_offset = y.ptp() * params.offset_y / y.size
            y += y_offset

        x, y = np.meshgrid(x, y)

        # rotation
        if params.rotation:
            rot = params.rotation * np.pi / 180
            x_rot = np.cos(rot) * x + np.sin(rot) * y
            y_rot = np.cos(rot + np.pi / 2) * x + np.sin(rot + np.pi / 2) * y
            x, y = x_rot, y_rot

        x = x.reshape(-1, 1)
        y = y.reshape(-1, 1)

        # custom function
        if params.custom_fuction:
            f = eval(params.custom_fuction)
        else:
            f = np.sqrt(x ** 2 + y ** 2)

        alpha = np.full((x.size, 1), params.alpha)
        beta = np.full((x.size, 1), params.beta)

        # mask
        if mask is not None:
            z = (mask / mask.max()).reshape(-1, 1) * 2 - 1
        else:
            z = np.full((x.size, 1), 0)
        input_space = x, y, z, alpha, beta, f
        input_space = np.concatenate(np.array(input_space), axis=1)
        return input_space
