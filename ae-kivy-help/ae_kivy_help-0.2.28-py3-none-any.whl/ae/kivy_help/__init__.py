"""
enhance your app with context help, user onboarding, product tours, walkthroughs and tutorials
==============================================================================================

This ae namespace portion integrates context-sensitive help, user onboarding, product tours, walkthroughs and tutorials
into your kivy app.

The generic class :class:`Tooltip` of this portion displays text blocks that are automatically positioned next to any
widget to providing e.g. i18n context help texts or app tour/onboarding info.

:class:`ModalBehavior` is another generic mix-in class that provides modal behavior to any container widget.

The mixin class :class:`HelpBehavior` provided by this namespace portion is extending and preparing any Kivy widget for
to show an individual help text for it. The widget :class:`HelpToggler` is a toggle button to switch the help mode
on and off.

The other classes of this portion are used to overlay or augment the app’s user interface with product tours, tutorials,
walkthroughs and user onboarding/welcome features.

The :class:`AnimatedTourMixin` can be mixed-into a tour class that inherits from :class:`~ae.gui_help.TourBase` to
extend it with animation and glsl shader features.

The class :class:`AnimatedOnboardingTour` is providing an app onboarding tour that covers the core features and can be
easily extended with app-specific tour pages.

Finally, the class :class:`TourOverlay` is implementing a overlay layout widget to display the animations, shaders,
tour page texts, tooltip text and the navigation buttons of an active/running app tour.


mixing-in modal behavior
------------------------

To convert a container widget into a modal dialog, add the :class:`ModalBehavior` mix-in class, provided by this ae
namespace portion.

The following code snippet demonstrates a typical implementation::

    class MyContainer(ModalBehavior, BoxLayout):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)

        def open(self):
            self.activate_modal()

        def close(self):
            self.deactivate_modal()


To activate the modal mode call the method :meth:`~ModalBehavior.activate_modal`. The modal mode can be deactivated by
calling the :meth:`~ModalBehavior.deactivate_modal` method.

All touch, mouse and keyboard user interactions will be consumed or filtered after activating the modal mode. Therefore
it is recommended to also visually change the GUI while in the modal mode, which has to be implemented by the mixing-in
container widget.

.. hint::
    usage examples of the :class:`ModalBehavior` mix-in are e.g. the classes :class:`TourOverlay` and
    :class:`~ae.kivy_app.FlowPopup`.


generic widget to display help and tour texts
---------------------------------------------

the tooltip class :class:`Tooltip` is targeting any widget by pointing with an arrow to it. The position and size of
this widget gets automatically calculated from the targeted widget position and size and the tooltip text size. And if
the screen/window size is not big enough then the tooltip texts get scrollable.

.. hint::
    use cases of the class :class:`Tooltip` are e.g. the help texts prepared and displayed by the method
    :meth:`~ae.gui_help.HelpAppBase.help_display` as well as the "explaining widget" tooltips in an app tour.


help behaviour mixin
--------------------

To show a i18n translatable help text for a Kivy widget create either a sub-class of the widget. The following example
allows to attach a help text to a Kivy :class:`~kivy.uix.button.Button`::

    from kivy.uix.button import Button
    from ae.kivy_help import HelpBehavior

    class ButtonWithHelpText(HelpBehavior, Button):
        ...

Alternatively you can archive this via the definition of a new kv-lang rule, like shown underneath::

    <ButtonWithHelpText@HelpBehavior+Button>


.. note::
    To automatically lock and mark the widget you want to add help texts for, this mixin class has to be specified
    as the first inheriting class in the class or rule declaration.


help activation and de-activation
---------------------------------

Use the widget :class:`HelpToggler` provided by this namespace portion in your app to toggle the active state of the
help mode.

.. hint::
    The :class:`HelpToggler` is using the low-level touch events to prevent the dispatch of the Kivy events `on_press`,
    `on_release` and `on_dismiss` to allow to show help texts for opened dropdowns and popups.


kivy_help portion dependencies
------------------------------

Although this portion depends only on the `Kivy framework <kivy>`_ and the ae namespace portions :mod:`ae.gui_app`,
:mod:`ae.gui_help` and :mod:`ae.kivy_relief_canvas`, it is recommended also include and use the portion
:mod:`ae.kivy_app` to provide context-help-aware widgets.

This namespace portion is a requirement of the :mod:`ae.kivy_app` module and is tight coupled to it. So when you also
include and use the :mod:`ae.kivy_app` for your app, then you only need to specify the :mod:`ae.kivy_app` portion in the
`requirements.txt` files (of the `pip` package installation tool) to automatically integrate also this module. Only for
mobile apps built with buildozer you need also to explicitly add this :mod:`ae.kivy_help` portion to the requirements
list in your `buildozer.spec` file.
"""
import os
import traceback
from copy import deepcopy
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, Union

