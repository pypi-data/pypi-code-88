# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Mermaid(Component):
    """A Mermaid component.
A light wrapper of https://github.com/e-attestations/react-mermaid2.

Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The children of this component.

- id (string; optional):
    The ID used to identify this component in Dash callbacks.

- chart (string; optional):
    The mermaid code of your chart. Check Mermaid js documentation for
    details.

- className (string; optional):
    The class of the component.

- config (dict; optional):
    On optional object with one of several Mermaid config parameters.
    Check Mermaid js documentation for details.

- name (string; optional):
    On optional name of your mermaid diagram/flowchart/gantt etc."""
    @_explicitize_args
    def __init__(self, children=None, chart=Component.UNDEFINED, name=Component.UNDEFINED, config=Component.UNDEFINED, id=Component.UNDEFINED, className=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'chart', 'className', 'config', 'name']
        self._type = 'Mermaid'
        self._namespace = 'dash_extensions'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'chart', 'className', 'config', 'name']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Mermaid, self).__init__(children=children, **args)
