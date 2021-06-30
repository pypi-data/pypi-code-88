"""module for managing component states"""

import time
import logging

from typing import Union, MutableMapping, List, Callable, Type
from enum import IntEnum
from functools import wraps

from .mixin.reg import InstanceRegistry


logger = logging.getLogger(__name__)


class OperationalState(IntEnum):
    """
    operational state tracker for components. By convention, use 0 to indicate offline, negative values for
    error states, and positive values for online states
    """
    ERROR = -1
    OFFLINE = 0
    ONLINE = 1


class GenericActionState(IntEnum):
    """
    Basic action state tracker for component. By convention, use 0 to represent an inactive state for the inactive
    state check decorator to function.
    """
    IDLE = 0
    ACTIVE = 1


class BadComponentState(Exception):
    def __init__(self, *components: 'ComponentState', threshold_state: IntEnum):
        """
        Exception signifying that bad state was encountered on the provided components

        :param components: components which have a bad state
        :param threshold_state: threshold state
        """
        self.components = components
        super(BadComponentState, self).__init__(
            f'a bad state was encountered with the component{"s" if len(components) > 0 else ""}: ' +
            ', '.join([
                f'{component.component_name}: {component.current_operational_state.name}'
                for component in components
            ])
            + f'; threshold state: {threshold_state.name}'
        )


def ensure_component_online(fn: Callable):
    """class instance decorator which will check for an online state before executing the decorated function"""
    @wraps(fn)
    def decorated(self: 'ComponentState', *args, **kwargs):
        if self.current_operational_state <= 0:
            logger.error(
                f'the component {self.component_name} is in operational state {self.current_operational_state.name} '
                f'(required: {OperationalState.ONLINE}) '
                f'when calling {fn.__name__}'
            )
            raise BadComponentState(self, threshold_state=OperationalState.OFFLINE)
        return fn(self, *args, **kwargs)

    return decorated


def ensure_component_inactive(fn: Callable):
    """
    class instance decorator which will check that the component is inactive before
    executing the decorated function
    """
    @wraps(fn)
    def decorated(self: 'ComponentState', *args, **kwargs):
        if self.current_action_state != 0:
            # retrieve the expected idle state enumeration
            expected_idle_state = self.current_action_state.__class__(0)
            logger.error(
                f'the component {self.component_name} is in action state {self.current_action_state.name} '
                f'(required: {expected_idle_state.name}) when calling {fn.__name__}'
            )
            raise BadComponentState(self, threshold_state=expected_idle_state)
        return fn(self, *args, **kwargs)

    return decorated


