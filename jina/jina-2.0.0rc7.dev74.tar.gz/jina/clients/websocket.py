"""A module for the websockets-based Client for Jina."""
import asyncio
from abc import ABC
from contextlib import nullcontext
from typing import Callable, Optional

from .base import BaseClient, InputType
from .grpc import GRPCClient
from .helper import callback_exec
from ..importer import ImportExtensions
from ..logging.profile import TimeContext, ProgressBar
from ..types.request import Request


class WebSocketClientMixin(BaseClient, ABC):
    """A MixIn for Websocket Client."""

    async def _get_results(
        self,
        inputs: InputType,
        on_done: Callable,
        on_error: Optional[Callable] = None,
        on_always: Optional[Callable] = None,
        **kwargs,
    ):
        """
        :meth:`send_requests()`
            Traverses through the request iterator
            Sends each request & awaits :meth:`websocket.send()`
            Sends & awaits `byte(True)` to acknowledge request iterator is empty
        Traversal logic:
            Starts an independent task :meth:`send_requests()`
            Awaits on each response from :meth:`websocket.recv()` (done in an async loop)
            This makes sure client makes concurrent invocations
        Await exit strategy:
            :meth:`send_requests()` keeps track of num_requests sent
            Async recv loop keeps track of num_responses received
            Client exits out of await when num_requests == num_responses

        :param inputs: the callable
        :param on_done: the callback for on_done
        :param on_error: the callback for on_error
        :param on_always: the callback for on_always
        :param kwargs: kwargs for _get_task_name and _get_requests
        :yields: generator over results
        """
        with ImportExtensions(required=True):
            import websockets

        self.inputs = inputs

        req_iter = self._get_requests(**kwargs)
        try:
            # setting `max_size` as None to avoid connection closure due to size of message
            # https://websockets.readthedocs.io/en/stable/api.html?highlight=1009#module-websockets.protocol

            async with websockets.connect(
                f'ws://{self.args.host}:{self.args.port_expose}/',
                max_size=None,
                ping_interval=None,
            ) as websocket:
                # To enable websockets debug logs
                # https://websockets.readthedocs.io/en/stable/cheatsheet.html#debugging
                self.logger.success(
                    f'connected to the gateway at {self.args.host}:{self.args.port_expose}!'
                )
                self.num_requests = 0
                self.num_responses = 0

                async def _send_requests(request_iterator):
                    next_request = None
                    for next_request in request_iterator:
                        await websocket.send(next_request.SerializeToString())
                        self.num_requests += 1
                    # Check if there was any request generated
                    if next_request is not None:
                        # Server has no way of knowing when to stop the await on sending response back to the client
                        # We send one last message to say `request_iterator` is completed.
                        # On the client side, this :meth:`send` doesn't need to be awaited with a :meth:`recv`
                        await websocket.send(bytes(True))
                    else:
                        # There is nothing to send, disconnect gracefully
                        await websocket.close(reason='No data to send')

                if self.args.show_progress:
                    cm1, cm2 = ProgressBar(), TimeContext('')
                else:
                    cm1, cm2 = nullcontext(), nullcontext()

                with cm1 as p_bar, cm2:
                    # Unlike gRPC, any arbitrary function (generator) cannot be passed via websockets.
                    # Simply iterating through the `req_iter` makes the request-response sequential.
                    # To make client unblocking, :func:`send_requests` and `recv_responses` are separate tasks

                    asyncio.create_task(_send_requests(request_iterator=req_iter))
                    async for response_bytes in websocket:
                        # When we have a stream of responses, instead of doing `await websocket.recv()`,
                        # we need to traverse through the websocket to recv messages.
                        # https://websockets.readthedocs.io/en/stable/faq.html#why-does-the-server-close-the-connection-after-processing-one-message

                        resp = Request(response_bytes)
                        resp = resp.as_typed_request(resp.request_type).as_response()
                        callback_exec(
                            response=resp,
                            on_error=on_error,
                            on_done=on_done,
                            on_always=on_always,
                            continue_on_error=self.args.continue_on_error,
                            logger=self.logger,
                        )
                        if self.args.show_progress:
                            p_bar.update(self.args.request_size)
                        yield resp
                        self.num_responses += 1
                        if self.num_requests == self.num_responses:
                            break

        except websockets.exceptions.ConnectionClosedOK:
            self.logger.warning(f'Client got disconnected from the websocket server')
        except websockets.exceptions.WebSocketException as e:
            self.logger.error(
                f'Got following error while streaming requests via websocket: {e!r}'
            )


class WebSocketClient(GRPCClient, WebSocketClientMixin):
    """A Python Client to stream requests from a Flow with a REST Gateway.

    :class:`WebSocketClient` shares the same interface as :class:`Client` and provides methods like
    :meth:`index`, "meth:`search`, :meth:`train`, :meth:`update` & :meth:`delete`.

    It is used by default while running operations when we create a `Flow` with `restful=True`

    .. highlight:: python
    .. code-block:: python

        from jina.flow import Flow
        f = Flow(protocol='websocket').add().add()

        with f:
            f.index(['abc'])


    :class:`WebSocketClient` can also be used to run operations for a remote Flow

    .. highlight:: python
    .. code-block:: python

        # A Flow running on remote
        from jina.flow import Flow
        f = Flow(protocol='websocket', port_expose=34567).add().add()

        with f:
            f.block()

        # Local WebSocketClient running index & search
        from jina.clients import WebSocketClient

        client = WebSocketClient(...)
        client.index(...)
        client.search(...)


    :class:`WebSocketClient` internally handles an event loop to run operations asynchronously.
    """
