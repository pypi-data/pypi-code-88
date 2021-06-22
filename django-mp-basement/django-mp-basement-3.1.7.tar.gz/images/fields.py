
from basement.fields import FormField

from images.widgets import ImagesFormFieldWidget
from images.forms import build_images_form_class


class ImagesFormField(FormField):

    widget = ImagesFormFieldWidget

    def __init__(self, image_model):
        self._image_model = image_model
        super().__init__()

    def _build_form(self, *args, **kwargs):

        form_class = build_images_form_class(self._image_model)

        return form_class(*args, **kwargs)
