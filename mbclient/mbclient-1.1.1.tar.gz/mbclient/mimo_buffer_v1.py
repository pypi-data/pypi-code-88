"""
Grundlegende Idee
"""
import numpy as np
from multiprocessing import shared_memory, Lock, SimpleQueue, Event
import threading
import heapq
import time


class Reader:
    """
    Thin client class initialized in each worker process.
    Grants access to single ring buffer objects without exposing the underlying management complexity.
    Interfaces with the buffer manager process.
    """

    def __init__(self, setup_dict):
        self.init_dict = setup_dict
        # Get buffer
        self.number_of_slots = setup_dict["number_of_slots"]
        self.values_per_slot = setup_dict["values_per_slot"]
        self.dtype = setup_dict["dtype"]
        self._m_share = shared_memory.SharedMemory(name=setup_dict["mshare_name"])
        array_shape = (self.number_of_slots, self.values_per_slot)
        self._buffer = np.ndarray(shape=array_shape, dtype=self.dtype, buffer=self._m_share.buf)
        self._metadata_share = shared_memory.SharedMemory(name=setup_dict["metadata_share_name"])
        metadata_dtype = [('timestamp', np.int), ('counter', np.int)]
        self._metadata = np.ndarray(shape=self.number_of_slots, dtype=metadata_dtype, buffer=self._metadata_share.buf)

        # Get queues
        self._todo_queue = setup_dict["todo_queue"]
        self._done_queue = setup_dict["done_queue"]

        # Setup class status variables
        self._last_get_index = -1
        self._active = setup_dict["active"]

    def __del__(self):
        # Clean up queue
        if self._last_get_index != -1:
            self._done_queue.put(self._last_get_index)
        # Clean up memory share
        del self._buffer
        self._m_share.close()

    def get(self):
        if self._last_get_index != -1:
            self._done_queue.put(self._last_get_index)
        self._last_get_index = self._todo_queue.get()
        if not self._active.is_set():
            raise SystemExit
        return self._buffer[self._last_get_index, :]

    def get_metadata(self):
        if self._last_get_index != -1:
            timestamp = self._metadata[self._last_get_index]['timestamp']
            counter = self._metadata[self._last_get_index]['counter']
            return timestamp, counter
        else:
            return -1, 0


