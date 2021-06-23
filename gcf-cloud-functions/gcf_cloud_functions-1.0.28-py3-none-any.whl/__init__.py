# -*- coding: utf-8 -*-
""" Utility functions to simplify Google Cloud Function implementation.

This package allows simple GCP function creation by subclassing a base Worker
and implementing it's `work` routine.

It will handle GPC max timeout, event handling in case of multiple GCP calls
to same function, error handling, state management (function can be `running`, `failed`, `success`, etc.)
and progress management - in case of resumable functions.

Example of a simple function:
    GCP simple function that will print 'Hello World!' when it's called.

    The function expects a firestore.document.create event
    that needs to be created in order to trigger the call.

    The deployment descriptor needs to account for the correct path of the
    document acting as the `start` event.

Create your function:
        >>> import firebase_admin
        ... from firebase_admin import firestore
        ...
        ... from gcf.functions import Worker
        ... from gcf.functions import Function
        ...
        ... firebase_admin.initialize_app()
        ... db = firestore.client()
        ...
        ... class Task(Worker):
        ...
        ...    def work(self):
        ...        # Add here the function implementation
        ...        print(self.get_task_name(), 'Hello World!')
        ...
        ... def trigger(data, context):
        ...    print(f"Function triggered by change to: {context.resource}.")
        ...
        ...    Function(
        ...        db=db,
        ...        event_path=context.resource.split('/documents/')[1],
        ...        worker_class=Task
        ...    ).run(timeout_seconds=540)

Deploy your function:
        >>> gcloud functions deploy task
        ...    --runtime python37
        ...    --retry
        ...    --timeout 540
        ...    --entry-point trigger
        ...    --trigger-event providers/cloud.firestore/eventTypes/document.create
        ...    --trigger-resource "projects/<YOUR_PROJECT_ID>/databases/(default)/documents/<ROOT_COLLECTION>/<ROOT_DOCUMENT>/tasks/{taskId}/events/{eventId}"

Note:
    - `task`: the name of the function as deployed in the cloud
    - `retry`: it should always be present, it will instruct GCP to retry our function in case of unwanted exceptions
    - `timeout`: set the timeout value the same here as in the run() method of the Function
    - `entry-point`: always `trigger`
    - `trigger-event`: always `providers/cloud.firestore/eventTypes/document.create`
    - `trigger-resource` should have the following logic:
        - ``tasks`` path element is the name of the collection that will hold all function executions
        - ``{taskId}`` path element is the id of the function. It can be any meaningfull name ('ingest', 'webhook', etc.)
        - ``event`` path element is the name of the collection that will hold all function invocations
        - ``{eventId}`` path element is the id of an event that will trigger the execution

Trigger your function:
        >>> import firebase_admin
        ... from firebase_admin import firestore
        ...
        ... from gcf.functions.workflow.events import TaskStartEvent
        ...
        ... firebase_admin.initialize_app()
        ... db = firestore.client()
        ...        ...
        ... def __main__():
        ...    root_path = '<ROOT_COLLECTION>/<ROOT_DOCUMENT>/tasks'
        ...
        ...    # Create a task in the root path
        ...    _, task_ref = db.collection(root_path).add({})
        ...
        ...    # Trigger the task by creating an event in it's 'events' collection
        ...    # Note: 'events' collection must be the same as the one declared above in the trigger-resource path
        ...    _, start_task_ref = task_ref.collection('events').add(TaskStartEvent().to_dict())
        
Example of data pipeline functions:

Create your dispatch function:
        >>> from typing import List
        ... 
        ... import firebase_admin
        ... from firebase_admin import firestore
        ...
        ... from gcf.functions import DispatchTask
        ... from gcf.functions import Function
        ...
        ... firebase_admin.initialize_app()
        ... db = firestore.client()
        ...
        ... class TestDispatch(DispatchTask):
        ...
        ...     def get_workflow(self) -> List[str]:
        ...        return ['task1', 'task2']
        ...
        ... def trigger(data, context):
        ...    print(f"Function triggered by change to: {context.resource}.")
        ...
        ...    Function(
        ...        db=db,
        ...        event_path=context.resource.split('/documents/')[1],
        ...        worker_class=TestDispatch
        ...    ).run(timeout_seconds=540)


Deploy your dispatch function:
        >>> gcloud functions deploy dispatch_task
        ...    --runtime python37
        ...    --retry
        ...    --timeout 540
        ...    --entry-point trigger
        ...    --trigger-event providers/cloud.firestore/eventTypes/document.create
        ...    --trigger-resource "projects/<YOUR_PROJECT_ID>/databases/(default)/documents/<ROOT_COLLECTION>/<ROOT_DOCUMENT>/dispatch_tasks/{dispatchTaskId}/events/{eventId}"

Note:
    Dispatch function will call ``task1`` and ``task2`` in this order.
    The names associated with the functions must be reused in the `workflow` tasks as described
    below.

    The firestore path above shoule be read as:
        * `projects/<YOUR_PROJECT_ID>/databases/(default)/documents/`: required by GCP.
        * `<ROOT_COLLECTION>/<ROOT_DOCUMENT>`: a path of one choosing acting as the root document for the pipeline execution.
        * `dispatch_tasks`: a collection representing the grouping of pipeline executions. Name is not important, only the presence of this document is.
        * `{dispatchTaskId}`: Document for tracking the execution state of dispacher
        * `events`: Collection of events to triggering events.
        * `{eventId}`: Document for triggering the execution.
    
    The events for the inner tasks will be generated under the same path as follows:
        * task1: ..dispatch_tasks/{dispatchTaskId}/tasks/``task1``/events/{eventId}
        * task2: ..dispatch_tasks/{dispatchTaskId}/tasks/``task2``/events/{eventId}

Trigger your dispatch function:
        >>> import firebase_admin
        ... from firebase_admin import firestore
        ...
        ... from gcf.functions.dispatch.events import DispatchStartEvent
        ...
        ... firebase_admin.initialize_app()
        ... db = firestore.client()
        ...        ...
        ... def __main__():
        ...    root_path = '<ROOT_COLLECTION>/<ROOT_DOCUMENT>/dispatch_tasks'
        ...
        ...    # Create a task in the root path
        ...    _, task_ref = db.collection(root_path).add({})
        ...
        ...    # Trigger the task by creating an event in it's 'events' collection
        ...    # Note: 'events' collection must be the same as the one declared above in the trigger-resource path
        ...    _, start_task_ref = task_ref.collection('events').add(DispatchStartEvent().to_dict())

Create your workflow function:
        >>> import firebase_admin
        ... from firebase_admin import firestore
        ...
        ... from gcf.functions import WorkflowTask
        ... from gcf.functions import Function
        ...
        ... firebase_admin.initialize_app()
        ... db = firestore.client()
        ...
        ... class Task1(WorkflowTask):
        ...
        ...    def get_task_name(self) -> str:
        ...        return 'task1'
        ...
        ...    def work(self):
        ...        print(self.get_task_name(), 'done')
        ...
        ... def trigger(data, context):
        ...    print(f"Function triggered by change to: {context.resource}.")
        ...
        ...    Function(
        ...        db=db,
        ...        event_path=context.resource.split('/documents/')[1],
        ...        worker_class=Task1
        ...    ).run(timeout_seconds=540)

Note:
    Here the task name as returned by `get_task_name` must be ``task1``. It must
    have the same name as declared in the dispatch workflow.

    You can have as many tasks as you need, they will all be called in the
    order they are defined in the dispatcher.

    If any of of them returns with status ``failed`` the dispatcher
    will stop the data pipline.

Deploy your workflow function:
        >>> gcloud functions deploy task_1
        ...    --runtime python37
        ...    --retry
        ...    --timeout 540
        ...    --entry-point trigger
        ...    --trigger-event providers/cloud.firestore/eventTypes/document.create
        ...    --trigger-resource "projects/<YOUR_PROJECT_ID>/databases/(default)/documents/<ROOT_COLLECTION>/<ROOT_DOCUMENT>/dispatch_tasks/{dispatchTaskId}/tasks/task1/events/{eventId}"

Note:
    Here the task name as part of firestore document path must be ``task1``.


"""

__version__ = "1.0.28"
