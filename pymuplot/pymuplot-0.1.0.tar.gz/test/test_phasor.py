import unittest
import random
from PyQt5 import QtCore
from pyqtgraph import setConfigOption
from pyqtest import TestApp

from pymuplot.phasor import PhasorDiagram
from pymuplot.phasor import PhasorDiagramUI
from pymuplot.phasor import _linestyle_to_dash

setConfigOption("antialias", True)


class TestPhasorDiagram(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(self)

    def test_add_and_update_data(self):
        d = PhasorDiagram()
        d.set_range(100)
        d.add_phasor(0, amp=80, phi=1)
        d.add_phasor(1, amp=80, phi=1, color=(255, 0, 0))
        d.update_data(1, 80, 2)

        self.app(d, ["White phasor in first quadrant",
                     "Red phasor in second quadrant"])

    def test_range_is_two(self):
        d = PhasorDiagram()
        d.set_range(2)
        self.app(d, ["Range is 2"])

    def test_range_change(self):
        d = PhasorDiagram()
        d.set_range(2)
        d.set_range(4)
        self.app(d, ["Range is 4"])

    def test_legend(self):
        d = PhasorDiagram()
        d.add_phasor('ph-1', amp=80, phi=0, color=(255, 0, 0), width=3)
        d.add_phasor('ph-3', amp=80, phi=-2*3.14/3, color=(0, 0, 255))
        d.add_legend()
        d.set_range(80)
        self.app(d, ["Legend OK",
                     "Lines in legend have different widths"])

    def test_legend_prefer_name(self):
        d = PhasorDiagram()
        d.add_phasor(0, amp=80, phi=0, color=(255, 0, 0), name="Ua")
        d.add_phasor(1, amp=80, phi=2*3.14/3, color=(0, 255, 0))
        d.add_legend()
        d.set_range(80)
        self.app(d, ["Legend: Ua, 1"])

    def test_legend_show_twice(self):
        d = PhasorDiagram()
        d.set_range(1)
        d.add_phasor(0, amp=1, phi=0)
        d.add_legend()
        d.add_legend()
        self.app(d, ["Legend OK"])

    def test_clear_empty(self):
        d = PhasorDiagram()
        d.remove_phasors()
        self.app(d, ["Grid OK"])

    def test_clear_and_add_legend(self):
        d = PhasorDiagram()
        d.set_range(80)
        d.add_phasor(0, amp=80, phi=0, color=(255, 0, 0), name="Ua")
        d.add_phasor(1, amp=80, phi=0, color=(0, 255, 0), name="Ub")
        d.add_legend()
        d.remove_phasors()
        d.add_phasor(0, amp=80, phi=0, name="Ua")
        d.add_legend()
        self.app(d, ["Legend: Ua"])

    def test_set_invisible(self):
        d = PhasorDiagram()

        d.set_range(2)
        d.add_phasor(0, amp=1, phi=0, color=(255, 0, 0))
        d.add_phasor(1, amp=2, phi=1, color=(0, 255, 0))
        d.add_phasor(2, amp=2, phi=1, color=(0, 0, 255))
        d.add_legend()

        d.set_visible(1, False)
        d.set_visible(2, False)
        d.set_visible(2, True)
        d.set_visible(3, False)

        self.app(d, ["2 phasors in diagram",
                     "3 items in legend"])

    def test_all_styles(self):
        d = PhasorDiagram()

        d.add_phasor(0, amp=1, phi=0.0, linestyle='solid')
        d.add_phasor(1, amp=1, phi=0.5, linestyle='dashed')
        d.add_phasor(2, amp=1, phi=1.0, linestyle='dotted')

        d.add_phasor(3, amp=1, phi=1.5, linestyle='solid', width=2)
        d.add_phasor(4, amp=1, phi=2.0, linestyle='dashed', width=2)
        d.add_phasor(5, amp=1, phi=2.5, linestyle='dotted', width=2)

        d.add_phasor(6, amp=2, phi=3.0, linestyle='solid', width=3)
        d.add_phasor(7, amp=2, phi=3.5, linestyle='dashed', width=3)
        d.add_phasor(8, amp=2, phi=4.0, linestyle='dotted', width=3)
        d.set_range(2)
        d.add_legend()

        self.app(d, ["Phasors of different styles",
                     "Legend OK"])

    def test_scale_dashed(self):
        d = PhasorDiagram()

        d.add_phasor(1, amp=1, phi=0.1, linestyle='dashed', width=2)
        d.add_phasor(2, amp=2, phi=0.2, linestyle='dashed', width=2)
        d.add_phasor(3, amp=4, phi=0.3, linestyle='dashed', width=2)
        d.add_phasor(4, amp=1, phi=2.1, linestyle='dotted', width=2)
        d.add_phasor(5, amp=2, phi=2.2, linestyle='dotted', width=2)
        d.add_phasor(6, amp=4, phi=2.3, linestyle='dotted', width=2)
        d.add_phasor(7, amp=5, phi=4.1, linestyle='dashed', width=4)
        d.add_phasor(8, amp=6, phi=4.2, linestyle='dashed', width=4)
        d.add_phasor(9, amp=7, phi=4.3, linestyle='dashed', width=4)
        d.set_range(7)
        d.add_legend()

        self.app(d, ["Styles are the same in groups"])


class TestPhasorDiagram_Animation(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.counter = 0

    def test_three_phasors_animation(self):
        app = TestApp(self)

        d = PhasorDiagram()
        d.add_phasor('ph-1', color=(255, 0, 0), linestyle='dashed')
        d.add_phasor('ph-2', color=(0, 255, 0), linestyle='dotted')
        d.add_phasor('ph-3', color=(0, 0, 255))
        d.add_legend()

        def rotate():
            delta_ph = self.counter / 200
            delta_am = self.counter / 10
            d.update_data('ph-1', 10 + delta_am, 0 + delta_ph)
            d.update_data('ph-2', 10, 2 + delta_ph)
            d.update_data('ph-3', 10, 4 + delta_ph)
            d.set_range(10 + delta_am)
            self.counter = self.counter + 1

        timer = QtCore.QTimer()
        timer.setInterval(10)
        timer.timeout.connect(rotate)
        self.counter = 0
        timer.start()

        app(d, ["Phasors smoothly rotating",
                "Amplitude of red phasor grows"])


class TestPhasorDiagram_Smoke(unittest.TestCase):
    def test_fast_update_data_and_range(self):
        app = TestApp(self)

        d = PhasorDiagram()
        d.add_phasor('ph-1', linestyle='dashed')
        d.add_phasor('ph-2', linestyle='dotted')
        d.add_phasor('ph-3')
        d.add_legend()

        def rotate():
            x = random.normalvariate(3, 1)
            if x < 0:
                x = 0
            d.update_data('ph-1', x, x+1)
            d.update_data('ph-2', x, x+2)
            d.update_data('ph-3', x, x+3)
            d.set_range(x)

        timer = QtCore.QTimer()
        timer.setInterval(10)
        timer.timeout.connect(rotate)
        timer.start()
        app(d, ["No smoke"])


class TestPhasorDiagram_Deprecation(unittest.TestCase):
    def setUp(self):
        TestApp(self)

    def test_size_arg(self):
        with self.assertWarns(FutureWarning):
            PhasorDiagram(size=100)

    def test_end_arg(self):
        with self.assertWarns(FutureWarning):
            PhasorDiagram(end='arrow')

    def test_set_phasor_visible(self):
        d = PhasorDiagram()
        d.add_phasor(0)
        with self.assertWarns(FutureWarning):
            d.set_phasor_visible(0, False)

    def test_update_phasor(self):
        d = PhasorDiagram()
        d.add_phasor(0)
        with self.assertWarns(FutureWarning):
            d.update_phasor(0, 1, 2)

    def test_show_legend(self):
        d = PhasorDiagram()
        d.add_phasor(0)
        with self.assertWarns(FutureWarning):
            d.show_legend()


class TestPhasorDiagramUI(unittest.TestCase):
    def setUp(self):
        self.app = TestApp(self)

    def test_u_and_i(self):
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_i(3, 'i0', color=(255, 255, 0), width=2)
        d.add_i(4, 'i0', color=(255, 0, 0), width=2)
        d.add_i(5, 'i0', color=(0, 255, 0), width=2)
        d.add_legend()

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)
        d.update_data(3, 1, 1)
        d.update_data(4, 1.2, 3)
        d.update_data(5, 1.1, 5)

        self.app(d, ["Grid OK",
                     "Legend OK",
                     "3 U phasors",
                     "3 I phasors"])

    def test_only_u(self):
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.update_data(0, 220, 0)
        d.update_data(2, 230, 4)
        self.app(d, ["Grid OK",
                     "2 U phasors"])

    def test_only_i(self):
        d = PhasorDiagramUI()
        d.add_i(3, 'i0', color=(255, 255, 0), width=2)
        d.add_i(4, 'i0', color=(255, 0, 0), width=2)
        d.update_data(3, 1, 1)
        d.update_data(4, 1.2, 3)
        self.app(d, ["Grid OK",
                     "2 I phasors"])

    def test_repeat_key(self):
        d = PhasorDiagramUI()
        d.add_u(0, 'u0')
        with self.assertRaises(ValueError):
            d.add_u(0, 'u0')

    def test_set_visible(self):
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_legend()

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)

        d.set_visible(1, False)
        d.set_visible(2, False)
        d.set_visible(2, True)

        self.app(d, ["Legend: u0, u1, u2",
                     "2 U phasors"])

    def test_remove_phasors(self):
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_legend()

        d.update_data(0, 220, 0)
        d.update_data(1, 225, 2)
        d.update_data(2, 230, 4)

        d.set_visible(1, False)
        d.remove_phasors()

        self.app(d, ["Only grid"])

    def test_remove_phasors_and_add_again(self):
        d = PhasorDiagramUI(auto_range=False)
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_legend()

        d.update_data(0, 10, 0)
        d.update_data(1, 20, 2)
        d.update_data(2, 30, 4)
        d.update_range()

        d.set_visible(1, False)
        d.remove_phasors()

        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.add_u(2, 'u2', color=(0, 255, 0), width=1)
        d.add_legend()

        d.update_data(0, 1, 0)
        d.update_data(1, 2, 2)
        d.update_data(2, 3, 4)
        d.update_range()

        self.app(d, ["No smoke"])

    def test_text(self):
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.update_data(0, 220, 0)
        d.set_text("50.01")
        self.app(d, ["Text: 50.01"])

    def test_zero_amp(self):
        d = PhasorDiagramUI()
        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.update_data(0, 0, 1)
        self.app(d, ["Only grid"])

    def test_update_range(self):
        d = PhasorDiagramUI(auto_range=False)

        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.update_data(0, 1, 0)
        d.update_range()
        d.remove_phasors()

        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.add_u(1, 'u1', color=(255, 0, 0), width=1)
        d.update_data(0, 1, 0)
        d.update_data(1, 2, 2)
        d.update_range()
        d.remove_phasors()

        d.add_u(0, 'u0', color=(255, 255, 0), width=1)
        d.update_data(0, 1, 0)
        d.update_range()

        self.app(d, ["U range is 1"])

    def test_range_ignores_unvisibles(self):
        d = PhasorDiagramUI()
        d.add_u(0)
        d.add_u(1)
        d.set_visible(1, False)
        d.update_data(0, 1, 0)
        d.update_data(1, 3, 1)
        self.app(d, ["U range is 1"])

    def test_visibility_changes_range(self):
        d = PhasorDiagramUI()
        d.add_u(0)
        d.add_u(1)
        d.set_visible(1, False)
        d.update_data(0, 1, 1)
        d.update_data(1, 3, 2)
        d.set_visible(1, True)
        self.app(d, ["U range is 3"])

    def test_all_became_unvisible(self):
        d = PhasorDiagramUI()
        d.add_u(0)
        d.update_data(0, 1, 1)
        d.set_visible(0, False)
        self.app(d, ["Ranges are 0.001"])


class Test__linestyle_to_dash(unittest.TestCase):
    def test_unknown_style(self):
        with self.assertRaises(ValueError):
            _linestyle_to_dash('some unknown', 1)
