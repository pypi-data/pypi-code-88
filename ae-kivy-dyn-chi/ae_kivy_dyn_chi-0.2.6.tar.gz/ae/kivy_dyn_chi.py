"""
dynamic children mix-in for kivy container widgets
==================================================

This ae portion is providing the mixin class :class:`DynamicChildrenBehavior` for to add children widgets dynamically
and data-driven to your kivy container widgets (like DropDowns, Popups or any layout widgets).
"""
from typing import Any, Callable, Dict, List

from kivy.factory import Factory                                                            # type: ignore
# pylint: disable=no-name-in-module
from kivy.properties import ListProperty                                                    # type: ignore # noqa: E0611
from kivy.uix.popup import Popup                                                            # type: ignore
from kivy.uix.widget import Widget                                                          # type: ignore

from ae.base import UNSET                                                                   # type: ignore
from ae.deep import deep_object, deep_replace                                               # type: ignore


__version__ = '0.2.6'


class DynamicChildrenBehavior:
    """ mixin class for the dynamic creation/refresh of child widgets from a data map.

    At least one of the classes that is mixing in this class has to inherit from Widget (or EventDispatcher) to get the
    :attr:`~DynamicChildrenBehavior.child_data_maps` attribute correctly initialized and firing on change.
    """
    child_data_maps: List[Dict[str, Any]] = ListProperty()
    """ list of child data dicts for to instantiate the children of the inheriting layout/widget.

    Each child data dict is defining its own widget with the following keys:

    * `cls`: either the class name or the class/type object of the widget to be created dynamically.
    * `kwargs`: dict of keyword arguments that will be passed to the constructor method of the widget.
      All values in this dict with the magic string `'replace_with_data_map_container'` will be
      replaced with the instance of the container before it gets passed to the `__init__` method
      of the child (see :func:`~ae.deep.deep_replace`).
    * `attributes`: dict of attributes where the key is specifying the attribute name/path and the
      value the finally assigned attribute value.
      The attribute name (the key of this dict) can be a deep/combined attribute/index path
      which allows to update deeper objects within the child object (via :func:`~ae.deep.deep_object`).
      All values in this dict with the magic string `'replace_with_data_map_container'` will be
      replaced with the instance of the container before the child attributes get updated.
      All values in this dict with the magic string `'replace_with_data_map_child'` will be
      replaced with the instance of the child before they get applied to it (via :func:`~ae.deep.deep_replace`).

    :attr:`child_data_maps` is a :class:`~kivy.properties.ListProperty` and
    defaults to an empty list.
    """

    bind: Callable
    container: Widget
    _container: Widget

    def __init__(self, **kwargs):
        """ add dynamic creation and refresh of children to this layout (Popup/Dropdown/...) widget. """
        super().__init__(**kwargs)
        self._is_popup = isinstance(self, Popup)    # True if inherits from :class:`~kivy.uix.popup.Popup`
        self._map_children = list()
        self.bind(child_data_maps=self.refresh_child_data_widgets)
        self.refresh_child_data_widgets(self, **kwargs)

    def refresh_child_data_widgets(self, *_args, **init_kwargs):
        """ recreate dynamic children of the passed widget.

        :param _args:           not needed extra args (only passed if this function get called as event handler).
        :param init_kwargs:     container kwargs (passed from :meth:`~DynamicChildrenBehavior.__init__` method).
        """
        if self._is_popup:
            children_container = init_kwargs.get('content', self._container)   # self._container is self.ids.container
        else:
            children_container = init_kwargs.get('container', getattr(self, 'container', self))
        if not hasattr(super(), 'container'):
            self.container = children_container

        for child in self._map_children:
            children_container.remove_widget(child)
        self._map_children.clear()

        for child_index, child_data in enumerate(self.child_data_maps):
            cls = child_data.get('cls', 'FlowButton')
            if isinstance(cls, str):
                cls = Factory.get(cls)

            init_child_kwargs = child_data.get('kwargs', dict())
            deep_replace(init_child_kwargs, lambda p, k, v: self if v == 'replace_with_data_map_container' else UNSET)
            child = cls(**init_child_kwargs)

            child.child_index = child_index

            attributes = child_data.get('attributes', dict())
            deep_replace(attributes, lambda p, k, v: self if v == 'replace_with_data_map_container' else UNSET)
            deep_replace(attributes, lambda p, k, v: child if v == 'replace_with_data_map_child' else UNSET)
            for attr_name, attr_value in attributes.items():
                # setattr(child, attr_name, attr_value) does not support composed/deep keys/attributes
                deep_object(child, attr_name, new_value=attr_value)

            children_container.add_widget(child)
            self._map_children.append(child)


Factory.register('DynamicChildrenBehavior', cls=DynamicChildrenBehavior)