class Writer:
    """
    TODO: DOCSTRING
    """

    def __init__(self, setup_dict):
        self.init_dict = setup_dict
        # Get buffer
        self.number_of_slots = setup_dict["number_of_slots"]
        self.values_per_slot = setup_dict["values_per_slot"]
        self.dtype = setup_dict["dtype"]
        self._m_share = shared_memory.SharedMemory(name=setup_dict["mshare_name"])
        array_shape = (self.number_of_slots, self.values_per_slot)
        self._buffer = np.ndarray(shape=array_shape, dtype=self.dtype, buffer=self._m_share.buf)
        self._metadata_share = shared_memory.SharedMemory(name=setup_dict["metadata_share_name"])
        metadata_dtype = [('timestamp', np.int), ('counter', np.int)]
        self._metadata = np.ndarray(shape=self.number_of_slots, dtype=metadata_dtype, buffer=self._metadata_share.buf)

        # Get queues
        self._empty_queue = setup_dict["empty_queue"]
        self._filled_queue = setup_dict["filled_queue"]

        # Setup class status variables
        self._current_buffer_index = -1
        self._write_counter = 0
        self._active = setup_dict["active"]
        self.start_time = time.time_ns()

    def __del__(self):
        # Clean up queue
        if self._current_buffer_index != -1:
            self._filled_queue.put(self._current_buffer_index)
        # Clean up memory share
        del self._buffer
        self._m_share.close()

    def get_new_buffer(self):
        if self._current_buffer_index != -1:
            self.process_buffer()
        # TODO: Handle buffer underflow (as of Python 3.8 multiprocessing.SimpleQueue.get() always blocks!)
        self._current_buffer_index = self._empty_queue.get()
        if not self._active.is_set():
            raise SystemExit
        self._metadata[self._current_buffer_index]['timestamp'] = -1
        self._metadata[self._current_buffer_index]['counter'] = self._write_counter
        self._write_counter += 1
        return self._buffer[self._current_buffer_index, :]

    def set_metadata(self, timestamp, counter):
        self._metadata[self._current_buffer_index]['timestamp'] = timestamp
        self._metadata[self._current_buffer_index]['counter'] = counter

    def process_buffer(self):
        if self._current_buffer_index != -1:
            if self._metadata[self._current_buffer_index]['timestamp'] == -1:
                self._metadata[self._current_buffer_index]['timestamp'] = np.int((time.time_ns() - self.start_time)//1000)
            self._filled_queue.put(self._current_buffer_index)
            self._current_buffer_index = -1


class Observer:
    """
    Thin client class initialized in each worker process.
    Grants access to a copy of the newest ring buffer object without exposing the underlying management complexity.
    Interfaces with the buffer manager process like a normal reader
    """

    def __init__(self, setup_dict):
        self.init_dict = setup_dict
        # Get buffer
        self.number_of_slots = setup_dict["number_of_slots"]
        self.values_per_slot = setup_dict["values_per_slot"]
        self.dtype = setup_dict["dtype"]
        self._m_share = shared_memory.SharedMemory(name=setup_dict["mshare_name"])
        array_shape = (self.number_of_slots, self.values_per_slot)
        self._buffer = np.ndarray(shape=array_shape, dtype=self.dtype, buffer=self._m_share.buf)
        self._copy_buffer = np.array(self.values_per_slot, dtype=self.dtype)

        # Get queues
        self._todo_queue = setup_dict["todo_queue"]
        self._done_queue = setup_dict["done_queue"]

        # Setup class status variables
        self._last_get_index = -1
        self._active = setup_dict["active"]

        # Setup internal thread structures
        self._copy_lock = threading.Lock()
        self._new_element = threading.Event()
        self._loop_thread = threading.Thread(target=self._get_newest_element_loop)
        self._loop_thread.start()

    def __del__(self):
        # Todo: remove print or change to logger
        self._loop_thread.join()
        # Clean up Get()-event
        self._new_element.set()
        # Clean up queue
        if self._last_get_index != -1:
            self._done_queue.put(self._last_get_index)
        while not self._todo_queue.empty():
            self._done_queue.put(self._todo_queue.get())
        # Clean up memory share
        del self._buffer
        self._m_share.close()

    def _get_newest_element_loop(self):
        while self._active.is_set():
            # This call will block until there is a new element
            new_index = self._todo_queue.get()
            # Make sure the current index isn't copied right now
            with self._copy_lock:
                # Immediately release the last index we got
                if self._last_get_index != -1:
                    self._done_queue.put(self._last_get_index)
                self._last_get_index = new_index
            # Signal the get() method fresh data is available (it blocks if called too soon)
            self._new_element.set()
        # If self._active() is not set anymore (aka: bm closed all readers), exit everything
        raise SystemExit

    def get(self):
        self._new_element.wait()
        self._new_element.clear()
        if not self._active.is_set():
            raise SystemExit
        with self._copy_lock:
            self._copy_buffer = np.array(self._buffer[self._last_get_index, :], copy=True)
        return self._copy_buffer


class NewBuffer:
    """
    Buffer manager running in the host/parent process. Has to be called before launching the worker processes.
    Creates all the necessary memory shares, queues, etc and keeps track of different worker groups like writers,
    readers, observers.
    Currently implements a 'strict' (not possible with multiple writers due to race conditions) FIFO ring buffer
    """

    def __init__(self, number_of_slots, values_per_slot, dtype, debug=False):
        """
        Method to initially create the shared memory buffer and all other prerequisites.
        This function has to be called ONCE and ONLY ONCE for each distinct ring buffer.
        """
        # TODO: Change naive print to logger
        # print(" > Creating MimoRingBuffer")
        self.debug = debug
        # Create memory share
        self.number_of_slots = number_of_slots
        self.values_per_slot = values_per_slot
        self.dtype = dtype
        m_bytes = number_of_slots * values_per_slot * np.dtype(dtype).itemsize
        self.m_share = shared_memory.SharedMemory(create=True, size=m_bytes)
        self.metadata_dtype = [('timestamp', np.int_), ('counter', np.int)]
        m_bytes = number_of_slots * np.dtype(self.metadata_dtype).itemsize
        self.m_metadata_share = shared_memory.SharedMemory(create=True, size=m_bytes)

        # Setup queues
        # > Queue with all EMPTY memory slots ready to be used by a writer (implicitly kept in order)
        self.writer_empty_queue = SimpleQueue()
        for i in range(self.number_of_slots):
            self.writer_empty_queue.put(i)
        # > Queue with all freshly FILLED memory slots. Will be redistributed to each reader group queue
        self.writer_filled_queue = SimpleQueue()
        # > List containing the 'to do'-queues of all reader groups. Each queue contains elements ready to be processed
        self.reader_todo_queue_list = []
        # > List containing the 'done'-queues of all reader groups. Each queue contains elements ready to be overwritten
        self.reader_done_queue_list = []
        # > List containing the 'done'-heaps of all reader groups.
        self.reader_done_heap_list = []
        # > List containing the 'to do'-queues of all OBSERVERS
        self.observer_todo_queue_list = []

        # Setup threading lock
        self.read_pointer_lock = Lock()  # Lock to synchronise self.read_pointer manipulations
        self.write_pointer_lock = Lock()  # Lock to synchronise self.write_pointer access
        self.heap_lock = Lock()  # Lock to synchronise manipulations on the reader group 'done'-heaps

        # Setup pointer
        self.read_pointer = 0  # Pointer referencing the oldest element that is currently worked on by any reader
        self.write_pointer = 0  # Pointer referencing the newest element added to the buffer CAUTION: might be wrong at startup

        # Setup events for a graceful shutdown
        self.writers_active = Event()
        self.writers_active.set()
        self.observers_active = Event()
        self.observers_active.set()
        self.readers_active = Event()
        self.readers_active.set()

        # Setup filled buffer dispatcher
        self._writer_queue_thread = threading.Thread(target=self.writer_queue_listener)
        self._writer_queue_thread.start()
        self.writer_created = False
        self.reader_queue_listener_thread_list = []

    def new_reader_group(self):
        # Temporary fix to prevent 'new reader after write' problem
        assert self.writer_created is False, "All readers must be created before the first writer is created!"
        # Create basic data structure
        done_queue = SimpleQueue()  # Queue containing elements a worker process is done processing with
        todo_queue = SimpleQueue()  # Queue containing elements ready to be processed next
        self.reader_todo_queue_list.append(todo_queue)
        self.reader_done_queue_list.append(done_queue)
        # > Heap the 'done'-queue gets flushed into. Used to keep 'self.writer_empty_queue' in order
        done_heap = []
        # TODO: Manage "new reader after write" problem by prefilling the heap
        self.reader_done_heap_list.append(done_heap)
        # Start thread to listen on queue (in lack of an event driven queue implementation)
        queue_listener = threading.Thread(target=self.reader_queue_listener, args=(done_queue, done_heap))
        queue_listener.start()
        self.reader_queue_listener_thread_list.append(queue_listener)
        setup_dict = {"number_of_slots": self.number_of_slots, "values_per_slot": self.values_per_slot,
                      "dtype": self.dtype, "mshare_name": self.m_share.name,
                      "metadata_share_name": self.m_metadata_share.name,
                      "todo_queue": todo_queue, "done_queue": done_queue,
                      "active": self.readers_active}
        return setup_dict

    def reader_queue_listener(self, done_queue, done_heap):
        """
        This method runs in a separate thread for each reader group and handles dispatching free ring buffer slots
        :param done_queue: the multiprocessing.queue created in 'new_reader_group()'
        :param done_heap: the heap created in 'new_reader_group()'
        """
        while self.readers_active.is_set():
            last_index = done_queue.get()
            if not self.readers_active.is_set():
                if self.debug:
                    print("Reader dispatcher closed...")
                raise SystemExit
            with self.heap_lock:
                with self.read_pointer_lock:
                    if last_index < self.read_pointer:
                        last_index += self.number_of_slots
                heapq.heappush(done_heap, last_index)
                self.increment_reader_pointer()
        if self.debug:
            print("Reader dispatcher closed...")

    def increment_reader_pointer(self):
        """
        For this function to work properly and without race conditions self.heap_lock has to be acquired BEFORE entering
        the function!
        """
        # Check if every reader group is done with the last element (this implicitly keeps the write queue in the right
        # order at the cost of possible buffer overruns if one reader hangs/takes too long to process the data)
        pop_last_element = True
        with self.read_pointer_lock:
            for reader_heap in self.reader_done_heap_list:
                try:
                    if reader_heap[0] != self.read_pointer:
                        pop_last_element = False
                        break
                except IndexError as err:
                    pop_last_element = False
                    pass
            if pop_last_element:
                if self.debug:
                    with self.write_pointer_lock:
                        print("?> pop last element: {:d} (writer right now: {:d})".format(self.read_pointer,
                                                                                          self.write_pointer))
                    for reader_heap in self.reader_done_heap_list:
                        print(reader_heap)
                for reader_heap in self.reader_done_heap_list:
                    heapq.heappop(reader_heap)
                self.writer_empty_queue.put(self.read_pointer)
                self.read_pointer += 1
                # Handle "lapping" the ring buffer
                if self.read_pointer >= self.number_of_slots:
                    if self.debug:
                        print("?> BUFFER IS LAPPING. {:d} -> {:d}".format(self.read_pointer, self.write_pointer))
                    self.read_pointer -= self.number_of_slots
                    for reader_heap in self.reader_done_heap_list:
                        for i in range(len(reader_heap)):
                            if reader_heap[i] >= self.number_of_slots:
                                reader_heap[i] -= self.number_of_slots
                        heapq.heapify(reader_heap)
                    with self.write_pointer_lock:
                        if self.write_pointer > self.number_of_slots:
                            self.write_pointer = self.write_pointer % self.number_of_slots
                        else:
                            self.write_pointer = 0
                        if self.debug:
                            print("?>               NOW: {:d} -> {:d}".format(self.read_pointer, self.write_pointer))
        if pop_last_element:
            self.increment_reader_pointer()

    def writer_queue_listener(self):
        while self.writers_active.is_set():
            new_data_index = self.writer_filled_queue.get()
            if new_data_index is not None:
                with self.write_pointer_lock:
                    if new_data_index < self.read_pointer:
                        self.write_pointer = max(new_data_index+self.number_of_slots, self.write_pointer)
                    else:
                        self.write_pointer = max(new_data_index, self.write_pointer)
            for reader_queue in self.reader_todo_queue_list:
                reader_queue.put(new_data_index)

    def new_writer(self):
        self.writer_created = True
        setup_dict = {"number_of_slots": self.number_of_slots, "values_per_slot": self.values_per_slot,
                      "dtype": self.dtype, "mshare_name": self.m_share.name,
                      "metadata_share_name": self.m_metadata_share.name,
                      "empty_queue": self.writer_empty_queue, "filled_queue": self.writer_filled_queue,
                      "active": self.writers_active}
        return setup_dict

    def new_observer(self):
        # An observer is just a reader, so create a reader object...
        setup_dict = self.new_reader_group()
        # ... but exchange the shutdown signal, so the observer does not indefinitely reserve the last element
        setup_dict["active"] = self.observers_active
        self.observer_todo_queue_list.append(setup_dict["todo_queue"])
        return setup_dict

    def fill_status(self):
        with self.read_pointer_lock:
            actually_read = self.read_pointer - 1
        with self.write_pointer_lock:
            actually_written = self.write_pointer

        if actually_written >= actually_read:
            return actually_written - actually_read
        else:
            return self.number_of_slots - actually_read + actually_written

    def shutdown(self):
        last_element_index = self.writer_empty_queue.get()
        self.writers_active.clear()
        # Observers have to be cleared extra, because they won't release the last resource until they get something new
        self.observers_active.clear()
        time.sleep(0.1)
        latest_observed_index = last_element_index - 1
        if latest_observed_index < 0:
            latest_observed_index = self.number_of_slots
        for q in self.observer_todo_queue_list:
            q.put(latest_observed_index)
        # Wait for readers to finish their queue
        while self.read_pointer != last_element_index:
            # TODO: change to logger or remove!
            print("DEBUG: Shutdown is waiting for processing to end!\n"
                  "  active slot: {:d}, target: {:d}".format(self.read_pointer, last_element_index))
            time.sleep(0.5)
        self.readers_active.clear()
        # Now quit all reader processes (they are currently all blocking and waiting on the reader_todo_queue)
        wait_shutdown = True
        while wait_shutdown:
            wait_shutdown = False
            for q in self.reader_todo_queue_list:
                if q.empty():
                    wait_shutdown = True
                    q.put(None)
            time.sleep(0.1)
        # And quit the reader threads waiting to dispatch new data
        for q in self.reader_done_queue_list:
            q.put(None)
        # And quit the writer dispatcher thread
        self.writer_filled_queue.put(None)

    def __del__(self):
        self._writer_queue_thread.join()
        for t in self.reader_queue_listener_thread_list:
            t.join()
        self.m_share.close()
        self.m_share.unlink()
