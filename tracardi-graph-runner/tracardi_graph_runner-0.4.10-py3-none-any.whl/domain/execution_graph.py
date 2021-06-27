import asyncio
import importlib
from datetime import datetime
from time import time
from typing import List
from pydantic import BaseModel
from tracardi_plugin_sdk.action_runner import ActionRunner
from .debug_call_info import DebugCallInfo
from .debug_info import DebugInfo
from .entity import Entity
from .flow_debug_info import FlowDebugInfo
from .init_result import InitResult
from .input_params import InputParams
from .action_result import ActionResult
from ..utils.dag_error import DagError, DagExecError
from .edge import Edge
from .node import Node
from .tasks_results import ActionsResults


class ExecutionGraph(BaseModel):
    graph: List[Node]
    start_nodes: list
    debug: bool = False

    @staticmethod
    def _add_to_event_loop(tasks, coroutine, port, params, edge_id) -> list:
        task = asyncio.create_task(coroutine)
        tasks.append((task, port, params, edge_id))
        return tasks

    async def _void_return(self, node):
        all_outputs = [ActionResult(port=_start_port, value=None)
                       for _start_port in node.graph.out_edges.get_start_ports()]
        if len(all_outputs) == 1:
            return all_outputs[0]
        else:
            return tuple(all_outputs)

    @staticmethod
    def _null_params(node):
        pass

    def _run_in_event_loop(self, tasks, node, params, _port, _task_result, edge_id):
        exec_result = node.object.run(**params)
        return self._add_to_event_loop(tasks, exec_result, port=_port, params=_task_result, edge_id=edge_id)

    async def run_task(self, node: Node, payload, ready_actions_results: ActionsResults):

        if isinstance(node.object, DagExecError):
            raise node.object

        tasks = []

        if node.start:

            # This is first node in graph.
            # During debugging debug nodes are removed.

            _port = "void"
            _payload = {}

            params = {"void": payload}
            tasks = self._run_in_event_loop(tasks, node, params, _port, _payload, None)

        elif node.graph.in_edges:

            # Prepare value

            for start_port, edge, end_port in node.graph.in_edges:  # type: str, Edge, str

                if not ready_actions_results.has_edge_value(edge.id):
                    # This edge is dead. Dead edges are connected to nodes that return None instead of Result object.
                    continue

                for action_result in ready_actions_results.get(edge.id, start_port):  # type: ActionResult

                    result_copy = action_result.copy(deep=True)

                    # Do not trigger fun for None values

                    params = {end_port: result_copy.value}
                    if result_copy.value is not None:

                        # Run spec with every downstream message (param)
                        # Runs as many times as downstream edges

                        tasks = self._run_in_event_loop(tasks, node, params, end_port, action_result.value, edge.id)

                    else:

                        # If downstream spec returns None. Return None for all its upstream edges
                        exec_result = self._void_return(node)
                        tasks = self._add_to_event_loop(tasks, exec_result, end_port, action_result.value, edge.id)

        # Yield async tasks results
        for task, input_port, input_params, input_edge_id in tasks:
            try:
                result = await task
            except BaseException as e:
                msg = "`{}` raised when running node `{}`. ". \
                          format(str(e), node.id) + "Check run method of `{}.{}`". \
                          format(node.module, node.className)
                raise DagExecError(msg,
                                   port=input_port,
                                   input=input_params,
                                   edge=input_edge_id)

            yield result, input_port, input_params, input_edge_id

    @staticmethod
    def _add_results(task_results: ActionsResults, node: Node, result: ActionResult) -> ActionsResults:
        for _, edge, _ in node.graph.out_edges:
            result_copy = result.copy(deep=True)
            task_results.add(edge.id, result_copy)
        return task_results

    @staticmethod
    def _get_object(node: Node, params=None) -> ActionRunner:
        module = importlib.import_module(node.module)
        task_class = getattr(module, node.className)
        if params:
            action = task_class(**params)
        else:
            action = task_class()

        return action

    def init(self, flow, flow_history, event, session, profile) -> InitResult:
        errors = []
        objects = []
        for node in self.graph:
            # Init object
            try:
                node.object = self._get_object(node, node.init)
                node.object.debug = self.debug
                node.object.event = event
                node.object.session = session
                node.object.profile = profile
                node.object.flow = flow
                node.object.flow_history = flow_history

                objects.append("{}.{}".format(node.module, node.className))
            except Exception as e:
                msg = "`{}` raised when initializing node `{}`. ".format(
                    str(e), node.id) + "Check __init__ of `{}.{}`".format(node.module, node.className)

                errors.append(msg)
                node.object = DagExecError(msg)

        return InitResult(errors=errors, objects=objects)

    @staticmethod
    def _is_result(result):
        return hasattr(result, 'port') and hasattr(result, 'value')

    def _post_process_result(self, input_port, input_params, input_edge_id, tasks_results, result,
                             node) -> ActionsResults:
        if result is not None:
            tasks_results = self._add_results(tasks_results, node, result)
        else:
            # Check if there are any ports bu no output
            if len(node.outputs) > 0:
                raise DagError(
                    "Action (Node: {}) did not return Result object though there are the following output ports open {}".format(
                        node.id, node.outputs),
                    port=input_port,
                    input=input_params,
                    edge=input_edge_id
                )

        return tasks_results

    @staticmethod
    def _get_input_params(input_port, input_params):
        if input_params and input_port:
            return InputParams(port=input_port, value=input_params)
        return None

    async def run(self, payload, flow_id) -> DebugInfo:

        actions_results = ActionsResults()
        start = time()
        debug_info = DebugInfo(
            timestamp=start,
            flow=FlowDebugInfo(id=flow_id),
            event=Entity(id="undefined")
        )

        for node in self.graph:  # type: Node

            try:

                # Skip debug nodes when not debugging
                if not self.debug and node.debug:
                    continue

                async for result, input_port, input_params, input_edge_id in \
                        self.run_task(node, payload, ready_actions_results=actions_results):

                    # Process result

                    if isinstance(result, tuple):
                        for sub_result in result:  # type: ActionResult
                            if self._is_result(sub_result) or sub_result is None:
                                actions_results = self._post_process_result(
                                    input_port,
                                    input_params,
                                    input_edge_id,
                                    actions_results,
                                    sub_result,
                                    node)
                            else:
                                raise DagError(
                                    "Action (Node: {}) did not return Result or tuple of Results. Expected Result got {}".format(
                                        node.id, type(result)),
                                    port=input_port,
                                    input=input_params,
                                    edge=input_edge_id
                                )
                    elif self._is_result(result) or result is None:
                        actions_results = self._post_process_result(
                            input_port,
                            input_params,
                            input_edge_id,
                            actions_results,
                            result,
                            node)
                    else:
                        raise DagError(
                            "Action (Node: {}) did not return Result or tuple of Results. Expected Result got {}".format(
                                node.id, type(result)),
                            port=input_port,
                            input=input_params,
                            edge=input_edge_id
                        )

                    # Save debug call info

                    call_debug_info = DebugCallInfo(
                        time=time() - start,
                        node=Entity(id=node.id),
                        edge=Entity(id=input_edge_id) if input_edge_id is not None else None,
                        init=node.init,
                        input=self._get_input_params(input_port, input_params),
                        output=[result] if self._is_result(result) else result,
                        profile=node.object.profile.dict() if isinstance(node.object, ActionRunner) else {},
                        event=node.object.event.dict() if isinstance(node.object, ActionRunner) else {},
                        session=node.object.session.dict() if isinstance(node.object, ActionRunner) else {}
                    )

                    debug_info.calls.append(call_debug_info)

            except (DagError, DagExecError) as e:

                if e.input is not None and e.port is not None:

                    call_debug_info = DebugCallInfo(
                        time=time() - start,
                        node=Entity(id=node.id),
                        edge=Entity(id=e.edge) if e.edge is not None else None,
                        init=node.init,
                        input=InputParams(port=e.port, value=e.input),
                        output=None,
                        profile=node.object.profile.dict() if isinstance(node.object, ActionRunner) else {},
                        event=node.object.event.dict() if isinstance(node.object, ActionRunner) else {},
                        session=node.object.session.dict() if isinstance(node.object, ActionRunner) else {},
                        error=str(e)
                    )

                else:

                    call_debug_info = DebugCallInfo(
                        time=time() - start,
                        node=Entity(id=node.id),
                        edge=Entity(id=e.edge) if e.edge is not None else None,
                        init=node.init,
                        input=None,
                        output=None,
                        error=str(e),
                        profile=node.object.profile.dict() if isinstance(node.object, ActionRunner) else {},
                        event=node.object.event.dict() if isinstance(node.object, ActionRunner) else {},
                        session=node.object.session.dict() if isinstance(node.object, ActionRunner) else {}
                    )

                debug_info.calls.append(call_debug_info)

        return debug_info

    def serialize(self):
        return self.dict()
