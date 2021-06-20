# -*- coding: utf-8 -*-
"""Event handler for function execution.

The handler will prevent executions of the function based on the following logic
    * if the event is already handled it won't allow it.
    * if the event is not handled, it will mark the state of the document as `running` and mark the event as `handled`.

The worker assigned for this event will only run if the `state` is `running`.
"""

from gcf.functions.execution.execution import TransactionalExecutionHandler
from gcf.functions.execution.config import ExecutionStatus


class DispatchExecutionHandler(TransactionalExecutionHandler):

    def set_execution_state(self) -> bool:
        """ Manages execution state.

        Used for event handling and to prevent unwanted execution:
            * if the event is already handled it won't allow execution.
            * if the event is not handled, it will mark the state of the document as `running` and mark the event as `handled`.

        Returns:
            Whether the execution is allowed or not.
        """

        is_handled = self.event.is_handled
        old_status = self.event.parent_data.get('status', ExecutionStatus.WAITING_EXECUTION)

        allow_execution = True
        if old_status == ExecutionStatus.RUNNING:
            allow_execution = False
        if is_handled:
            allow_execution = False
        
        if allow_execution:
            self.transaction.update(self.event.parent_ref, {'status': ExecutionStatus.RUNNING})

        return allow_execution
