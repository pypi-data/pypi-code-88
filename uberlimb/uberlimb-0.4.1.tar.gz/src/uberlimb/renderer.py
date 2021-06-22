import numpy as np
from PIL import Image
from skimage.filters import gaussian
from skimage.transform import resize

from uberlimb.frame import LimbFrame
from uberlimb.input_space import InputSpace
from uberlimb.model.model import LimbModel
from uberlimb.parameters import RendererParams, FrameColorMap


class Renderer:
    def __init__(self,
                 params: RendererParams,
                 mask: np.ndarray = None):
        self.params = params
        self.model = LimbModel.build_model(self.params.model)
        self._mask = mask
        self.input_space = InputSpace(self.params.input,
                                      self._mask)

    def load_mask_from_raster_image(self,
                                    mask_img: Image):
        # TODO: handle AA
        mask_img = (mask_img
                    .convert('L')
                    .resize((self.input_space.arr_y_resolution,
                             self.input_space.arr_x_resolution)))
        mask_arr = np.array(mask_img, dtype=np.float32)
        mask_arr = gaussian(mask_arr, sigma=7)
        mask_noise = 1 + np.random.random(mask_arr.shape) * 0.02
        mask_arr *= mask_noise
        self._mask = mask_arr
        self.update_input_space()

    def update_model(self):
        self.model = LimbModel.build_model(self.params.model)

    def update_input_space(self):
        self.input_space = InputSpace(self.params.input,
                                      self._mask)

    def render_frame(self) -> LimbFrame:
        # TODO set batch size based on params count
        arr = self.model.predict(self.input_space.arr,
                                 batch_size=int(2 ** 17),
                                 verbose=0)
        arr = arr.reshape(self.input_space.arr_y_resolution,
                          self.input_space.arr_x_resolution,
                          3)
        arr = resize(arr,
                     (self.params.input.y_resolution,
                      self.params.input.x_resolution,))
        frame = LimbFrame(arr)
        if self.params.post_fx.color_map == FrameColorMap.BINNING:
            frame.postprocess_binning(self.params.post_fx.dither_strength)
        elif self.params.post_fx.color_map == FrameColorMap.NORMED:
            frame.postprocess_normed(self.params.post_fx.dither_strength)
        return frame