class ComponentState(InstanceRegistry):

    # dedicated component-specific mapping
    _components: MutableMapping[str, 'ComponentState'] = {}

    # override this when subclassing to indicate more advanced component action states
    action_states: Type[IntEnum] = GenericActionState

    # override this when subclassing to indicate more advanced component operational states
    #   negative values indicate error states, 0 is offline, and positive is an operational state
    operational_states: Type[IntEnum] = OperationalState

    def __init__(self,
                 component_name: str,
                 current_operational_state: Union[int, str, IntEnum] = None,
                 current_action_state: Union[int, str, IntEnum] = None
                 ):
        """
        ABC for tracking a component's operational state

        :param component_name: reference name for the component being registered
        :param current_operational_state: current state of the component
        """
        # todo create an InstanceRegistry subclass which tracks subclass instances (i.e. all components)
        if component_name in ComponentState.class_registry:
            raise NameError(
                f'the component "{component_name}" is already defined, please retrieve using get_component_by_name or '
                f'choose a different name for the component'
            )
        InstanceRegistry.__init__(self)
        ComponentState._components[component_name] = self
        self.component_name = component_name
        self._current_operational_state: OperationalState = None
        self.current_operational_state = current_operational_state or 0
        self._current_action_state: IntEnum = None
        self.current_action_state = current_action_state or 0
        self.logger = logger.getChild(self.component_name)

    @staticmethod
    def _match_instance_key(inst: "ComponentState", identifier: str) -> bool:
        """matches the provided identifier against the component name and standard identifiers"""
        if inst._uuid == identifier:
            return True
        elif inst.uuid == identifier:
            return True
        elif identifier == inst.component_name:
            # todo consider matching case-insensitive
            return True
        return False

    @property
    def current_operational_state(self) -> IntEnum:
        """The current state of the component"""
        return self._current_operational_state

    @current_operational_state.setter
    def current_operational_state(self, value: Union[int, str, IntEnum]):
        self.update_operational_state(value)

    def get_operational_state_from_key(self, value: Union[int, str, IntEnum]) -> IntEnum:
        """
        Gets an operational state from the provided key. If an IntEnum instance which is not the same
        class as the assigned operational state class of the instance, the equivalent state will be retrieved.

        :param value: value, name, or IntEnum
        """
        if isinstance(value, self.operational_states):
            return value
        elif isinstance(value, IntEnum):
            try:
                return self.operational_states(value.value)
            except ValueError as e:
                raise ValueError(f'the operational state {value} does not have an equivalent {self.operational_states.__name__} value')
        elif type(value) is str:
            return getattr(self.operational_states, value.upper())
        elif type(value) is int:
            return self.operational_states(value)
        else:
            raise TypeError(f'the type {type(value)} is not supported for a current component operational state')

    def update_operational_state(self, value: Union[int, str, IntEnum]) -> IntEnum:
        """
        Updates the current state of the Component

        :param value: value to set the state to
        :return: component state
        """
        self._current_operational_state = self.get_operational_state_from_key(value)
        return self._current_operational_state

    @property
    def current_action_state(self) -> IntEnum:
        """the current action state of the component"""
        return self._current_action_state

    @current_action_state.setter
    def current_action_state(self, value: Union[int, str, IntEnum]):
        self.update_action_state(value)

    def update_action_state(self, value: Union[int, str, IntEnum]) -> IntEnum:
        """
        Updates the current action state of the component

        :param value: value to set the state to
        :return: component action state
        """
        if type(value) is int:
            value = self.action_states(value)
        elif type(value) is str:
            value = getattr(self.action_states, value.upper())
        elif isinstance(value, self.action_states) is False:
            raise TypeError(f'the type {type(value)} is not supported for a current component action state')
        self._current_action_state = value
        return self._current_action_state

    @classmethod
    def check_component_states(cls,
                               threshold_state: Union[int, OperationalState],
                               *components: Union[str, 'ComponentState'],
                               ) -> List['ComponentState']:
        """
        Checks the provided components against the minimum component state value, returning any components which do not
        pass the check.

        :param threshold_state: Minimum state value (components with states lower than this will fail the check)
        :param components: components to check
        :return: list of failing components
        """
        components = cls.get_components_to_monitor(*components)
        return [
            component
            for component in components
            if component.current_operational_state <= threshold_state
        ]

    @classmethod
    def check_component_states_raise(cls,
                                     threshold_state: Union[int, OperationalState],
                                     *components: 'ComponentState',
                                     ):
        """
        Checks the list of components against the minimum state and raises an error if any fail the test

        :param threshold_state: the threshold state to monitor for
        :param components: components to check
        """
        bad_states = cls.check_component_states(threshold_state, *components)
        if len(bad_states) > 0:
            logger.error(
                f'a bad state was encountered on the following component{"s" if len(bad_states) == 1 else ""}: '
                + ", ".join([
                    f'{component.component_name} {component.current_operational_state.value} '
                    f'({component.current_operational_state.name})'
                    for component in bad_states
                ])
            )
            raise BadComponentState(*bad_states, threshold_state=threshold_state)

    @classmethod
    def components_from_names(cls, *components: Union[str, 'ComponentState']) -> List['ComponentState']:
        """
        Retrieves a list of ComponentState subclasses from the provided list.

        :param components: components to find
        :return: list of ComponentState instances
        """
        out = []
        for component in components:
            if isinstance(component, ComponentState) is True:
                out.append(component)
            elif type(component) is str:
                out.append(cls._components[component])
            else:
                raise TypeError(f'the component "{component}" is not recognized')
        return out

    @classmethod
    def get_components_to_monitor(cls, *components: Union[str, 'ComponentState']) -> List['ComponentState']:
        """
        Gets a list of components to monitor from the provided arguments. If no components are provided, the complete
        list of components is provided.

        :param components: components to monitor
        :return: list of ComponentState instances
        """
        if len(components) > 0:
            return cls.components_from_names(*components)
        return [component for _, component in cls._components.items()]

    @classmethod
    def components_state_monitor_sleep(cls,
                                       duration: float,
                                       *components: Union[str, 'ComponentState'],
                                       cycle_time: float = 0.1,
                                       threshold_state: Union[int, IntEnum] = OperationalState.OFFLINE,
                                       ):
        """
        Executes a sleep while also monitoring the state of the specified components. If no components are provided,
        all components will be monitored.

        :param duration: duration to sleep (approximate)
        :param components: components to monitor for a bad state. Can be either the name of the component or the
            ComponentState instance itself.
        :param cycle_time: cycle frequency (s; a check for a bad state will be executed every this seconds)
        :param threshold_state: the state to monitor for (states less or equal to this will raise an error)
        """
        # retrieve components as specified
        monitored_components = cls.get_components_to_monitor(*components)
        logger.info(
            f'waiting for ~{duration} s while monitoring '
            + f'{len(monitored_components)} components'
            if len(monitored_components) > 0
            else monitored_components[0].component_name
        )
        end_time = time.time() + duration
        while time.time() < end_time:
            cls.check_component_states_raise(threshold_state, *monitored_components)
            time.sleep(cycle_time)
        logging.info(f'finished waiting, continuing')

    def state_monitor_sleep(self,
                            duration: float,
                            cycle_time: float = 0.1,
                            threshold_state: Union[int, IntEnum] = OperationalState.OFFLINE,
                            ):
        """
        Executes a sleep while also monitoring the state of the component. To monitor the state of multiple components,
        use components_state_monitor_sleep.

        :param duration: duration to sleep (approximate)
        :param cycle_time: cycle frequency (s; a check for a bad state will be executed every this seconds)
        :param threshold_state: the state to monitor for (states less or equal to this will raise an error)
        """
        return self.components_state_monitor_sleep(
            duration,
            self.component_name,
            cycle_time=cycle_time,
            threshold_state=threshold_state,
        )

    @classmethod
    def components_state_monitor_flag_check(cls,
                                            flag_check: Callable,
                                            *components: Union[str, 'ComponentState'],
                                            target_flag_state=True,
                                            cycle_time: float = 0.1,
                                            threshold_state: Union[int, IntEnum] = OperationalState.OFFLINE,
                                            **flag_check_kwargs
                                            ):
        """
        Monitors the provided flag check while also monitoring the state of the specified components. If no components
        are provided, all components will be monitored.

        :param flag_check: method which will return a value that will be checked against the target_flag_state
        :param components: components to monitor for a bad state. Can be either the name of the component or the
            ComponentState instance itself.
        :param cycle_time: cycle frequency (s; a check for a bad state will be executed every this seconds)
        :param threshold_state: the state to monitor for (states less or equal to this will raise an error)
        :param target_flag_state: target flag state to monitor for
        :param flag_check_kwargs: keyword arguments for the flag check
        """
        # retrieve components as specified
        monitored_components = cls.get_components_to_monitor(*components)
        logger.info(
            f'waiting for {flag_check.__name__} to be {target_flag_state} while monitoring '
            + f'{len(monitored_components)} components' if len(monitored_components) > 0
            else monitored_components[0].component_name
        )
        while flag_check(**flag_check_kwargs) != target_flag_state:
            cls.check_component_states_raise(threshold_state, *monitored_components)
            time.sleep(cycle_time)
            # todo add timeout
        logging.info(f'finished waiting, continuing')

    def state_monitor_flag_check(self,
                                 flag_check: Callable,
                                 target_flag_state=True,
                                 cycle_time: float = 0.1,
                                 threshold_state: Union[int, IntEnum] = OperationalState.OFFLINE,
                                 **flag_check_kwargs
                                 ):
        """
        Monitors the state of the component, waiting for the threshold state. To monitor multiple components, use
        components_state_monitor_flag_check.


        :param flag_check: method which will return a value that will be checked against the target_flag_state
        :param cycle_time: cycle frequency (s; a check for a bad state will be executed every this seconds)
        :param threshold_state: the state to monitor for (states less or equal to this will raise an error)
        :param target_flag_state: target flag state to monitor for
        :param flag_check_kwargs: keyword arguments for the flag check
        """
        self.components_state_monitor_flag_check(
            flag_check,
            self.component_name,
            target_flag_state=target_flag_state,
            cycle_time=cycle_time,
            threshold_state=threshold_state,
            **flag_check_kwargs,
        )

    @classmethod
    def get_component_by_name(cls, component_name: str) -> 'ComponentState':
        """
        Retrieves a component by its name. If you need to retrieve a component that you know is already instantiated,
        use this method.

        :param component_name: name assigned to the component
        """
        try:
            return cls._components[component_name]
        except KeyError:
            raise KeyError(f'the component "{component_name}" is not a defined component')

    @classmethod
    def get_or_create_component(cls, *args, component_name: str = None, **kwargs) -> 'ComponentState':
        """
        Retrieves an existing component or instantiates it as needed. This is intended to be the primary factory for
        component instantiation.

        :param args: component arguments
        :param component_name: name for the component
        :param kwargs: component keyword arguments
        :return: instantiated components
        """
        if component_name is None:
            raise ValueError(f'a component name must be specified')
        if component_name in cls._components:
            return cls._components[component_name]
        return cls(
            *args,
            component_name=component_name,
            **kwargs,
        )

    def wait_for_component_operational_state(self,
                                             desired_state: Union[int, IntEnum, str],
                                             cycle_time: float = 0.1,
                                             timeout: float = None,  # todo implement timeout for wait
                                             ):
        """
        Waits for the specified components to be at or above the specified operational state.

        :param desired_state: desired state for the component to be in
        :param cycle_time: state check cycle time
        """
        # todo create a generic method to wait for multiple components
        desired_state = self.get_operational_state_from_key(desired_state)
        if timeout is not None:
            max_time = time.time() + timeout
        self.logger.info(f'waiting for {desired_state.name} operational state')
        while self.current_operational_state < desired_state:
            if timeout is not None and time.time() > max_time:
                self.logger.error(
                    f'timeout of {timeout} s elapsed while waiting for {self.component_name} to be {desired_state.name}'
                )
            time.sleep(cycle_time)
