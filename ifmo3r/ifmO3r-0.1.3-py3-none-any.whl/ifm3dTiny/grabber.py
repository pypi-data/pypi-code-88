"""
Author: ifm CSR

This is a helper script: it contains the grabber class which can be imported in other scripts.

To use this class:
:FrameGrabber   :   Connects to the camera head for receiving a frame
:ImageBuffer    :   Is used to save the image data from the Framegrabber-Object and make
                    images retrievable

Simple use case:
    from ifmO3r.ifm3dTiny import Device
    dev = Device(ip, port)
    fg = FrameGrabber(dev)
    im = ImageBuffer()

    fg.wait_for_frame(im,1)
    print(im.amplitude_image())
    print(im.distance_image())
    print(im.xyz_image())
"""
# %%
import pickle
import os
import threading
import numpy as np
from ifmO3r.pcic import ImageClient, ImageClient2D
from ifmO3r.ifm3dTiny.utils import GetCallableMethods, ifm3dTinyExceptions, StatusLogger
from ifmO3r import o3ralgo
import ctypes as ct
import socket


# %%
DEFAULT_IMAGE_STACK_DEPTH = 10  # Arbitrary number
DEFAULT_TIMEOUT = 5  # Timeout in sec.
DEFAULT_TIMEOUT_LIVE = 30

