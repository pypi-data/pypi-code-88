"""
main app base class with context help for flow and app state changes
====================================================================

The class :class:`HelpAppBase` provided by this namespace portion is extending your application with a context-sensitive
help functionality.

The data-driven approach allows to add, edit and remove help texts without the need to change a single line of code or
to recompile your app. This gets achieved within :class:`HelpAppBase` by overriding the main app class methods
:meth:`~ae.gui_app.MainAppBase.change_flow` and :meth:`~ae.gui_app.MainAppBase.change_app_state`.

So to add help support to the widgets of your app you only need to add/provide the help texts with a help id that is
matching the value of the :attr:`help_id` attribute of the widget you need help for.

Additionally you can provide a separate i18n translation message file for each of the supported languages to make your
help texts multi-lingual.


help layout implementation example
----------------------------------

:class:`HelpAppBase` inherits from :class:`~ae.gui_app.MainAppBase` while still being independent from the used GUI
framework/library.

.. note::
    The user interface for this help system has to be provided externally on top of this module. It can either be
    implemented directly in your app project or in a separate framework-specific module.

Use :class:`HelpAppBase` as base class of the GUI framework specific main application class and implement the abstract
methods :meth:`~ae.gui_app.MainAppBase.init_app` and :meth:`~HelpAppBase.ensure_top_most_z_index`::

    from ae.gui_help import HelpAppBase

    class MyMainApp(HelpAppBase):
        def init_app(self, framework_app_class=None):
            self.framework_app = framework_app_class()
            ...
            return self.framework_app.run, self.framework_app.stop

        def ensure_top_most_z_index(self, widget):
            framework_method_to_push_widget_to_top_most(widget)
            ...

To activate the help mode the widget to display the help texts have to be assigned to the main app attribute
:attr:`~HelpAppBase.help_layout` and to the framework app property :attr:`~ae.kivy_app.FrameworkApp.help_layout` via
the :meth:`~ae.gui_app.MainAppBase.change_observable` method::

    main_app.change_observable('help_layout', HelpScreenContainerOrWindow())

The :attr:`~HelpAppBase.help_layout` property is also used as a flag of the help mode activity. By assigning `None` to
these attributes the help mode will be deactivated::

    main_app.change_observable('help_layout', None)

Use the attribute :attr:`~HelpAppBase.help_activator` to provide and store a widget that allows the user to toggle the
help mode activation. The :meth:`~HelpAppBase.help_display` is using it as fallback widget if no help target (or
widget to be explained) got found.

.. hint::
    The de-/activation method :meth:`~ae.kivy_app.KivyMainApp.help_activation_toggle` together with the classes
    :class:`~ae.kivy_help.HelpBehavior`, :class:`~ae.kivy_help.HelpToggler` and :class:`~ae.kivy_help.Tooltip` are
    demonstrating a typical implementation of help activator and help text tooltip widgets.


additional helper functions
---------------------------

The helper functions :func:`anchor_points`, :func:`layout_ps_hints`, :func:`layout_x` and :func:`layout_y`, provided
by this module, are providing a framework-independent calculation of the position and size of the help layout and the
anchor.


flow change context message id
------------------------------

The message id to identify the help texts for each flow button is composed by the :func:`id_of_flow_help`, using the
prefix marker string defined by the module variable :data:`FLOW_HELP_ID_PREFIX` followed by the flow id of the flow
widget.

For example the message id for a flow button with the flow action `'open'`, the object `'item'` and the (optional)
flow key `'123456'` is resulting in the following help text message id::

    'help_flow#open_item:123456'

If there is no need for a detailed message id that is taking the flow key into account, then simply create a help text
message id without the flow key.

The method :meth:`~HelpAppBase.help_display` does first search for a message id including the flow key in the available
help text files and if not found it will automatically fallback to use a message id without the flow key::

    'help_flow#open_item'

.. hint::
    More information regarding the flow id you find in the doc string of the module :mod:`ae.gui_app` in the section
    :ref:`application flow`.


application state change context message id
-------------------------------------------

The message ids for app state change help texts are using the prefix marker string defined by the module variable
:data:`APP_STATE_HELP_ID_PREFIX`, followed by the name of the app state and are composed via the method
:func:`id_of_state_help`.


pluralize-able help texts
-------------------------

Each message id can optionally have several different help texts for their pluralization. For that simply add a `count`
item to the `help_vars` property of the help target widget and then define a help text for the all the possible count
cases in your message text file like shown in the following example::

    {
        'message_id': {
                       'zero':      "help text if {count} == 0",    # {count} will be replaced with `'0'`
                       'one':       "help text if count == 1",
                       'many':      "help text if count > 1",
                       'negative':  "help text if count < 0",
                       '':          "fallback help text if count is None",
                       },
       ...
    }

The provided `count` value can also be included/displayed in the help text, like shown in the `'zero'` count case of
the example.


pre- and post-change help texts
-------------------------------

to display a different help message before and after the change of the flow id or the app state define a message
dict with the keys `''` (an empty string) and `'after'` like shown in the following example::

    {
        'message_id': {
                       '':      "help text displayed before the flow/app-state change.",
                       'after': "help text displayed after the flow/app-state change",
                       },
       ...
    }


If you want to move/change the help target to another widget after a change, then use instead of `'after'` the
'`next_help_id'` message dict key::

    {
        'message_id': {
                       '':              "help text before the change",
                       'next_help_id':  "help_flow#next_flow_id",
                       },
       ...
    }

In this case the help target will automatically change to the widget specified by the flow id in the '`next_help_id'`
key, if the user was tapping the second time on the first/initial help target widget.


i18n help texts
---------------

The displayed help messages related to the message id will automatically get translated into the default language of the
current system/environment.

The declaration and association of message ids and their related help messages is done with the help of the namespace
portion :mod:`ae.i18n`.


further examples
----------------

More details on these and other features of this help system, e.g. the usage of f-strings in the help texts, is
documented in the doc string of the :mod:`ae.i18n` module.

A more complex example app demonstrating the features of this context help system can be found in the repository of the
`kivy lisz demo app <https://gitlab.com/ae-group/kivy_lisz>`_.

app tours
=========

The following classes provided by this portion building a solid fundament to implement tours for your app:

* :class:`TourBase`
* :class:`TourDropdownFromButton`
* :class:`OnboardingTour`
* :class:`UserPreferencesTour`


app tour start and stop events
------------------------------

The following main app event methods get called (if they exist) in relation to the start/stop of an app tour:

* `on_tour_init`: called when an app tour got initialized and is just before to be started.
* `on_tour_exit`: called when an app tour got finished and the app states got restored to the values of the tour start.


UI-specific implementation
--------------------------

To complete the implementation of the app tours, the UI-specific framework has to provide a tour layout class, which is
highlighting the widget explained and to display a tooltip and the tour page texts.

.. hint:: the :class:`~ae.kivy_help.TourOverlay` class is a quite complete implementation of a tour layout class.

Optionally for the 'user_registration' page of the :class:`OnboardingTour` a open user name editor flow has to be
implemented.
"""
from abc import abstractmethod, ABC
from copy import deepcopy
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from ae.inspector import stack_vars, try_eval                                                             # type: ignore
from ae.i18n import default_language, get_f_string, get_text, register_package_translations, translation  # type: ignore
from ae.gui_app import (                                                                                  # type: ignore
    FLOW_KEY_SEP, flow_action, flow_class_name, flow_path_id, id_of_flow, update_tap_kwargs, MainAppBase)


