# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class FullScreenControl(Component):
    """A FullScreenControl component.
Thin wrapper of https://github.com/krvital/react-leaflet-fullscreen

Keyword arguments:
- position (a value equal to: 'topleft', 'topright', 'bottomleft', 'bottomright'; optional): Position.
- title (string; optional): Title of the button, default Full Screen.
- titleCancel (string; optional): Title of the button when fullscreen is on, default Exit Full Screen.
- forceSeparateButton (boolean; optional): Force separate button to detach from zoom buttons, default false.
- forcePseudoFullscreen (boolean; optional): Force use of pseudo full screen even if full screen API is available, default false.
- fullscreenElement (boolean; optional): Dom element to render in full screen, false by default, fallback to map._container."""
    @_explicitize_args
    def __init__(self, position=Component.UNDEFINED, title=Component.UNDEFINED, titleCancel=Component.UNDEFINED, forceSeparateButton=Component.UNDEFINED, forcePseudoFullscreen=Component.UNDEFINED, fullscreenElement=Component.UNDEFINED, **kwargs):
        self._prop_names = ['position', 'title', 'titleCancel', 'forceSeparateButton', 'forcePseudoFullscreen', 'fullscreenElement']
        self._type = 'FullScreenControl'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['position', 'title', 'titleCancel', 'forceSeparateButton', 'forcePseudoFullscreen', 'fullscreenElement']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(FullScreenControl, self).__init__(**args)