# %%
class FrameGrabber:
    """
    Use the framegrabber to retrieve a frame from a head (2D or 3D).
    """

    def __init__(self, device):
        """
        :device         :   Device class, uses IP,PORT
        :_type:         :   "2D"/"3D" - Define 2D imager or 3D imager - will be deprecated in the future
        """
        self.im_type = device.im_type

        self.device = self._Connection2D(device.ip,device.port) if(self.im_type == '2d') \
            else self._Connection(device.ip, device.port)
        
        self.run = False

        self.logger = StatusLogger('grabber')

        self.exc = None

    def __str__(self):
        """
        Provide a list of *public* functions to be used by the user.

        :return:str_method_list     :   String representing a list of functions
        """
        str_method_list = GetCallableMethods().get_methods(self)
        return str_method_list

    def __timeout(self):
        try:
            self.logger.critical(format(ifm3dTinyExceptions.Timeout()))
            raise ifm3dTinyExceptions.Timeout()
        except ifm3dTinyExceptions.Timeout as e:
            # Catching exception to propagate it to the main thread
            self.exc = e


    def wait_for_frame(self, image_buffer, timeout):
        """
        Uses the device object within a context manager for establishing a connection.
        Provides only one single frame. Do not use this for streaming data.

        The module threading is used to create a timer thread and call the
        __timeout after 'n' amount of seconds. Raising an exception if the timer
        is not canceld before. See following description:
        https://realpython.com/intro-to-python-threading/

        :imageBuffer        :   ImageBuffer-Object (Class) responsible for saving/accessing the
                                image data within the frame
        :timeout (sec.)     :   Timeout for the receiving of a frame
        """

        if timeout is None:
            timeout = DEFAULT_TIMEOUT

        if image_buffer.im_type is None:
            image_buffer.im_type = self.im_type

        self.thread_timeout = threading.Timer(timeout, self.__timeout)
        self.thread_timeout.start()  # Start the timeout

        if self.run is False:
            with self.device as port:
                frame = port.device.readNextFrame()
                image_buffer.frame = frame
                # If data was received, timeout thread will be stopped before raising an exception
                self.thread_timeout.cancel()
                # Propagating a potential exception
                if self.exc != None:
                    raise self.exc
                return True
        else:
            self.logger.info(format(ifm3dTinyExceptions.StreamingMultipleQueues()))
            raise ifm3dTinyExceptions.StreamingMultipleQueues()

    def stream_on(self, image_buffer, timeout):
        """
        This function starts _stream_frame as a thread and if called again, cancels
        this thread too.

        :imageBuffer        :   ImageBuffer-Object (Class) responsible for saving/accessing
                                the image data within the frame
        :timeout (sec.)     :   Timeout for the receiving of a frame
        """
        self.exc = None 

        if timeout is None:
            timeout = DEFAULT_TIMEOUT_LIVE
            
        if image_buffer.im_type is None:
            image_buffer.im_type = self.im_type


        if self.run is False:
            self.run = True
            self.thread_stream = threading.Thread(
                target=self._stream_frame, args=(image_buffer, timeout), daemon=True
            )

            self.thread_stream.start()
            # Wait until first frame is received before returning
            while True:
                next(image_buffer)
                if image_buffer.frame != None:
                    break
            return True
        else:
            self.run = False  # Deactivate the while True within _stream_frame
            self.thread_stream.join()  # Block the program until the thread is closed
            return False



    def _stream_frame(self, image_buffer, timeout):
        """
        This function opens a connection via FrameGrabber() and receives always the
        next frame. Instead of overwriting the frame within ImageBuffer() it is using
        an image stack within ImageBuffer().
        It will trigger a timeout error if no frame is received before the end of the defined timeout.

        :imageBuffer        :   ImageBuffer-Object (Class) responsible for saving/accessing the image data within the frame
        :timeout (sec.)     :   Timeout for the receiving of a frame
        """
        if timeout is None:
            timeout = DEFAULT_TIMEOUT_LIVE

        thread_timeout = threading.Timer(timeout, self.__timeout)
        thread_timeout.start()  # Start the timeout

        with self.device as port:
            while self.run is True:  # run is toggled via stream_on
                frame = port.device.readNextFrame()
                image_buffer._push(frame)
                thread_timeout.cancel()
                # Propagate exception
                if self.exc != None:
                    raise self.exc
        return True

    class _Connection:
        """
        This object is taking care of the connection to the 3D head (ImagerClient)
        """ 

        def __init__(self, ip="192.168.0.69", port=50012):
            """
            :ip             :   IP Address of the head -  default:192.168.0.69
            :port           :   Port of the head - default: 50010
            """
            self.ip = ip
            self.port = port

        def __enter__(self):
            """
            Used for the context manager
            Opens a TCP/IP connection via ImageClient to the defined ip/port
            """
            self.device = ImageClient(self.ip, self.port, True)
            return self

        def __exit__(self, exc_t, exc_v, trace):
            """
            Used for the context manager
            Closes the TCP/IP connection
            """
            self.device.close()

    class _Connection2D:
        """
        This object is taking care of the connection to the 2D Imager - It will be
        deprecated in the future. It is based on the
        example: https://gitlab.dev.ifm/syntron/support/csr/o3d3xx-python/-/blob/o3r/examples/ov9782serverReadout.py#L47
        """

        def __init__(self, ip="192.168.0.69", port=50020):
            """
            :ip             :   IP Address of the head -  default:192.168.0.69
            :port           :   Port of the head - default: 50020
            """
            self.ip = ip
            self.port = port

        def __enter__(self):
            """
            Used for the context manager
            Opens a TCP/IP connection via ImageClient to the defined ip/port
            """
            self.device = ImageClient2D(self.ip, self.port)
            return self

        def __exit__(self, exc_t, exc_v, trace):
            """
            Used for the context manager
            Closes the TCP/IP connection
            """
            self.device.close()

        
