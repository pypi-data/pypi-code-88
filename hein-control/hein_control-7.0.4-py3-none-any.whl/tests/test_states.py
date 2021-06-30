import threading
import time
import unittest
from enum import IntEnum
from hein_control.states import (ComponentState, OperationalState, ensure_component_online, ensure_component_inactive,
                                 BadComponentState, GenericActionState)


class CustomActiveState(IntEnum):
    IDLE = 0
    ACTIVE = 1
    HYPERACTIVE = 2
    JUMP_JUMP = 3
    BOOGIE_WOOGIE = 4
    # can you tell I have a two year old?


class TestComponent(ComponentState):
    action_states = CustomActiveState

    @ensure_component_online
    def only_run_online(self):
        return

    @ensure_component_inactive
    def only_run_inactive(self):
        return


class TestComponentStates(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.lock = threading.Lock()
        cls.component_one = TestComponent('test_component1', 1)
        cls.component_two = ComponentState('test_component2', 1)
        cls.component_three = ComponentState('test_component3', 1)

    def set_and_check_state(self, component: ComponentState, attribute: str, state: IntEnum):
        """generic tester for action and operational state"""
        # test by value
        setattr(component, attribute, state.value)
        self.assertIs(getattr(component, attribute), state)
        # test by name
        setattr(component, attribute, state.name)
        self.assertIs(getattr(component, attribute), state)
        # test name capitalization support
        setattr(component, attribute, state.name.lower())
        self.assertIs(getattr(component, attribute), state)
        # test direct state setting
        setattr(component, attribute, state)
        self.assertIs(getattr(component, attribute), state)

    def set_and_check_operational_state(self, component: ComponentState, state: OperationalState):
        """tests the setting of an operational state by state, value, and name"""
        # test property setting
        self.set_and_check_state(component, 'current_operational_state', state)
        # test method updating
        component.update_operational_state(state)
        self.assertIs(component.current_operational_state, state)

    def set_and_check_action_state(self, component: ComponentState, state: OperationalState):
        """tests the setting of an active state by state, value, and name"""
        # test property setting
        self.set_and_check_state(component, 'current_action_state', state)
        # test method updating
        component.update_action_state(state)
        self.assertIs(component.current_action_state, state)

    def test_component_state_setting(self):
        """tests setting and retrieval of component states"""
        with self.lock:
            for state in OperationalState:
                self.set_and_check_operational_state(self.component_one, state)

    def test_online_only(self):
        """tests the online check decorator functionality"""
        with self.lock:
            try:
                # check that the method runs
                self.component_one.only_run_online()
                # set to offline state
                self.component_one.current_operational_state = 0
                self.assertRaises(BadComponentState, self.component_one.only_run_online)
                # set to error state
                self.component_one.current_operational_state = -1
                self.assertRaises(BadComponentState, self.component_one.only_run_online)
            finally:
                self.component_one.current_operational_state = OperationalState.ONLINE

    def test_component_activity_setting(self):
        """tests the setting of the component activity"""
        with self.lock:
            for state in GenericActionState:
                self.set_and_check_action_state(self.component_two, state)

    def test_custom_activity_setting(self):
        """tests components with custom activity support"""
        with self.lock:
            for state in CustomActiveState:
                self.set_and_check_action_state(self.component_one, state)

    def test_inactive_only(self):
        """tests the inactive-only decorator functionality"""
        with self.lock:
            try:
                # set to active state
                for state in CustomActiveState:
                    self.component_one.current_action_state = state
                    if state == 0:
                        # check that the method runs
                        self.component_one.only_run_inactive()
                    else:
                        self.assertRaises(BadComponentState, self.component_one.only_run_inactive)
            finally:
                self.component_one.current_action_state = 0

    def update_component_state(self, state):
        """sets component one to an error state after 1 second"""
        time.sleep(1)
        self.component_one.current_operational_state = state

    def get_component_state_thread(self, state: int = -1):
        """retrieves a thread which sets the first component to the specified state"""
        return threading.Thread(
            target=self.update_component_state,
            daemon=True,
            args=[state],
        )

    def test_self_waiting(self):
        """tests waiting on a component where the error flag is switched mid-wait"""
        with self.lock:
            try:
                # ensure state monitor actually sleeps
                self.component_one.components_state_monitor_sleep(0.1)
                # tests that error raises
                first_thread = self.get_component_state_thread()
                first_thread.start()
                self.assertRaises(
                    BadComponentState,
                    self.component_one.components_state_monitor_sleep,
                    2
                )

            finally:
                self.component_one.current_operational_state = 1

    def test_adjacent_waiting(self):
        """tests a wait where the error flag is flipped on another component"""
        with self.lock:
            try:
                # ensure state monitor actually sleeps
                self.component_two.components_state_monitor_sleep(0.1)
                # perform wait on another component and ensure that bad state propagates to an error
                second_thread = self.get_component_state_thread()
                second_thread.start()
                self.assertRaises(
                    BadComponentState,
                    self.component_two.components_state_monitor_sleep,
                    2
                )

            finally:
                self.component_one.current_operational_state = 1

    def test_solo_monitor(self):
        """tests a wait where a single component is monitored for an error state (ignores errors from other components"""
        with self.lock:
            try:
                # perform wait on an third component, specifically only monitoring that component
                #   component 1 is still in an error state for this test
                third_thread = self.get_component_state_thread()
                third_thread.start()
                self.component_three.components_state_monitor_sleep(
                    1.5,
                    'test_component3'
                )
            finally:
                self.component_one.current_operational_state = 1

    def test_wait_for_operational(self):
        """tests the functionality for waiting for a component to be operational"""
        with self.lock:
            try:
                # set to offline
                self.component_one.current_operational_state = 0
                thread = self.get_component_state_thread(1)
                thread.start()
                self.component_one.wait_for_component_operational_state(1)
            finally:
                self.component_one.current_operational_state = 1