from kivy.animation import Animation                                                                    # type: ignore
from kivy.app import App                                                                                # type: ignore
from kivy.clock import Clock                                                                            # type: ignore
from kivy.core.window import Window                                                                     # type: ignore
from kivy.input import MotionEvent                                                                      # type: ignore
from kivy.lang import Builder                                                                           # type: ignore
# pylint: disable=no-name-in-module
from kivy.metrics import sp                                                                             # type: ignore
from kivy.properties import (  # type: ignore
    BooleanProperty, DictProperty, ListProperty, NumericProperty, ObjectProperty, StringProperty)
from kivy.uix.floatlayout import FloatLayout                                                            # type: ignore
from kivy.uix.image import Image                                                                        # type: ignore
from kivy.uix.scrollview import ScrollView                                                              # type: ignore
from kivy.uix.textinput import TextInput                                                                # type: ignore
from kivy.uix.widget import Widget                                                                      # type: ignore

from ae.inspector import try_eval                                                                       # type: ignore
from ae.gui_help import anchor_points, help_id_tour_class, HelpAppBase, OnboardingTour, TourBase        # type: ignore
from ae.kivy_glsl import ShaderIdType, ShadersMixin                                                     # type: ignore
from ae.kivy_relief_canvas import ReliefCanvas                                                          # type: ignore


__version__ = '0.2.28'


# load/declared help/tour widgets, based-on Kivy core widgets (without any features from ae.kivy_app/widgets.kv)
Builder.load_file(os.path.join(os.path.dirname(__file__), "widgets.kv"))


class ModalBehavior:                                                                    # pragma: no cover
    """ mix-in making a container widget modal. """
    # abstracts provided by the mixing-in container widget
    center: List
    close: Callable
    collide_point: Callable
    disabled: bool
    fbind: Callable
    funbind: Callable

    auto_dismiss = BooleanProperty()
    """ determines if the container is automatically dismissed when the user hits the Esc/Back key or clicks outside it.

    :attr:`auto_dismiss` is a :class:`~kivy.properties.BooleanProperty` and defaults to True.
    """

    _fast_bound: List = list()                              #: list of arg tuples for fbind/funbind
    _touch_started_inside: Optional[bool] = None            #: flag if touch started inside of the container widget
    _window = ObjectProperty(allownone=True, rebind=True)   #: internal flag to store main window instance if open

    def activate_modal(self):
        """ activate or renew modal mode for the mixing-in container. """
        self.deactivate_modal()

        Window.add_widget(self)
        Window.bind(on_resize=self._align_center, on_key_down=self._on_key_down)

        fast_bind = self.fbind                                                  # pylint: disable=no-member
        self._fast_bound = [('center', self._align_center), ('size', self._align_center)]
        for fast_binding in self._fast_bound:
            fast_bind(*fast_binding)

        self._window = Window

    def _align_center(self, *_args):
        """ reposition container on window resize. """
        if self._window:
            self.center = Window.center

    def deactivate_modal(self):
        """ de-activate modal mode for the mixing-in container. """
        fast_unbind = self.funbind                                              # pylint: disable=no-member
        for fast_unbinding in self._fast_bound:
            fast_unbind(*fast_unbinding)
        self._fast_bound = list()

        if self._window:
            Window.unbind(on_resize=self._align_center, on_key_down=self._on_key_down)
            Window.remove_widget(self)
        self._window = None

    def _on_key_down(self, _window, key, _scancode, _codepoint, _modifiers):
        """ close/dismiss this popup if back/Esc key get pressed - allowing stacking with DropDown/FlowDropDown. """
        if key == 27 and self.auto_dismiss and self._window:
            if not App.get_running_app().tour_layout:   # prevent close/dismiss by Esc-key if app tour is active/running
                self.close()
            return True
        return False

    def on_touch_down(self, touch: MotionEvent) -> bool:
        """ touch down event handler, prevents the processing of a touch on the help activator widget by this popup.

        :param touch:           motion/touch event data.
        :return:                True if event got processed/used.
        """
        if App.get_running_app().main_app.help_activator.collide_point(*touch.pos):
            return False  # allow help activator button to process this touch down event
            # .. and leave self._touch_started_inside == None to not initiate popup.close/dismiss in on_touch_up
        self._touch_started_inside = self.collide_point(*touch.pos)

        # pylint: disable=superfluous-parens # false positive
        if not (self.disabled if self._touch_started_inside else self.auto_dismiss):
            super().on_touch_down(touch)    # type: ignore # pylint: disable=no-member # false positive

        return True

    def on_touch_move(self, touch):
        """ touch move event handler. """
        if not self.auto_dismiss or self._touch_started_inside:
            super().on_touch_move(touch)    # type: ignore # pylint: disable=no-member # false positive
        return True

    def on_touch_up(self, touch):
        """ touch up event handler. """
        if self.auto_dismiss and self._touch_started_inside is False:
            self.close()
        else:
            super().on_touch_up(touch)      # type: ignore # pylint: disable=no-member # false positive
        self._touch_started_inside = None
        return True