# %%
class ImageBuffer:
    """
    Use the ImageBuffer as an object for saving the frame/images received by the FrameGrabber.
    When streaming images, the frames are added to a stack.
    """

    def __init__(self, image_stack_length=None):

        if image_stack_length is None:
            image_stack_length = DEFAULT_IMAGE_STACK_DEPTH

        from collections import deque

        self.image_stack = deque(maxlen=image_stack_length)

        self.frame = None
        self.im_type = None

        self.logger = StatusLogger('imageBuffer')

    def __next__(self):
        """
        This function is used to pop the last taken image from the image stack and
        assign it to self.frame.
        This enables the user to use next(im) - assuming im = ImageBuffer() and get the
        newest frame.
        """
        if not self.image_stack:
            return False

        self.frame = self._pop()
        return True

    def __str__(self):
        """
        Provide a list of *public* functions to be used by the user.

        :return:str_method_list     :   String representing a list of functions
        """
        str_method_list = GetCallableMethods().get_methods(self)
        if self.im_type == '2d':
            str_method_list = 'image_2D'
        if self.im_type == '3d':
            str_method_list = str_method_list.replace("image_2D\r\n", "")
            str_method_list = str_method_list.replace("timestamp\r\n", "")

        return str_method_list

    def __getattr__(self, item):
        if(item == "width"):
            return self.frame["image_width"]
        if(item == "height"):
            return self.frame["image_height"]
        if(item == "time"):
            return self.timestamp()        
        #return getattr(self, item, None)

    def __calculate_distance_xyz(self):
        """
        This function uses the ifmO3r.o3ralgo functionality to calculate the

        :return:x           :   x-image
        :return:y           :   y-image
        :return:z           :   z-image
        :return:distance    :   distance image (not radial distance)
        """
        distResolution = self.frame["distance_image_info"].DistanceResolution
        extrinsicOpticToUserTrans = [
            self.frame["distance_image_info"].ExtrinsicOpticToUser.transX,
            self.frame["distance_image_info"].ExtrinsicOpticToUser.transY,
            self.frame["distance_image_info"].ExtrinsicOpticToUser.transZ,
        ]

        extrinsicOpticToUserRot = [
            self.frame["distance_image_info"].ExtrinsicOpticToUser.rotX,
            self.frame["distance_image_info"].ExtrinsicOpticToUser.rotY,
            self.frame["distance_image_info"].ExtrinsicOpticToUser.rotZ,
        ]

        intrinsicModelID = self.frame[
            "distance_image_info"
        ].IntrinsicCalibration.modelID
        intrinsicModelParameters = list(
            self.frame["distance_image_info"].IntrinsicCalibration.modelParameters
        )

        x, y, z, distance = o3ralgo.xyzd_from_distance(
            np.frombuffer(self.frame["distance"], dtype="uint16"),
            distResolution,
            extrinsicOpticToUserTrans,
            extrinsicOpticToUserRot,
            intrinsicModelID,
            intrinsicModelParameters,
            self.frame["image_width"],
            self.frame["image_height"],
        )

        return x, y, z, distance

    def __convert_distance_noise(self):
        dist_resolution = self.frame["distance_image_info"].DistanceResolution
        distance_noise = o3ralgo.convert_distance_noise(
            np.frombuffer(self.frame["distance_noise"], dtype="uint16"),
            dist_resolution,
            self.frame["image_width"],
            self.frame["image_height"]
        )

        return distance_noise

    def _push(self, frame):
        """
        Adds a frame to the stack (LiFo stack)

        :frame      :   Frame received from FrameGrabber()
        """
        self.image_stack.append(frame)
        return True

    def _pop(self):
        """
        Returns/Pops the last item (frame) from the image stack. Raises
        exception if stack is empty.

        :return:frame   :   Returns frame from stack (FrameGrabber)
        """
        return self.image_stack.pop()

    def _save_buffer(self):
        """
        This function might be used to save a frame etc. via the pickle module
        """
        cws = os.path.dirname(os.path.realpath(__file__))
        cws = os.path.join(cws, "file.p")
        pickled_buffer = pickle.dump(self, open(cws, "wb"))
        return True

    def _load_buffer(self, path=None):
        """
        You can unpickle a imagebuffer and therefore have access to the frame,
        etc. from the state when the ImageBuffer was pickled.

        :path                       :   The path were the pickled file is based
        :return:ImageBuffer()       :   Pickle loads the ImageBuffer and returns that
        """

        if path == None:
            path = os.path.dirname(os.path.realpath(__file__))
            path = os.path.join(path, "file.p")
        return pickle.load(open(path, "rb"))

    def amplitude_image(self):
        """
        :return:amplitudeImg    :   Returns the amplitude image
        """
        if self.frame is None:
            return None

        try:
            amplitudeResolution = self.frame["distance_image_info"].AmplitudeResolution
            amplitudeImg = np.frombuffer(self.frame["amplitude"], dtype="uint16")

            amplitudeImg = o3ralgo.convert_amplitude(
                amplitudeImg, amplitudeResolution,
                self.frame["image_width"],
                self.frame["image_height"]
            )
            return amplitudeImg
        except KeyError:
            self.logger.info(format(ifm3dTinyExceptions.WrongBufferType("amplitude")))
            raise ifm3dTinyExceptions.WrongBufferType("amplitude")


    def distance_image(self):
        """
        :return:distance    :   Returns the distance image (not radial distance)
        """
        try:
            x, y, z, distance = self.__calculate_distance_xyz()
            return np.array(distance)
        except KeyError:
            self.logger.info(format(ifm3dTinyExceptions.WrongBufferType("distance_image")))
            raise ifm3dTinyExceptions.WrongBufferType("distance_image")

    def confidence_image(self):
        """
        :return:confidence  :   Returns the confidence matrix/image
        """
        try:
            confidence = np.reshape(np.frombuffer(
                self.frame["confidence"], dtype="uint8"),
                (self.frame["image_height"],
                self.frame["image_width"]),
                )
            # # It appears, that one part for the calculation is missing

            # confidence = np.full(
            #     (self.image_width, self.image_height), 32
            # )  # Magic number -> confidence not yet working
            return confidence

        except KeyError:
            self.logger.info(format(ifm3dTinyExceptions.WrongBufferType("confidence_image")))
            raise ifm3dTinyExceptions.WrongBufferType("confidence_image")

    def xyz_image(self):
        """
        :return:[x,y,z]     :   Returns x,y,z as a numpy array [[x],[y],[z]]
        """
        try:
            x, y, z, _ = self.__calculate_distance_xyz()
            return np.array([x, y, z])

        except KeyError:
            self.logger.info(format(ifm3dTinyExceptions.WrongBufferType("xyz_image")))
            raise ifm3dTinyExceptions.WrongBufferType("xyz_image")

    def distance_noise_image(self):
        try:
            return self.__convert_distance_noise()
        except KeyError:
            self.logger.info(format(ifm3dTinyExceptions.WrongBufferType("distance_noise_image")))
            raise ifm3dTinyExceptions.WrongBufferType("distance_noise_image")

    def all_images(self):
        """
        :return:[x,y,z,distance,amplitude]  :   Return x,y,z,distance and amplitude image as numpy array [x,y,z,distance,amplitude]
        """
        try:
            x, y, z, distance = self.__calculate_distance_xyz()
            amplitude = self.amplitude_image()

            return np.array([x, y, z, distance, amplitude])

        except KeyError:
            self.logger.info(format(ifm3dTinyExceptions.WrongBufferType("all_images")))
            raise ifm3dTinyExceptions.WrongBufferType("all_images")

    def _set_frame(self, frame):
        """
        Simple setter method for frame. Could be used to provide a frame and
        use image buffer methods (extracting image data)

        :frame: Frame (most likely provided by FrameGrabber
        """
        self.frame = frame
        return True

    def _get_frame(self):
        """
        This function is normally not intended to be used by the user.
        Still, if you want to receive the complete frame, instead of single images,
        you can use this function. Because x,y,z images are not yet within the frame, we
        add them to the frame before forwarding it.

        :return:frame           :   Frame from ImageClient()
        """
        x, y, z = self.xyz_image()

        self.frame["x"] = x
        self.frame["y"] = y
        self.frame["z"] = z

        return self.frame

    def _get_image_stack(self):
        """
        Return the complete image stack (up to 10 frames).

        :return:imageStack  :   Image stack containing frames
        """
        return self.image_stack

    def image_2D(self):
        """
        Return the 2D image from the 2D Imager
        :return:image_2d    :   ByteArray containign the 2D image
        """
        return self.frame["img_jpeg"]

    def timestamp(self):
        """
        Returns the timestamp in sec./nano sec.
        :return: timestamp(int) in nanosec.
        """
        if self.frame["time_stamp_sec"] is None:
            return None

        timestamp = (int(self.frame["time_stamp_sec"]) * 1000000000) + int(self.frame["time_stamp_nsec"])
        return timestamp


#%%
if __name__ == "__main__":

    IP = "192.168.0.69"
    PORT = 50012

    DEFAULT_TIMEOUT = 1000
    from ifmO3r.ifm3dTiny.device import Device

    cam = Device(IP, PORT)
    fg = FrameGrabber(cam)
    im = ImageBuffer()

    fg.stream_on(im, 5)