__version__ = '0.2.37'


register_package_translations()


CLOSE_POPUP_FLOW_ID = id_of_flow('close', 'flow_popup')             #: flow id to close opened dropdown/popup

APP_STATE_HELP_ID_PREFIX = 'help_app_state#'                        #: message id prefix for app state change help texts
FLOW_HELP_ID_PREFIX = 'help_flow#'                                  #: message id prefix for flow change help texts
TOUR_PAGE_HELP_ID_PREFIX = 'tour_page#'                             #: message id prefix of tour page text/dict

IGNORED_HELP_FLOWS = (CLOSE_POPUP_FLOW_ID, )                        #: tuple of flow ids never search/show help text for
IGNORED_HELP_STATES = ('flow_id', 'flow_path', 'win_rectangle')     #: tuple of app state names never searched help for

REGISTERED_TOURS = dict()                                           #: map(name: class) of all registered tour classes


PsHintsType = Dict[str, Any]                                        #: actually Dict[str, Union[float, str]] but mypy...


def anchor_points(font_size: float, ps_hints: PsHintsType) -> Tuple[float, ...]:
    """ recalculate points of the anchor triangle drawing.

    :param font_size:       font_size to calculate size (radius == hypotenuse / 2) of the anchor triangle.

    :param ps_hints:        pos/size hints dict containing the three keys:
                            anchor_x (anchor x coordinate in window),
                            anchor_y (anchor y coordinate in window) and
                            anchor_dir (anchor direction: 'r'=right, 'i'=increase-y, 'l'=left, 'd'=decrease-y)

                            .. note:
                                the direction in the y axis got named increase for higher y values
                                and `decrease` for lower y values to support different coordinate
                                systems of the GUI frameworks.

                                For example in `kivy` the zero value of the y axis is at the bottom
                                of the app window, whereas in enaml/qt it is at the top.

    :return:                tuple of the three x and y coordinates of the anchor triangle edges.
    """
    if not ps_hints:
        return ()           # return empty tuple to prevent run-time-error at kv build/init

    radius = font_size * 0.69
    anchor_x, anchor_y, anchor_dir = ps_hints['anchor_x'], ps_hints['anchor_y'], ps_hints['anchor_dir']
    return (anchor_x - (radius if anchor_dir in 'id' else 0),
            anchor_y - (radius if anchor_dir in 'lr' else 0),
            anchor_x + (0 if anchor_dir in 'id' else radius * (-1 if anchor_dir == 'r' else 1)),
            anchor_y + (0 if anchor_dir in 'lr' else radius * (-1 if anchor_dir == 'i' else 1)),
            anchor_x + (radius if anchor_dir in 'id' else 0),
            anchor_y + (radius if anchor_dir in 'lr' else 0),
            )


def help_id_tour_class(help_id: str) -> Optional[Any]:
    """ determine the tour class if passed help id has attached tour pages.

    :param help_id:         help id to determine the tour class from.
    :return:                tour class of an existing tour for the passed help id or None if no associated tour exists.
    """
    tour_id = help_sub_id(help_id)
    if tour_id:
        return tour_id_class(tour_id)
    return None


def help_sub_id(help_id: str) -> str:
    """ determine sub id (flow id, tour id or app state name) of the current/specified/passed help id.

    opposite of :func:`id_of_flow_help` / :func:`id_of_state_help` / :func:`id_of_tour_help`.

    :param help_id:         help id to extract the sub id from.
    :return:                flow id, tour id, app state name or empty string if help id does not contain a sub id.
    """
    if help_id.startswith(APP_STATE_HELP_ID_PREFIX):
        return help_id[len(APP_STATE_HELP_ID_PREFIX):]
    if help_id.startswith(FLOW_HELP_ID_PREFIX):
        return help_id[len(FLOW_HELP_ID_PREFIX):]
    if help_id.startswith(TOUR_PAGE_HELP_ID_PREFIX):
        return help_id[len(TOUR_PAGE_HELP_ID_PREFIX):]
    return ''


def id_of_flow_help(flow_id: str) -> str:
    """ compose help id for specified flow id.

    :param flow_id:         flow id to make help id for.
    :return:                help id for the specified flow id.
    """
    return f'{FLOW_HELP_ID_PREFIX}{flow_id}'


def id_of_state_help(app_state_name: str) -> str:
    """ compose help id for app state name/key.

    :param app_state_name:  name of the app state variable.
    :return:                help id for the specified app state.
    """
    return f'{APP_STATE_HELP_ID_PREFIX}{app_state_name}'