class HelpBehavior:
    """ behaviour mixin class for widgets providing help texts.
    """
    help_id = StringProperty()
    """ unique help id of the widget.

    The correct identification of each help-aware widget presuppose that the attribute :attr:`~HelpBehavior.help_id` has
    a unique value for each widget instance. This is done automatically for the widgets provided by the module
    :mod:`~ae.kivy_app` by converting the app flow or app state of these widgets into a help id (see e.g. the
    implementation of the class :class:`~ae.kivy_app.FlowButton`).

    :attr:`help_id` is a :class:`~kivy.properties.StringProperty` and defaults to an empty string.
    """

    help_lock = BooleanProperty(False)
    """ this property is True if the help mode is active and this widget is not the help target.

    :attr:`help_lock` is a :class:`~kivy.properties.BooleanProperty` and defaults to the value `False`.
    """

    help_vars = DictProperty()
    """ dict of extra data to displayed/render the help text of this widget.

    The :attr:`~HelpBehavior.help_vars` is a dict which can be used to provide extra context data to dynamically
    generate, translate and display individual help texts.

    :attr:`help_vars` is a :class:`~kivy.properties.DictProperty` and defaults to an empty dict.
    """

    _shader_args = ObjectProperty()     #: shader internal data / id

    # abstract attributes and methods provided by the class to be mixed into
    collide_point: Callable

    def on_touch_down(self, touch: MotionEvent) -> bool:                                    # pragma: no cover
        """ prevent any processing if touch is done on the help activator widget or in active help mode.

        :param touch:           motion/touch event data.
        :return:                True if event got processed/used.
        """
        main_app = App.get_running_app().main_app

        if main_app.help_activator.collide_point(*touch.pos):
            return False        # allow help activator button to process this touch down event

        if self.help_lock and self.collide_point(*touch.pos):   # main_app.help_layout is not None
            if main_app.help_display(self.help_id, self.help_vars):
                return True

        return super().on_touch_down(touch)                 # type: ignore # pylint: disable=no-member # false positive


