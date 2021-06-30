# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class LoadingControl(Component):
    """A LoadingControl component.
LoadingControl is based on https://github.com/ebrelsford/Leaflet.loading

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children of this component (dynamic).
- position (a value equal to: "topleft", "topright", "bottomleft", "bottomright"; optional): The position of this component.
- separate (boolean; default False): Whether the control should be separate from the zoom control or not, defaults to false.
- delayIndicator (number; optional): The number of milliseconds to wait before showing the loading indicator. Defaults to null (no delay).
- spinjs (boolean; default False): Enable the use of spin.js (optional).
- spin (dict; default {
    lines: 7,
    length: 3,
    width: 3,
    radius: 5,
    rotate: 13,
    top: "83%"
}): A spin.js options object (optional).
- className (string; optional): A custom class name to assign to the image. Empty by default.
- id (string; optional): The ID used to identify this component in Dash callbacks."""
    @_explicitize_args
    def __init__(self, children=None, position=Component.UNDEFINED, separate=Component.UNDEFINED, delayIndicator=Component.UNDEFINED, spinjs=Component.UNDEFINED, spin=Component.UNDEFINED, className=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'position', 'separate', 'delayIndicator', 'spinjs', 'spin', 'className', 'id']
        self._type = 'LoadingControl'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'position', 'separate', 'delayIndicator', 'spinjs', 'spin', 'className', 'id']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(LoadingControl, self).__init__(children=children, **args)