def id_of_tour_help(page_id: str) -> str:
    """ compose help id for specified tour page id.

    :param page_id:         tour page id to make help id for.
    :return:                help id for the specified tour page.
    """
    return f'{TOUR_PAGE_HELP_ID_PREFIX}{page_id}'


def layout_ps_hints(wid_x: float, wid_y: float,
                    wid_width: float, wid_height: float,
                    win_width: float, win_height: float) -> PsHintsType:
    """ recalculate anchor and max width/height on change of widget pos/size or window size.

    :param wid_x:           x coordinate in app window of help target flow widget.
    :param wid_y:           y coordinate in app window of help target flow widget.
    :param wid_width:       width of help target flow widget.
    :param wid_height:      height of help target flow widget.
    :param win_width:       app window width.
    :param win_height:      app window height.
    :return:                dict with position and size hints, like e.g.:

                            * anchor_dir:       direction of the anchor triangle (pointing from help layout
                                                to the help target widget):
                                                'r'=right, 'i'=increase-y, 'l'=left, 'd'=decrease-y(kivy:bottom/qt:top).
                            * anchor_x:         x coordinate of the anchor center.
                            * anchor_y:         y coordinate of the anchor center.
                            * max_width:        maximum width of the layout.
                            * max_height:       maximum height of the layout.

    """
    max_width = win_width - wid_x - wid_width
    if max_width < wid_x:
        max_width = wid_x
        anchor_dir_x = 'l'
    else:
        anchor_dir_x = 'r'
    max_height = win_height - wid_y - wid_height
    if max_height < wid_y:
        max_height = wid_y
        anchor_dir_y = 'd'
    else:
        anchor_dir_y = 'i'
    if max_width > max_height:
        anchor_dir = anchor_dir_x                                       # pylint: disable=possibly-unused-variable
        anchor_x = wid_x + (0 if anchor_dir_x == 'l' else wid_width)    # pylint: disable=possibly-unused-variable
        anchor_y = wid_y + wid_height / 2                               # pylint: disable=possibly-unused-variable
        max_height = win_height
    else:
        anchor_dir = anchor_dir_y
        anchor_x = wid_x + wid_width / 2
        anchor_y = wid_y + (0 if anchor_dir_y == 'd' else wid_height)
        max_width = win_width

    return locals().copy()


def layout_x(anchor_x: float, anchor_dir: str, width: float, win_width: float) -> float:
    """ recalculate help layout x position.

    :param anchor_x:        anchor x coordinate in window.
    :param anchor_dir:      anchor direction: 'r'=right, 'i'=increase-y, 'l'=left, 'd'=decrease-y (kivy:bottom, qt:top).
    :param width:           help layout width.
    :param win_width:       app window width.
    :return:                x coordinate of help layout within the app window.
    """
    if anchor_dir == 'l':
        return anchor_x - width
    if anchor_dir == 'r':
        return anchor_x
    return min(max(0.0, anchor_x - width / 2), win_width - width)


def layout_y(anchor_y: float, anchor_dir: str, height: float, win_height: float) -> float:
    """ recalculate help layout y position.

    :param anchor_y:        anchor y coordinate in window.
    :param anchor_dir:      anchor direction: 'r'=right, 'i'=increase-y, 'l'=left, 'd'=decrease-y (kivy:bottom, qt:top).
    :param height:          help layout height.
    :param win_height:      app window height.
    :return:                y coordinate of help layout in the app window.
    """
    if anchor_dir == 'i':
        return anchor_y
    if anchor_dir == 'd':
        return anchor_y - height
    return min(max(0.0, anchor_y - height / 2), win_height - height)


def register_tour_class(tour_class: Type['TourBase']):
    """ register app tour class.

    :param tour_class:          tour class to register.
    """
    REGISTERED_TOURS[tour_class.__name__] = tour_class


def tour_help_translation(page_id: str) -> Optional[Union[str, Dict[str, str]]]:
    """ determine help translation for the passed page id (flow id or app state name).

    :param page_id:         tour page id.
    :return:                help translation text/dict (if exists) or None if translation not found.
    """
    return (translation_short_help_id(id_of_flow_help(page_id))[0] or
            translation_short_help_id(id_of_state_help(page_id))[0])


def tour_id_class(tour_id: str) -> Optional[Any]:
    """ determine the tour class of the passed tour id.

    :param tour_id:         tour/flow id to determine tour class for.
    :return:                tour class of an existing tour for the passed tour id or None if no tour exists.
    """
    return REGISTERED_TOURS.get(flow_class_name(tour_id, 'Tour'))


def translation_short_help_id(help_id: str) -> Tuple[Optional[Union[str, Dict[str, str]]], str]:
    """ check if a help text exists for the passed help id.

    :param help_id:         help id to check if a translation/help texts exists.
    :return:                tuple of translation text/dict (if exists) and maybe shortened help id(removed detail)
                            or tuple of (None, help_id) if translation not found.
    """
    trans_text_or_dict = translation(help_id)
    short_help_id = help_id
    if not trans_text_or_dict and FLOW_KEY_SEP in help_id:
        short_help_id = help_id[:help_id.index(FLOW_KEY_SEP)]  # remove detail (e.g. flow key or app state value)
        trans_text_or_dict = translation(short_help_id)
    return trans_text_or_dict, short_help_id


def widget_page_id(wid: Any) -> str:
    """ determine tour page id of passed widget.

    :param wid:                 widget to determine tour page id from.
    :return:                    tour page id or empty string if widget has no page id.
    """
    page_id = getattr(wid, 'tap_flow_id', '')
    if not page_id:
        page_id = getattr(wid, 'app_state_name', '')
    return page_id