class Tooltip(ScrollView):                                                           # pragma: no cover
    """ semi-transparent and optional click-through container to display help and tour page texts. """
    explained_widget = ObjectProperty()
    """ target widget to display tooltip text for (mostly a button, but could any, e.g. a layout widget).

    :attr:`explained_widget` is a :class:`~kivy.properties.ObjectProperty` and defaults to None.
    """

    tip_text = StringProperty()
    """ tooltip text string to display.

    :attr:`tip_text` is a :class:`~kivy.properties.StringProperty` and defaults to an empty string.
    """

    explained_pos = ListProperty()      #: Window position of the explained widget
    has_tour = BooleanProperty(False)   #: True if a tour exists for the current app flow/help context (read-only)
    ps_hints = ObjectProperty()         #: pos- and size-hints for the layout window widget (read-only)
    tap_thru = BooleanProperty(False)   #: True if user can tap widgets behind/covered by this tooltip win (read-only)
    tour_start_pos = ListProperty()     #: screen position of the optionally displayed tour start button (read-only)
    tour_start_size = ListProperty()    #: size of the optionally displayed tour start button (read-only)

    def collide_tap_thru_toggler(self, touch_x: float, touch_y: float) -> bool:
        """ check if touch is on the tap thru toggler pseudo button.

        :param touch_x:         window x position of touch.
        :param touch_y:         window y position of touch.
        :return:                True if user touched the tap through toggler.
        """
        anchor_pts = anchor_points(App.get_running_app().main_app.font_size, self.ps_hints)

        x_values = tuple(x for idx, x in enumerate(anchor_pts) if not idx % 2)
        min_x, max_x = min(x_values), max(x_values)
        y_values = tuple(x for idx, x in enumerate(anchor_pts) if idx % 2)
        min_y, max_y = min(y_values), max(y_values)

        return min_x <= touch_x < max_x and min_y <= touch_y < max_y

    def collide_tour_start_button(self, touch_x: float, touch_y: float) -> bool:
        """ check if touch is on the tap thru toggler pseudo button.

        :param touch_x:         window x position of touch.
        :param touch_y:         window y position of touch.
        :return:                True if user touched the tap thru toggler.
        """
        min_x, min_y = self.tour_start_pos
        width, height = self.tour_start_size
        max_x, max_y = min_x + width, min_y + height

        return min_x <= touch_x < max_x and min_y <= touch_y < max_y

    def on_touch_down(self, touch: MotionEvent) -> bool:
        """ check for additional events added by this class.

        :param touch:           motion/touch event data.
        :return:                True if event got processed/used.
        """
        app = App.get_running_app()
        if self.collide_tap_thru_toggler(*touch.pos):
            self.tap_thru = not self.tap_thru
            ret = True
        elif self.has_tour and self.collide_tour_start_button(*touch.pos):
            ret = app.main_app.start_app_tour(help_id_tour_class(self.explained_widget.help_id))
        elif self.tap_thru or not self.collide_point(*touch.pos):
            ret = False     # if self.tap_thru then make this tooltip widget transparent and let user click through
        else:
            ret = super().on_touch_down(touch)
        return ret


class HelpToggler(ReliefCanvas, Image):                                                               # pragma: no cover
    """ widget to activate and deactivate the help mode.

    To prevent the dismiss of opened popups and dropdowns at help mode activation, this singleton instance has to:

    * be registered in its __init__ to the :attr:`~ae.gui_help.HelpAppBase.help_activator` attribute and
    * have a :meth:`~HelpToggler.on_touch_down` method that is eating the activation touch event (returning True) and
    * a :meth:`~HelpToggler.on_touch_down` method not passing a activation touch in all DropDown/Popup widgets.

    """
    def __init__(self, **kwargs):
        """ initialize an instance of this class and also :attr:`~ae.gui_help.HelpAppBase.help_activator`. """
        App.get_running_app().main_app.help_activator = self
        super().__init__(**kwargs)

    def on_touch_down(self, touch: MotionEvent) -> bool:
        """ touch down event handler to toggle help mode while preventing dismiss of open dropdowns/popups.

        :param touch:           touch event.
        :return:                True if touch happened on this button (and will get no further processed => eaten).
        """
        if self.collide_point(*touch.pos):
            App.get_running_app().main_app.help_activation_toggle()
            return True
        return False


