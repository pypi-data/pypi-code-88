# Adapted from https://github.com/abalter/polyglottus/blob/master/simple_kernel.py

import queue
from jupyter_client.manager import start_new_kernel

POLL_TIME = 0.01


class SimpleKernel():
    """
    A simplistic Jupyter kernel client wrapper.

    Adapted from
    https://github.com/abalter/polyglottus/blob/master/simple_kernel.py

    :param kernel_name: string
        if no kernel is installed with this name, `jupyter_client` sends a
        NoSuchKernel error
    :param  timeout: number
        wait time before raising a TimeoutError. TimeoutError is never raised
        when calling executesilent => SimpleKernel simply waits while the code
        runs in parallel
    :param verbose: bool (default=False)
        Whether to display processing information.

    """

    # TODO: logging level
    def __init__(self, kernel_name='python3', timeout=10, verbose=False):
        """
        Initializes the `kernel_manager` and `client` objects
        and starts the kernel.

        :param kernel_name : string
            if no kernel is installed with this name, `jupyter_client` sends a
            NoSuchKernel error
        :param  timeout: number
            wait time before raising a TimeoutError. TimeoutError is never raised
            when calling executesilent => SimpleKernel simply waits while the code
            runs in parallel
        :param verbose : bool (default=False)
            Whether to display processing information.
        """
        # Initialize kernel and client
        self.kernel_manager, self.client = start_new_kernel(kernel_name=kernel_name)
        # A short POLL_TIME is used for executesilent, since we don't have to wait for
        #  the output, and execute, where we do have to wait, and if we don't, the result
        #  can not be trusted.
        self.timeout = timeout
        self.pending_jobs = 0
        # TODO: use logging module
        self.debug = lambda *args: print(*args) if verbose else lambda *args: None
        self.warning = lambda *args: print(*args)
        # end __init__ #

    def executesilent(self, code, allow_errors=False):
        r'''
        Does not collect output, but runs the code.
        It doesn't wait for the kernel to finish, but instead queues whatever code is
        left running for the next call to `executesilent` or `execute`.
        '''
        self.debug("----------------")
        self.debug("executing code: " + code)
        # msg_id = self.client.execute(code)
        self.client.execute(code)
        self.pending_jobs += 1

        # Continue polling for execution to complete
        # which is indicated by having an execution state of "idle"
        while True:
            # Poll the message in intervals of length POLL_TIME seconds
            try:
                io_msg_content = self.client.get_iopub_msg(timeout=POLL_TIME)['content']
                self.debug("io_msg content")
                self.debug(io_msg_content)
                if ('execution_state' in io_msg_content and io_msg_content['execution_state'] == 'idle'):
                    self.pending_jobs -= 1
                    self.debug('pending job recovered', self.pending_jobs)
                    if self.pending_jobs == 0:
                        return True
            except queue.Empty:
                self.debug('pending job', self.pending_jobs)
                return True

            # Check the message for various possibilities
            if 'traceback' in io_msg_content:  # Indicates jupyter kernel error
                if allow_errors:
                    return False
                else:
                    self.warning("ERROR")
                    # Put error into nice format
                    self.warning('\n'.join(io_msg_content['traceback']))
                    raise AttributeError
            elif ('data' in io_msg_content and
                  'error' in io_msg_content['data']):  # Indicates error when running code
                if allow_errors:
                    return False
                else:
                    self.warning('error')
                    self.warning(io_msg_content['data']['error'])
                    raise AttributeError

    def execute(self, code, allow_errors=False):
        """
        Executes a code string in the kernel. Returns both
        the full execution response payload, or just `stdout`.

        :param code: string
            The code string to get passed to `stdin`.

        :return: `stdout` or the full response payload.
        """
        self.debug("----------------")
        self.debug("executing code: " + code)

        # Execute the code
        msg_id = self.client.execute(code)
        self.pending_jobs += 1

        # Collect the response payload
        reply = self.client.get_shell_msg(msg_id)
        self.debug("reply content")
        self.debug(reply['content'])

        out = []

        # Continue polling for execution to complete
        # which is indicated by having an execution state of "idle"
        while True:
            # Poll the message
            try:
                io_msg_content = self.client.get_iopub_msg(timeout=self.timeout)['content']
                self.debug("io_msg content")
                self.debug(io_msg_content)
                if ('execution_state' in io_msg_content and io_msg_content['execution_state'] == 'idle'):
                    self.pending_jobs -= 1
                    self.debug('pending job recovered', self.pending_jobs)
                    if self.pending_jobs == 0:
                        break
            except queue.Empty:
                self.debug("timeout get_iopub_msg")
                raise TimeoutError

            # Check the message for various possibilities
            if 'traceback' in io_msg_content:  # Indicates error
                self.debug("ERROR")
                self.debug('\n'.join(io_msg_content['traceback']))  # Put error into nice format
                if allow_errors:
                    out.append({'error': '\n'.join(io_msg_content['traceback'])})
                else:
                    raise AttributeError
            elif ('data' in io_msg_content
                  and 'error' in io_msg_content['data']):  # Indicates error when running code
                if allow_errors:
                    return False
                else:
                    self.warning('error')
                    self.warning(io_msg_content['data']['error'])
                    raise AttributeError
            elif self.pending_jobs > 1:
                # These iopub_msg come from pending jobs which where queued from
                # calls to executesilent, which do not expect us to collect the result
                pass
            elif 'data' in io_msg_content:  # Indicates completed operation
                self.debug('has data')
                out.append(io_msg_content['data'])
            elif 'name' in io_msg_content and io_msg_content['name'] == "stdout":  # output
                self.debug('name is stdout')
                out.append({'text/plain': io_msg_content['text']})

        self.debug("----------------\n\n")
        self.debug("returning " + str(out))
        return out

    # end execute #

    def __del__(self):
        """
        Destructor. Shuts down kernel safely.
        """
        from zmq.error import ZMQError
        try:
            self.kernel_manager.shutdown_kernel()
        except (ZMQError, AttributeError):
            pass