class TourBase:
    """ abstract tour base class, automatically registering sub-classes as app tours.

    sub-class this generic, UI-framework-independent base class to bundle pages of a tour and make sure that the
    attr:`~TourBase.page_ids` and :attr:`~TourBase.page_data` attributes are correctly set. An UI-framework-dependent
    tour overlay/layout instance, created and assigned to main_app.tour_layout, will automatically create an instance
    of your tour-specific sub-class on tour start.
    """
    def __init_subclass__(cls, **kwargs):
        """ register tour class; called on declaration of tour subclass. """
        super().__init_subclass__(**kwargs)
        register_tour_class(cls)

    def __init__(self, main_app: 'HelpAppBase'):
        super().__init__()
        main_app.vpo(f"TourBase.__init__(): tour overlay={main_app.tour_layout}")
        self._auto_switch_page_request = None
        self._delayed_setup_layout_call = None
        self._initial_page_data = None
        self._saved_app_states: Dict[str, Any] = dict()

        self.auto_switch_pages: Union[bool, int] = False
        """ enable/disable automatic switch of tour pages.

        set to `True`, `1` or `-1` to automatically switch tour pages; `True` and `1` will switch to the next page
        until the last page is reached, while `-1` will switch back to the previous pages until the first page is
        reached; `-1` and `1` automatically toggles at the first/last page the to other value (endless ping-pong until
        back/next button gets pressed by the user).

        the seconds to display each page before switching to the next one can be specified via the item value of the
        the dict :attr:`.page_data` dict with the key `'next_page_delay'`.
        """

        self.page_data: Dict[str, Any] = dict(help_vars=dict())
        """ page data with additional help variables (in `help_vars` key) and optional page text/layout/timing settings.

        The class attribute values are default values for all tour pages and get individually overwritten by the i18n
        translations attributes on tour page change via :meth:`.load_page_data`.

        supported/implemented dict keys:

        * `app_flow_delay`: time in seconds to wait until app flow change is completed (def=1.2, >0.9 for auto-width).
        * `app_reset_delay`: time in seconds between app reset/close-popups and flow reset/prepare-tour-page (def=0.3).
        * `back_text`: caption of tour previous page button (def=get_text('back')).
        * `help_vars`: additional help variables, e.g. `help_translation` providing context help translation dict/text.
        * `next_text`: caption of tour next page button (def=get_text('next')).
        * `next_page_delay`: time in seconds to read the current page before next request_auto_page_switch() (def=9.6).
        * `tip_text` or (empty string): tour page tooltip text fstring message text template.
        """

        self.page_ids: List[str] = list()
        """ list of tour page ids, either initialized via this class attribute or dynamically. """

        self.pages_explained_matcher: Dict[str, Union[Callable[[Any], bool], str]] = dict()
        """ :meth:`MainAppBase.find_widget` match callable to determine explained widget of each tour page. """

        self.page_idx: int = 0                      #: index to the current tour page (in :attr:`.page_ids`)
        self.last_page_idx: Optional[int] = None    #: last tour page index (None on tour start)

        self.main_app = main_app                    #: shortcut to main app instance
        self.layout = main_app.tour_layout          #: tour overlay layout instance

        self.top_popup = None                       #: top most popup widget (in app simulation)

        self.backup_app_states()

        main_app.call_method('on_tour_init', self)  # notify main app to backup additional app-specific non-app-states

    def backup_app_states(self):
        """ backup current states of this app, including flow. """
        main_app = self.main_app
        main_app.vpo("TourBase.backup_app_states")
        self._saved_app_states = deepcopy(main_app.retrieve_app_states())

    def cancel_auto_page_switch_request(self, reset: bool = True):
        """ cancel auto switch callback if requested, called e.g. from tour layout/overlay next/back buttons. """
        if self._auto_switch_page_request:
            self._auto_switch_page_request.cancel()
            self._auto_switch_page_request = None
        if reset:
            self.auto_switch_pages = False

    def cancel_delayed_setup_layout_call(self):
        """ cancel delayed setup layout call request. """
        if self._delayed_setup_layout_call:
            self._delayed_setup_layout_call.cancel()
            self._delayed_setup_layout_call = None

    @property
    def last_page_id(self) -> Optional[str]:
        """ determine last displayed tour page id. """
        return None if self.last_page_idx is None else self.page_ids[self.last_page_idx]    # type: ignore # silly mypy

    def load_page_data(self):
        """ load page before switching to it (and maybe reload after preparing app flow and before setup of layout). """
        page_idx = self.page_idx
        page_cnt = len(self.page_ids)
        assert 0 <= page_idx < page_cnt, f"page_idx ({page_idx}) has to be greater zero and less than {page_cnt}"
        page_id = self.page_ids[page_idx]
        if self._initial_page_data is None:     # reset page data to tour class default: dict(help_vars=dict(), ...)
            self._initial_page_data = self.page_data
            page_data = deepcopy(self.page_data)
        else:
            page_data = deepcopy(self._initial_page_data)

        help_translation = tour_help_translation(page_id)
        tour_translation = translation_short_help_id(id_of_tour_help(page_id))[0]
        if help_translation:
            if tour_translation:
                page_data['help_vars']['help_translation'] = help_translation
            else:
                tour_translation = help_translation

        page_data.update(tour_translation if isinstance(tour_translation, dict) else {'tip_text': tour_translation})

        self.main_app.vpo(f"TourBase.load_page_data(): tour page{page_idx}/{page_cnt} id={page_id} data={page_data}")
        self.page_data = page_data

    def next_page(self):
        """ switch to next tour page. """
        self.teardown_app_flow()

        ids = self.page_ids
        assert self.page_idx + 1 < len(ids), f"TourBase.next_page missing {self.__class__.__name__}:{self.page_idx + 1}"
        self.last_page_idx = self.page_idx
        self.page_idx += 1
        self.main_app.vpo(f"TourBase.next_page #{self.page_idx} id={ids[self.last_page_idx]}->{ids[self.page_idx]}")

        self.setup_app_flow()

    def prev_page(self):
        """ switch to previous tour page. """
        self.teardown_app_flow()

        ids = self.page_ids
        assert self.page_idx > 0, f"TourBase.prev_page wrong/missing page {self.__class__.__name__}:{self.page_idx - 1}"
        self.last_page_idx = self.page_idx
        self.page_idx -= 1
        self.main_app.vpo(f"TourBase.prev_page #{self.page_idx} id={ids[self.last_page_idx]}->{ids[self.page_idx]}")

        self.setup_app_flow()

    def request_auto_page_switch(self):
        """ initiate automatic switch to next tour page. """
        self.cancel_auto_page_switch_request(reset=False)

        next_idx = self.page_idx + self.auto_switch_pages
        if not 0 <= next_idx < len(self.page_ids):
            if self.auto_switch_pages is True:
                self.cancel_auto_page_switch_request()  # only switch to next until last page reached
                return
            self.auto_switch_pages = -self.auto_switch_pages
            next_idx += 2 * self.auto_switch_pages

        main_app = self.main_app
        delay = self.page_data.get('next_page_delay', 30.9)
        main_app.vpo(f"TourOverlay.request_auto_page_switch from #{self.page_idx} to #{next_idx} delay={delay}")
        self._auto_switch_page_request = main_app.call_method_delayed(
            delay, self.prev_page if self.auto_switch_pages < 0 else self.next_page)

    def reset_app_flow(self):
        """ delayed reset of flow path/id to be processed on tour start and after dispatching of popups dismiss. """
        self.main_app.vpo("TourBase.reset_app_flow")

    def reset_app_states(self):
        """ reset app to a defined start to prepare a new tour start. """
        main_app = self.main_app
        main_app.vpo("TourBase.reset_app_states")

        # close all popups and delay reset of flow path/id - to be done after dispatch of popups dismiss
        main_app.close_popups()
        main_app.call_method_delayed(self.page_data.get('app_reset_delay', 0.3), self.reset_app_flow)

    def restore_app_states(self):
        """ restore app states of this app - saved via :meth:`.backup_app_states`. """
        main_app = self.main_app
        main_app.vpo("TourBase.restore_app_states")
        main_app.setup_app_states(self._saved_app_states)

    def setup_app_flow(self):
        """ setup app flow and load page data to prepare a tour page. """
        self.main_app.vpo(f"TourBase.setup_app_flow page_data={self.page_data}")

        self.load_page_data()

        app_flow_delay = self.page_data.get('app_flow_delay', 1.2)  # > 0.9 to complete auto width animation
        self._delayed_setup_layout_call = self.main_app.call_method_delayed(app_flow_delay, self.setup_layout)

    def setup_explained_widget(self):
        """ determine and set the explained widget for the actual tour page. """
        main_app = self.main_app
        page_id = self.page_ids[self.page_idx]
        if page_id in self.pages_explained_matcher:
            matcher = self.pages_explained_matcher[page_id]
            if isinstance(matcher, str):
                matcher = try_eval(matcher, glo_vars=main_app.global_variables(layout=self.layout, tour=self))
            wid = main_app.find_widget(matcher)
            self.page_data['help_vars']['help_translation'] = tour_help_translation(widget_page_id(wid))
        else:
            wid = main_app.widget_by_flow_id(page_id)
            if not wid:
                wid = main_app.widget_by_app_state_name(page_id)
        if wid:
            self.layout.explained_widget = wid

    def setup_layout(self):
        """ setup/prepare tour overlay/layout after switch of tour page. """
        self._delayed_setup_layout_call = None
        main_app = self.main_app
        layout = self.layout

        try:
            self.top_popup = main_app.popups_opened()[-1]
        except IndexError:
            self.top_popup = None

        self.update_page_ids()
        main_app.vpo(f"TourBase.setup_layout(): page id={self.page_ids[self.page_idx]}")

        self.setup_explained_widget()
        self.setup_texts()
        layout.page_updated()

        main_app.ensure_top_most_z_index(layout)

        if self.auto_switch_pages:
            self.request_auto_page_switch()

    def setup_texts(self):
        """ setup texts in tour layout from page_data. """
        main_app = self.main_app
        layout = self.layout
        page_data = self.page_data
        page_idx = self.page_idx

        glo_vars = main_app.global_variables(layout=layout, tour=self)
        if self.layout.explained_widget:
            glo_vars['self'] = self.layout.explained_widget
        if self.top_popup:
            glo_vars['root'] = self.top_popup

        help_vars = page_data['help_vars']
        help_vars['self'] = layout.explained_widget

        main_app.vpo(f"TourBase.setup_texts page_data={page_data}")

        _txt = lambda _t: _t is not None and get_f_string(_t, glo_vars=glo_vars, loc_vars=help_vars) or ""  # noqa: E731

        layout.title_text = _txt(page_data.get('title_text'))
        layout.page_text = _txt(page_data.get('page_text'))

        tip_text = page_data.get('tip_text', page_data.get(''))
        if tip_text is None:
            help_tra = help_vars.get('help_translation')
            tip_text = help_tra.get('', "") if isinstance(help_tra, dict) else help_tra
        layout.tip_text = _txt(tip_text)

        layout.next_text = page_data.get('next_text', get_text('next')) if page_idx + 1 < len(self.page_ids) else ""
        layout.prev_text = page_data.get('back_text', get_text('back')) if page_idx > 0 else ""

    def start(self):
        """ prepare app tour start. """
        self.main_app.vpo("TourBase.start")
        self.reset_app_states()
        self.setup_app_flow()

    def stop(self):
        """ stop/cancel tour. """
        self.main_app.vpo("TourBase.stop")
        self.teardown_app_flow()
        # notify main app to restore additional app-specific states (delayed to be called after self.reset_app_flow())
        self.main_app.call_method_delayed(self.page_data.get('app_reset_delay', 0.3) + 0.12, 'on_tour_exit', self)

    def teardown_app_flow(self):
        """ restore app flow and app states before tour finishing or before preparing/switching to prev/next page. """
        self.main_app.vpo("TourBase.teardown_app_flow")
        self.cancel_delayed_setup_layout_call()
        self.cancel_auto_page_switch_request(reset=False)
        self.restore_app_states()

    def update_page_ids(self):
        """ update/change page ids after app flow setup and before the tour overlay/layout setup.

        override this method to change the page_ids in a running tour. don't forget to reload the page data (by calling
        :meth:`.load_page_data`) if you remove/replace the current page, or to correct/decrement the attribute values
        of :attr:`.last_page_idx` and :attr:`.page_idx` if you remove a page which is preceding the current page.
        """
        self.main_app.vpo(f"TourBase.update_page_ids {self.page_ids}")