class AnimatedTourMixin:        # (TourBase):
    """ tour class mixin to add individual shaders to the tour layout and their children widgets. """
    # abstracts
    layout: Widget
    main_app: Any
    page_ids: List[str]
    page_idx: int

    def __init__(self, main_app: 'HelpAppBase') -> None:
        super().__init__(main_app)                                          # type: ignore # pylint: disable=no-member

        self._added_animations: List[Tuple[Widget, Animation]] = list()
        self._added_shaders: List[Tuple[Widget, ShaderIdType]] = list()

        self.pages_animations: Dict[Optional[str], Tuple[Tuple[str, Union[Animation, str]], ...]] = dict()
        """ statically declarable class attribute dict of compound animation instances of the pages of this tour.

        the key of this dict is the page id or None (for animations available in all pages of this tour).
        the value of this dict is a tuple of tuples of widget id and animation instances.

        if the first character of the widget id is a `@` then the :attr:`~kivy.animation.Animation.repeat` attribute of
        the :class:`~kivy.animation.Animation` class will be set to True. the rest of the widget id string specifies the
        widget to be animated which is either:

        * one of the widgets of the :class:`TourOverlay` layout class, like `tooltip`, `tour_page_texts`, `title_lbl`,
          `page_lbl`, `prev_but` or `next_but`.
        * the explained widget if an empty string is given.
        * the :class:`TourOverlay` layout class instance for any other string.
        """

        self.pages_shaders: Dict[Optional[str], Tuple[Tuple[str, ShaderIdType], ...]] = dict()
        """ statically declarable class attribute dict of widget shaders for the pages of this tour.

        the key of this dict is the page id or None (for shaders available in all pages of this tour).
        the value of this dict is a tuple of tuples of widget id and add_shader()-kwargs.

        the widget id string specifies the widget to which a shader will be added, which is either:

        * one of the widgets of the :class:`TourOverlay` layout class, like `tooltip`, `tour_page_texts`, `title_lbl`,
          `page_lbl`, `prev_but` or `next_but`.
        * the explained widget if an empty string is given.
        * the :class:`TourOverlay` layout class instance for any other string.

        the add_shader()-kwargs dict will directly be passed to the :meth:`~ae.kivy_glsl.ShadersMixin.add_shader`
        method.
        """

    def _evaluated_shader_kwargs(self, shader_kwargs: dict) -> dict:
        tour_shader_kwargs = deepcopy(shader_kwargs)
        glo_vars = self.main_app.global_variables(layout=self.layout, sp=sp, tour=self, Clock=Clock, Window=Window)
        for key, arg in tour_shader_kwargs.items():
            if isinstance(arg, str) and key not in ('add_to', 'render_shape', 'shader_code', 'shader_file'):
                tour_shader_kwargs[key] = try_eval(arg, glo_vars=glo_vars)
        return tour_shader_kwargs

    def setup_animations(self):
        """ setup shaders specified in class attribute :attr:`~AnimatedTourMixin.pages_shaders`. """
        layout = self.layout
        page_id = self.page_ids[self.page_idx]

        pages_shaders = self.pages_shaders.get(None, ()) + self.pages_shaders.get(page_id, ())
        added = list()
        for wid_id, shader_kwargs in pages_shaders:
            wid = layout.ids.get(wid_id, layout) if wid_id else self.layout.explained_widget
            added.append((wid, wid.add_shader(**self._evaluated_shader_kwargs(shader_kwargs))))
        self._added_shaders = added

        pages_animations = self.pages_animations.get(None, ()) + self.pages_animations.get(page_id, ())
        added = list()
        for wid_id, anim in pages_animations:
            if isinstance(anim, str):
                glo_vars = self.main_app.global_variables(layout=self.layout, sp=sp, tour=self,
                                                          A=Animation, Animation=Animation, Clock=Clock, Window=Window)
                anim = try_eval(anim, glo_vars=glo_vars)
            if wid_id[0] == '@':
                wid_id = wid_id[1:]
                anim.repeat = True
            wid = layout.ids.get(wid_id, layout) if wid_id else self.layout.explained_widget
            anim.start(wid)
            added.append((wid, anim))
        self._added_animations = added

    def setup_layout(self):
        """ overridden to setup animations and shaders of the current tour page. """
        # noinspection PyUnresolvedReferences
        super().setup_layout()                                                              # pylint: disable=no-member
        self.setup_animations()

    def simulate_text_input(self, text_input: TextInput, text_to_delay: str,
                            text_to_insert: str = "", deltas: Tuple[float, ...] = (0.9, 0.6, 0.3)):
        """ simulate the typing of texts by a user entered into an explained TextInput widget of a tour page.

        :param text_input:      text input widget, either of type :class:`~kivy.textinput.TextInput` or
                                :class:`~ae.kivy_app.FlowInput`.
        :param text_to_delay:   text string to be inserted delayed by the seconds specified in deltas[0].
        :param text_to_insert:  text string to be inserted directly into the passed text input widget.
        :param deltas:          delay deltas in seconds between each character to simulate text inputted by a user.
        """
        if text_input.get_root_window():
            if text_to_insert:
                if text_input.interesting_keys.get(ord(text_to_insert), None) == 'backspace':
                    text_input.do_backspace()
                else:
                    text_input.insert_text(text_to_insert)

            if text_to_delay:
                next_delay = deltas[0]
                self.main_app.call_method_delayed(next_delay, self.simulate_text_input, text_input, text_to_delay[1:],
                                                  text_to_insert=text_to_delay[0], deltas=deltas[1:] + (next_delay, ))

    def teardown_animations(self):
        """ teardown shaders added by :meth:`~AnimatedTourMixin.setup_animations` method for current tour page. """
        for wid, anim in reversed(self._added_animations):
            anim.stop(wid)
        self._added_animations = list()
        for wid, shader_id in reversed(self._added_shaders):
            wid.del_shader(shader_id)
        self._added_shaders = list()

    def teardown_app_flow(self):
        """ overridden to teardown the animations of the current/last-shown tour page. """
        self.teardown_animations()
        # noinspection PyUnresolvedReferences
        super().teardown_app_flow()                                                         # pylint: disable=no-member


