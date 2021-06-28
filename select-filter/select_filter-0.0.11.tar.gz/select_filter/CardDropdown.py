# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class CardDropdown(Component):
    """A CardDropdown component.
ExampleComponent is an example component.
It takes a property, `label`, and
displays it.
It renders an input with the property `value`
which is editable by the user.

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): The children components displayed inside the grid.
- id (string; optional): The ID used to identify this component in Dash callbacks.
- label (string; optional): A label that will be printed when this component is rendered.
- value (boolean | number | string | dict | list; optional): The value displayed in the input.
- classes (dict; optional): The classes displayed in the component."""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, label=Component.UNDEFINED, value=Component.UNDEFINED, classes=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'label', 'value', 'classes']
        self._type = 'CardDropdown'
        self._namespace = 'select_filter'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'label', 'value', 'classes']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(CardDropdown, self).__init__(children=children, **args)
