# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class VectorGrid(Component):
    """A VectorGrid component.
VectorGrid is a wrapper of https://github.com/mhasbie/react-leaflet-vectorgrid

Keyword arguments:
- children (a list of or a singular dash component, string or number; optional): Children
- data (dict; optional): Required when using type slicer. A valid GeoJSON FeatureCollection object.
- type (a value equal to: "slicer", "protobuf"; default 'slicer'): Decides between using VectorGrid.Slicer and VectorGrid.Protobuf. Available options: slicer, protobuf.
- idField (string; optional): A unique identifier field in the vector feature.
- tooltip (string; optional): Property to display as tooltip.
- style (dict; optional): Apply default style to all vector features. Use this props when not using vectorTileLayerStyles
- hoverStyle (dict; optional): Style to apply to features on mouseover event.
- activeStyle (dict; optional): Style to apply to features on click event. Can be use to show user selection when feature is clicked.
Double click to clear selection.
- zIndex (number; optional): Sets the VectorGrid z-index.
- interactive (boolean; optional): Whether VectorGrid fires Interactive Layer events.
- url (string; optional): Required when using type protobuf. Pass a url template that points to vector tiles (usually .pbf or .mvt).
- subdomains (string; default ''): Akin to the subdomains option to L.TileLayer.
- accessKey (string; optional): Tile server access key.
- accessToken (string; optional): Tile server access token.
- vectorTileLayerStyles (dict; optional): A data structure holding initial symbolizer definitions for the vector features. Refer to
[Leaflet.VectorGrid doc](https://github.com/Leaflet/Leaflet.VectorGrid) for more info.
- id (string; optional): The ID used to identify this component in Dash callbacks"""
    @_explicitize_args
    def __init__(self, children=None, data=Component.UNDEFINED, type=Component.UNDEFINED, idField=Component.UNDEFINED, tooltip=Component.UNDEFINED, style=Component.UNDEFINED, hoverStyle=Component.UNDEFINED, activeStyle=Component.UNDEFINED, zIndex=Component.UNDEFINED, interactive=Component.UNDEFINED, url=Component.UNDEFINED, subdomains=Component.UNDEFINED, accessKey=Component.UNDEFINED, accessToken=Component.UNDEFINED, vectorTileLayerStyles=Component.UNDEFINED, id=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'data', 'type', 'idField', 'tooltip', 'style', 'hoverStyle', 'activeStyle', 'zIndex', 'interactive', 'url', 'subdomains', 'accessKey', 'accessToken', 'vectorTileLayerStyles', 'id']
        self._type = 'VectorGrid'
        self._namespace = 'dash_leaflet'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'data', 'type', 'idField', 'tooltip', 'style', 'hoverStyle', 'activeStyle', 'zIndex', 'interactive', 'url', 'subdomains', 'accessKey', 'accessToken', 'vectorTileLayerStyles', 'id']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(VectorGrid, self).__init__(children=children, **args)