class AnimatedOnboardingTour(AnimatedTourMixin, OnboardingTour):
    """ onboarding tour, extended with glsl shaders.
    """
    def __init__(self, main_app: 'HelpAppBase') -> None:
        super().__init__(main_app)

        self._bound = None

        self.pages_animations.update({
            None: (
                ('@root',
                 Animation(ani_value=0.999, t='in_out_sine', d=30) + Animation(ani_value=0.0, t='in_out_sine', d=9)),
            ),
            '': (
                ('next_but',
                 "A(font_size=layout.font_height, t='in_out_sine', d=24) + "
                 "A(font_size=layout.main_app.framework_app.min_font_size, t='in_out_sine', d=3) + "
                 "A(font_size=layout.main_app.framework_app.max_font_size, t='in_out_sine', d=6) + "
                 "A(font_size=layout.font_height, t='in_out_sine', d=3)"),
            ),
            'layout_font_size': (
                ('@',
                 "A(value=layout.main_app.framework_app.max_font_size, t='in_out_sine', d=12.9) + "
                 "A(value=layout.main_app.framework_app.min_font_size, t='in_out_sine', d=4.2)"),
            )
        })

        self.pages_shaders.update({
            '': (
                ('root', dict(
                    alpha="lambda: 0.39 * layout.ani_value",
                    center_pos="lambda: list(map(float, layout.ids.next_but.center))",
                    shader_code="=plunge_waves",
                    time="lambda: -Clock.get_boottime()",
                    tint_ink=(0.21, 0.39, 0.09, 0.9),
                )),
                ('tour_page_texts', dict(add_to='before')),
                ('next_but', dict(
                    add_to='before',
                    alpha="lambda: 0.3 + layout.ani_value / 3",
                    render_shape='Ellipse',
                    shader_code='=plunge_waves',
                )),
            ),
            'page_switching': (
                ('root', dict(
                    alpha="lambda: 0.39 * layout.ani_value",
                    center_pos="lambda: list(map(float, layout.ids.prev_but.center))",
                    shader_code="=plunge_waves",
                    time="lambda: -Clock.get_boottime()",
                    tint_ink=(0.21, 0.39, 0.09, 0.9),
                )),
                ('tour_page_texts', dict(add_to='before')),
                ('prev_but', dict(
                    add_to='before',
                    alpha="lambda: 0.12 + layout.ani_value / 3",
                    render_shape='Ellipse',
                    shader_code='=plunge_waves',
                    time="lambda: -Clock.get_boottime()",
                )),
            ),
            'tip_help_intro': (
                ('tour_page_texts', dict(
                    add_to='before',
                    alpha="lambda: 0.12 + layout.ani_value / 3",
                    render_shape='RoundedRectangle',
                    shader_code='=worm_whole',
                    tint_ink=(0.021, 0.039, 0.009, 0.9),
                )),
                ('prev_but', dict(
                    add_to='before',
                    alpha="lambda: 0.12 + layout.ani_value / 3",
                    render_shape='Ellipse',
                    shader_code='=worm_whole',
                    time="lambda: -Clock.get_boottime()",
                )),
                ('next_but', dict(
                    add_to='before',
                    alpha="lambda: 0.12 + layout.ani_value / 3",
                    render_shape='Ellipse',
                    shader_code='=worm_whole',
                )),
            ),
            'tip_help_tooltip': (
                ('prev_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=fire_storm',
                    tint_ink=(0.81, 0.39, 0.09, 0.39),
                    time="lambda: -Clock.get_boottime()",
                )),
                ('next_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=fire_storm',
                    tint_ink=(0.03, 0.03, 0.9, 0.39),
                )),
            ),
            'responsible_layout': (
                ('prev_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=colored_smoke',
                    time="lambda: -Clock.get_boottime()",
                )),
                ('next_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=colored_smoke',
                )),
            ),
            'layout_font_size': (
                ('prev_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=circled_alpha',
                    tint_ink=(0.51, 0.39, 0.9, 0.999),
                )),
                ('next_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    shader_code='=circled_alpha',
                    tint_ink=(0.81, 0.39, 0.9, 0.999),
                )),
            ),
            'tour_end': (
                ('tour_page_texts', dict(add_to='before')),
                ('prev_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    tint_ink=(0.51, 0.39, 0.9, 0.999),
                    time="lambda: -Clock.get_boottime()",
                )),
                ('next_but', dict(
                    add_to='before',
                    render_shape='Ellipse',
                    tint_ink=(0.81, 0.39, 0.9, 0.999),
                )),
            ),
        })

    def next_page(self):
        """ overriding to remove next button size animation only visible in the first tour after app re/start. """
        layout = self.layout
        layout.ani_value = 0.0
        super().next_page()
        if self.last_page_id == '' and self.pages_animations.pop('', False):
            Animation(font_size=layout.font_height).start(layout.ids.next_but)  # set font size back to original value

    def setup_layout(self):
        """ overridden to update layout texts if app window/screen orientation (app.landscape) changes. """
        super().setup_layout()
        page_id = self.page_ids[self.page_idx]
        if page_id == 'responsible_layout':
            self._bound = self.main_app.framework_app.fbind('landscape', lambda *_args: self.setup_texts())
        elif page_id == 'layout_font_size':
            self._bound = self._added_animations[-1][1].fbind('on_progress', lambda *_args: self.setup_texts())

    def teardown_animations(self):
        """ overridden to unbind setup_texts() on leaving the responsible_layout tour page. """
        if self._bound:
            page_id = self.page_ids[self.page_idx]
            if page_id == 'responsible_layout':
                self.main_app.framework_app.unbind_uid('landscape', self._bound)
            elif page_id == 'layout_font_size':
                # noinspection PyUnresolvedReferences
                self._added_animations[-1][1].unbind_uid('on_progress', self._bound)
            self._bound = None

        super().teardown_animations()