class TourDropdownFromButton(TourBase):
    """ generic tour base class to auto-explain a dropdown menu, starting with the button opening the dropdown. """
    determine_page_ids = '_v_'

    def setup_app_flow(self):
        """ prevent opening of sub-menus and close of dropdown if dropdown child would open another dropdown. """
        super().setup_app_flow()
        if self.last_page_idx == 0 and self.page_idx == 1:
            last_page_id = self.page_ids[self.last_page_idx]
            if flow_action(last_page_id) == 'open':
                self.main_app.change_flow(last_page_id, **update_tap_kwargs(self.layout.explained_widget))

        elif self.last_page_idx == 1 and self.page_idx == 0:
            if self.top_popup and flow_action(self.page_ids[self.page_idx]) == 'open':
                self.top_popup.close()

    def update_page_ids(self):
        """ prepare all tour pages - first page is explaining opening dropdown button. """
        super().update_page_ids()
        page_ids = self.page_ids
        if self.page_idx == 1 and page_ids[-1] == TourDropdownFromButton.determine_page_ids:
            main_app = self.main_app
            if not self.top_popup:
                main_app.po("TourDropDownFromButton.update_page_ids: dropdown not opened")
                return

            children = main_app.widget_tourable_children_page_ids(self.top_popup)
            if not children:
                main_app.po(f"TourDropDownFromButton.update_page_ids missing tour-able child in {self.top_popup}")
                return

            page_ids.remove(TourDropdownFromButton.determine_page_ids)
            page_ids.extend(children)

            self.load_page_data()   # reload page data of this 2nd tour page (explaining the first dropdown child)


