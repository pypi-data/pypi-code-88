from gcf.functions.execution.execution import TransactionalExecutionHandler
from gcf.functions.execution.config import ExecutionStatus


class TaskExecutionHandler(TransactionalExecutionHandler):

    def set_execution_state(self) -> bool:
        # -- IMPORTANT --
        # Inside a transaction reads must go before writes

        old_status = self.event.parent_data.get('status', ExecutionStatus.WAITING_EXECUTION)
        new_status = old_status

        allow_execution = old_status in [ExecutionStatus.WAITING_EXECUTION,
                                         ExecutionStatus.WAITING_RETRY,
                                         ExecutionStatus.WAITING_SLEEP]

        if old_status in [ExecutionStatus.WAITING_EXECUTION, ExecutionStatus.WAITING_RETRY]:
            new_status = ExecutionStatus.RUNNING
            self.transaction.update(self.event.parent_ref, {'status': new_status})

        if old_status == ExecutionStatus.WAITING_SLEEP:
            new_status = ExecutionStatus.SLEEP
            self.transaction.update(self.event.parent_ref, {'status': new_status})

        # -- DEBUGGING --

        invocation = {
            'old_status': old_status,
            'new_status': new_status,
            'allow_execution': allow_execution,
        }

        self.event.add_invocation(invocation)

        return allow_execution