class TourOverlay(ModalBehavior, ShadersMixin, FloatLayout):
    """ tour layout/view overlay singleton class to display an active/running modal app tour with optional glsl shaders.
    """
    ani_value = NumericProperty()
    """ animated float value between 0.0 and 1.0, used e.g. by :attr:`AnimatedTourMixin.pages_animations`.

    :attr:`ani_value` is a :class:`~kivy.properties.NumericProperty` and is read-only.
    """

    explained_pos = ListProperty([-9, -9])
    """ window position of the target/explained widget.

    :attr:`explained_pos` is a :class:`~kivy.properties.ListProperty` and is read-only.
    """

    explained_widget = ObjectProperty()
    """ explained widget instance on actual tour (page).

    :attr:`explained_widget` is a :class:`~kivy.properties.ObjectProperty` and is read-only.
    """

    label_height = NumericProperty()
    """ height in pixels of the page text labels and text lines.

    :attr:`label_height` is a :class:`~kivy.properties.NumericProperty` and is read-only.
    """

    navigation_disabled = BooleanProperty()
    """ if this flag is True then the back/next buttons in the tour layout/overlay are disabled.

    :attr:`navigation_disabled` is a :class:`~kivy.properties.BooleanProperty` and is read-only.
    """

    tour_instance = ObjectProperty()
    """ holding the :class:`~ae.gui_help.TourBase` instance of the current tour, initialized by :meth:`.start_tour`.

    :attr:`tour_instance` is a :class:`~kivy.properties.ObjectProperty` and is read-only.
    """

    def __init__(self, main_app: HelpAppBase, tour_class: Optional[Type['TourBase']] = None, **kwargs):
        """ prepare app and tour overlay (singleton instance of this class) to start tour.

        :param main_app:        main app instance.
        :param tour_class:      optional tour (pages) class, default: tour class of current help id or OnboardingTour.
        """
        self.main_app = main_app
        main_app.vpo("TourOverlay.__init__")

        if main_app.onboarding_tour_class is OnboardingTour:
            main_app.onboarding_tour_class = AnimatedOnboardingTour

        self._tooltip_animation = None
        self.auto_dismiss = False
        self.explained_widget = main_app.help_activator             # assign dummy init widget to prevent None errors

        super().__init__(**kwargs)

        if main_app.help_layout:
            main_app.help_activation_toggle()   # deactivate help mode if activated

        self.start_tour(tour_class)

    def next_page(self):
        """ switch to next tour page. """
        self.main_app.vpo("TourOverlay.next_page")
        self.navigation_disabled = True
        self.tour_instance.cancel_auto_page_switch_request()
        self.tour_instance.next_page()

    def page_updated(self):
        """ callback from :meth:`~TourBase.setup_layout` for UI-specific patches, after tour layout/overlay setup. """
        Clock.tick()                        # let Kivy fully update the layout (e.g. for tour_page_texts.height)
        tooltip = self.ids.tooltip
        win_height = Window.height
        nav_y = self.label_height * 1.29    # default pos_y of navigation bar with prev/next buttons
        if self.main_app.widget_visible(tooltip):
            exp_y = self.explained_pos[1]
            pos1 = min(exp_y, tooltip.y)
            pos2 = max(exp_y + self.explained_widget.height, tooltip.top)
            if pos1 < win_height - pos2:
                nav_y = max(nav_y + pos2, win_height - self.ids.tour_page_texts.height)
        Animation(navigation_pos_hint_y=nav_y / win_height, t='in_out_sine', d=3).start(self)

        self.navigation_disabled = False

    def prev_page(self):
        """ switch to previous tour page. """
        self.main_app.vpo("TourOverlay.prev_page")
        self.navigation_disabled = True
        self.tour_instance.cancel_auto_page_switch_request()
        self.tour_instance.prev_page()

    def start_tour(self, tour_cls: Optional[Type[TourBase]] = None) -> bool:
        """ reset app state and prepare tour to start.

        :param tour_cls:        optional tour (pages) class, default: tour of currently shown help id or OnboardingTour.
        :return:                True if tour exists and got started.
        """
        main_app = self.main_app
        if tour_cls is None:
            tour_cls = help_id_tour_class(main_app.displayed_help_id) or main_app.onboarding_tour_class
        main_app.vpo(f"TourOverlay.start_tour tour_cls={tour_cls.__name__}")

        try:
            main_app.change_observable('tour_layout', self)             # set tour layout
            # noinspection PyArgumentList
            self.tour_instance = tour_instance = tour_cls(main_app)     # initialize tour instance
            tour_instance.start()                                       # start tour
        except Exception as ex:
            main_app.po(f"TourOverlay.start_tour exception {ex}")
            traceback.print_exc()
            main_app.change_observable('tour_layout', None)             # reset tour layout
            return False

        ani = Animation(ani_value=0.3, t='in_out_sine', d=6) + Animation(ani_value=0.999, t='in_out_sine', d=3)
        ani.repeat = True
        ani.start(self.ids.tooltip)
        self._tooltip_animation = ani

        self.activate_modal()

        return True

    def stop_tour(self):
        """ stop tour and restore the initially backed-up app state. """
        main_app = self.main_app
        main_app.vpo("TourOverlay.stop_tour")

        self.navigation_disabled = True

        if self._tooltip_animation:
            self._tooltip_animation.stop(self.ids.tooltip)

        if self.tour_instance:
            self.tour_instance.stop()
        else:
            main_app.po("TourOverlay.stop_tour error: called without tour instance")

        main_app.change_observable('tour_layout', None)    # set app./main_app.tour_layout to None

        self.deactivate_modal()