# ====== app tours =============================================================

_OPEN_USER_PREFERENCES_FLOW_ID = id_of_flow('open', 'user_preferences')


class OnboardingTour(TourBase):
    """ onboarding tour for first app start. """
    def __init__(self, main_app: 'HelpAppBase'):
        """ overridden to handle onboarding tour starts since app installation. """
        started = main_app.get_var('onboarding_tour_started', default_value=0) + 1
        main_app.set_var('onboarding_tour_started', started)    # persistently store in config variable

        super().__init__(main_app)

        self.page_ids.extend([
            '', 'page_switching', 'responsible_layout', 'tip_help_intro', 'tip_help_tooltip', 'layout_font_size',
            'tour_end', 'user_registration'])

        self.pages_explained_matcher.update(dict(
            tip_help_intro=lambda widget: widget.__class__.__name__ == 'HelpToggler',
            tip_help_tooltip=lambda widget: getattr(widget, 'tap_flow_id', None) == _OPEN_USER_PREFERENCES_FLOW_ID,
            layout_font_size=lambda widget: getattr(widget, 'app_state_name', None) == 'font_size',
        ))

        if started > main_app.get_var('onboarding_tour_max_started', default_value=9):
            # this would remove welcome and base pages, unreachable for the user:  ids[:] = ids[ids.index('tour_end'):]
            self.page_idx = self.page_ids.index('tour_end')   # .. instead jump to last page before user registration

    def setup_app_flow(self):
        """ overridden to open user preferences dropdown in responsible_layout tour page. """
        super().setup_app_flow()
        page_id = self.page_ids[self.page_idx]
        if page_id == 'layout_font_size':
            main_app = self.main_app
            flow_id = _OPEN_USER_PREFERENCES_FLOW_ID
            wid = main_app.widget_by_flow_id(flow_id)
            main_app.change_flow(flow_id, **update_tap_kwargs(wid))

        elif page_id == 'user_registration':
            self.layout.stop_tour()
            self.main_app.change_flow(id_of_flow('open', 'user_name_editor'))

    def teardown_app_flow(self):
        """ overridden to close the opened user preferences dropdown on leaving responsible_layout tour page. """
        super().teardown_app_flow()
        if self.top_popup and self.page_ids[self.page_idx] == 'layout_font_size':
            self.top_popup.close()

    def update_page_ids(self):
        """ overridden to remove page (only showing once). """
        super().update_page_ids()
        if self.last_page_id == 'page_switching':
            self.page_ids.remove('page_switching')
            if self.last_page_idx == self.page_idx - 1:
                self.last_page_idx -= 1
                self.page_idx -= 1


class UserPreferencesTour(TourDropdownFromButton):
    """ user preferences menu tour. """

    def __init__(self, main_app: 'HelpAppBase'):
        super().__init__(main_app)

        self.auto_switch_pages = 1
        self.page_data['next_page_delay'] = 3.6
        self.page_ids.extend([_OPEN_USER_PREFERENCES_FLOW_ID, TourDropdownFromButton.determine_page_ids])


class HelpAppBase(MainAppBase, ABC):
    """ main app help base class. """
    displayed_help_id: str = ''                 #: message id of currently explained/focused target widget in help mode
    help_activator: Any = None                  #: help mode de-/activator button widget
    help_layout: Optional[Any] = None           #: help text container widget in active help mode else None
    onboarding_tour_class: Type[OnboardingTour] = OnboardingTour    #: default onboarding app tour class
    tour_layout: Optional[Any] = None           #: tour layout/overlay widget in active tour mode else None
    tour_overlay_class: Optional[Type] = None   #: UI-framework-specific tour overlay class, set by main app sub-class

    _next_help_id: str = ''                     #: last app-state/flow change to show help text on help mode activation
    _closing_popup_open_flow_id: str = ''       #: flow id of just closed popup

    @abstractmethod
    def call_method_delayed(self, delay: float, callback: Union[Callable, str], *args, **kwargs) -> Any:
        """ delayed call of passed callable/method with args/kwargs catching and logging exceptions preventing app exit.

        :param delay:           delay in seconds before calling the callable/method specified by
                                :paramref:`~call_method_delayed.callback`.
        :param callback:        either callable or name of the main app method to call.
        :param args:            args passed to the callable/main-app-method to be called.
        :param kwargs:          kwargs passed to the callable/main-app-method to be called.
        :return:                delayed call event object instance, providing a `cancel` method to allow
                                the cancellation of the delayed call within the delay time.
        """

    @abstractmethod
    def ensure_top_most_z_index(self, widget: Any):
        """ ensure visibility of the passed widget to be the top most in the z index/order.

        :param widget:          the popup/dropdown/container widget to be moved to the top.
        """

    @abstractmethod
    def help_activation_toggle(self):
        """ button tapped event handler to switch help mode between active and inactive (also inactivating tour). """

    # overwritten methods

    def change_app_state(self, app_state_name: str, state_value: Any, send_event: bool = True, old_name: str = ''):
        """ change app state via :meth:`~ae.gui_app.MainAppBase.change_app_state`, show help text in active help mode.

        All parameters are documented in the overwritten method :meth:`~ae.gui_app.MainAppBase.change_app_state`.
        """
        help_vars = dict(app_state_name=app_state_name, state_value=state_value, old_name=old_name)
        if not self.help_app_state_display(help_vars):
            super().change_app_state(app_state_name, state_value, send_event=send_event, old_name=old_name)
            self.help_app_state_display(help_vars, changed=True)

    def change_flow(self, new_flow_id: str, **event_kwargs) -> bool:
        """ change/switch flow id - overriding :meth:`~ae.gui_app.MainAppBase.change_flow`.

        More detailed documentation of the parameters you find in the overwritten method
        :meth:`~ae.gui_app.MainAppBase.change_app_state`.

        This method returns True if flow changed and got confirmed by a declared custom event handler
        (either event method or Popup class) of the app
        AND if the help mode is *not* active or the calling widget is selected
        in active help mode, else False.
        """
        count = event_kwargs.pop('count', None)
        help_vars = dict(new_flow_id=new_flow_id, event_kwargs=event_kwargs)
        if count is not None:
            help_vars['count'] = count

        if not self.help_flow_display(help_vars):
            if super().change_flow(new_flow_id, **event_kwargs):
                self.help_flow_display(help_vars, changed=True)
                return True
        return False

    # help specific methods

    def help_app_state_display(self, help_vars: Dict[str, Any], changed: bool = False) -> bool:
        """ actualize the help layout if active, before and after the change of the app state.

        :param help_vars:       locals (args/kwargs) of overwritten :meth:`~ae.gui_app.MainAppBase.change_flow` method.

                                items passed to the help text formatter:
                                    * `count`: optional number used to render a pluralized help text
                                      for this app state change.

        :param changed:         False before change of the app state, pass True if app state got just/already changed.
        :return:                True if help mode and layout is active and found target widget is locked, else False.
        """
        app_state_name = help_vars.get('app_state_name')
        if not app_state_name or app_state_name in IGNORED_HELP_STATES:
            return False

        help_id = id_of_state_help(app_state_name)

        hlw = self.help_layout
        if hlw is None:
            if translation_short_help_id(help_id)[0]:
                self._next_help_id = help_id
            return False            # inactive help layout

        ret = self.help_display(help_id, help_vars, key_suffix='after' if changed else '')
        if help_id == self.displayed_help_id and not changed:
            ret = False             # allow to execute app state change
        return ret

    def help_display(self, help_id: str, help_vars: Dict[str, Any], key_suffix: str = '', must_have: bool = False
                     ) -> bool:
        """ display help text to the user in activated help mode.

        :param help_id:         help id to show help text for.
        :param help_vars:       variables used in the conversion of the f-string expression to a string.
                                optional items passed to the help text formatter:
                                * `count`: optional number used to render a pluralized help text.
                                * `self`: target widget to show help text for.
        :param key_suffix:      suffix to the key used if the translation is a dict.
        :param must_have:       pass True to display error help text and console output if no help text exists.
        :return:                True if help text got found and displayed.
        """
        has_trans, short_help_id = translation_short_help_id(help_id)
        if not has_trans:
            if not must_have:
                return False
            if self.debug:
                help_id = f"No translation found for help id [b]'{help_id}/{key_suffix}'[/b] in '{default_language()}'"
            else:
                help_id = ''        # show at least initial help text as fallback
            short_help_id = help_id
            key_suffix = ''
            self.play_beep()
        elif key_suffix == 'after' and 'next_help_id' in has_trans and not self._closing_popup_open_flow_id:
            help_id = short_help_id = has_trans['next_help_id']     # type: ignore # silly mypy, Pycharm is more clever
            key_suffix = ''

        glo_vars = self.global_variables()
        hlw: Any = self.help_layout
        hlw.tip_text = get_f_string(short_help_id, key_suffix=key_suffix, glo_vars=glo_vars, loc_vars=help_vars)
        hlw.explained_widget = self.help_widget(help_id, help_vars)     # set help target widget

        self.ensure_top_most_z_index(hlw)
        self.change_observable('displayed_help_id', help_id)
        self.call_method_delayed(0.12, 'on_help_displayed')

        return True

    def help_flow_display(self, help_vars: Dict[str, Any], changed: bool = False) -> bool:
        """ actualize the help layout if active, exclusively called by :meth:`~ae.gui_app.MainAppBase.change_flow`.

        :param help_vars:       locals (args/kwargs) of overwritten :meth:`~ae.gui_app.MainAppBase.change_flow` method.
        :param changed:         False before change to new flow, pass True if flow got changed already.
        :return:                True if help layout is active and found target widget is locked, else False.
        """
        flow_id = help_vars.get('new_flow_id')
        if not flow_id or flow_id in IGNORED_HELP_FLOWS:
            if not changed or flow_id != CLOSE_POPUP_FLOW_ID or not self._closing_popup_open_flow_id:
                if flow_id == CLOSE_POPUP_FLOW_ID:  # check on close to save opening flow id, to reset in changed call
                    self._closing_popup_open_flow_id = flow_path_id(self.flow_path)
                return False
            flow_id = self._closing_popup_open_flow_id      # reset after call of self.help_display()
        wid = self.widget_by_flow_id(flow_id)
        if wid and 'self' not in help_vars:
            help_vars['self'] = wid                         # set help widget to opening button after closing popup

        help_id = id_of_flow_help(flow_id)

        hlw = self.help_layout
        if hlw is None:
            if translation_short_help_id(help_id)[0]:
                self._next_help_id = help_id
            return False            # inactive help layout

        key_suffix = 'after' if changed and not self._closing_popup_open_flow_id else ''
        ret = self.help_display(help_id, help_vars, key_suffix=key_suffix, must_have=not changed)
        self._closing_popup_open_flow_id = ''
        if not changed and (help_id == self.displayed_help_id or flow_action(flow_id) == 'open'):
            # allow to execute flow change of currently explained flow button or if open flow action with no help text
            ret = False
        return ret

    def help_target_and_id(self, help_vars: Dict[str, Any]) -> Tuple[Any, str]:
        """ find help widget/target and help id on help mode activation.

        :param help_vars:       optional help vars.
        :return:                tuple of help target widget and help id.
        """
        activator = self.help_activator
        if self._next_help_id:
            help_id = self._next_help_id
        elif self.flow_id:
            help_id = id_of_flow_help(self.flow_id)
        else:
            return activator, ''

        target = self.help_widget(help_id, help_vars)
        if target is activator:
            help_id = ''
        return target, help_id

    def help_widget(self, help_id: str, help_vars: Dict[str, Any]) -> Any:
        """ ensure/find help target widget via attribute name/value and extend :paramref:`~help_widget.help_vars`.

        :param help_id:         widget.help_id attribute value to detect widget and call stack locals.
        :param help_vars:       help env variables, to be extended with event activation stack frame locals
                                and a 'self' key with the help target widget.
        :return:                found help target widget or self.help_activator if not found.
        """
        wid = help_vars.get('self')
        if not wid or help_id and not getattr(wid, 'help_id', "").startswith(help_id):
            if help_id:
                # first look for widget with help_id attr in kv/enaml rule call stack frame for translation text context
                depth = 1
                while depth <= 15:
                    _gfv, lfv, _deep = stack_vars("", min_depth=depth, max_depth=depth)  # "" to not skip ae.kivy_help
                    widget = lfv.get('self')
                    if getattr(widget, 'help_id', None) == help_id:
                        help_vars.update(lfv)
                        return widget
                    depth += 1

                # then search the widget tree
                wid = self.widget_by_attribute('help_id', help_id)
                if not wid:
                    self.vpo(f"HelpAppBase.help_widget(): widget with help_id '{help_id}' not found")

            if not wid:
                wid = self.help_activator
            help_vars['self'] = wid

        return wid

    def key_press_from_framework(self, modifiers: str, key: str) -> bool:
        """ overwritten ae.gui_app.MainAppBase method to suppress key press events in help or app tour mode.

        :param modifiers:       modifier keys.
        :param key:             key character.
        :return:                True if key got consumed/used else False.
        """
        self.vpo(f"HelpAppBase.key_press_from_framework({modifiers}+{key})")
        if self.help_layout or self.tour_layout:
            return True
        return super().key_press_from_framework(modifiers, key)

    def on_app_started(self):
        """ last app init event on app startup. """
        if self.user_id not in self.registered_users:
            self.start_app_tour()

    def on_flow_popup_close(self, _flow_key: str, _event_kwargs: Dict[str, Any]) -> bool:
        """ overwritten popup close handler of FlowPopup widget to reset help widget/text.

        :param _flow_key:       (unused)
        :param _event_kwargs:   (unused)
        :return:                always True.
        """
        if self.help_layout and self.help_widget(self.displayed_help_id, dict()) is self.help_activator:
            self.help_display('', dict())
        return True

    def on_help_displayed(self):
        """ default post help display event handler for to update the window pos of the explained widget. """
        hlw = self.help_layout
        hlw.explained_pos = hlw.explained_widget.to_window(*hlw.explained_widget.pos)

    def save_app_states(self) -> str:
        """ override MainAppBase method to not overwrite app states if app tour is active. """
        if self.tour_layout:
            return "running app tour prevent to save app states into config file"   # was: self.tour_layout.stop_tour()
        return super().save_app_states()

    def start_app_tour(self, tour_class: Optional[Type['TourBase']] = None) -> bool:
        """ start new app tour, automatically cancelling a currently running app tour.

        :param tour_class:          optional tour (pages) class, default: tour of current help id or `OnboardingTour`.
        :return:                    True if UI-framework support tours/has tour_overlay_class set and tour got started.
        """
        tour_layout_class = self.tour_overlay_class
        if tour_layout_class:
            if self.tour_layout:
                self.tour_layout.stop_tour()
            tour_layout_class(self, tour_class=tour_class)  # pylint: disable=not-callable # false positive
        else:
            self.vpo("HelpAppBase.start_app_tour called but tour overlay/layout class got not set")

        return bool(self.tour_layout)   # overlay instance sets main_app./framework_app.tour_layout on tour start

    def widget_tourable_children_page_ids(self, parent_widget: Any) -> List:
        """" determine all visible and tourable children widgets of the passed parent and its child container widgets.

        :param parent_widget:   parent widget to determine all children that are tourable.
        :return:                list of page ids of tourable children of the passed parent widget.
        """
        tourable_children = list()
        for wid in self.widget_children(parent_widget, only_visible=True):
            page_id = widget_page_id(wid)
            if page_id:
                tourable_children.append(page_id)
            else:
                for sub_wid in self.widget_children(wid, only_visible=True):
                    page_id = widget_page_id(sub_wid)
                    if page_id and page_id not in tourable_children:
                        tourable_children.append(page_id)
        return tourable_children
