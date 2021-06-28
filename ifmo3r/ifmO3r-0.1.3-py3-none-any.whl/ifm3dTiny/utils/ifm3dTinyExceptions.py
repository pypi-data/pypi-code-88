# %%

class ifm3dTinyException(Exception):
    pass

class Timeout(ifm3dTinyException):
    def __init__(self):
        self.message = "Timeout occurred - check power, connection, port, ip, timout in sec."
        super().__init__(self.message)

    def __str__(self):
        return self.message

class WrongBufferType(ifm3dTinyException):
    def __init__(self, image_name):
        self.image_name = image_name
        self.message = "The "+ image_name+ " is not available for the current ImageBuffer object (wrong 2D/3D imager type)."
    def __str__(self):
        return self.message

class WrongPortNumber(ifm3dTinyException):
    def __init__(self, port_nb):
        self.port_nb = port_nb
        self.message = "Invalid port number: "+str(self.port_nb)
    def __str__(self):
        return self.message

class WrongJSONStructure(ifm3dTinyException):
    def __init__(self):
        self.message = "Wrong JSON structure. Follow the structure returned by the dump() function."
    def __str__(self):
        return self.message

class ParameterError(ifm3dTinyException):
    def __init__(self, param_name):
        self.message = "The expected value for "+param_name+" is not available. Please refer to the json schema."
    def __str__(self):
        return self.message

class WrongImagerType(ifm3dTinyException):
    def __init__(self):
        self.message = "The Device object you are using refers to the wrong imager type (2D or 3D)"
    def __str__(self):
        return self.message

class StreamingMultipleQueues(ifm3dTinyException):
    def __init__(self):
        self.message = "'CAUTION streaming to two queues with the same frame grabber instance is currently not supported"
    def __str__(self):
        return self.message

# %%
if __name__ == "__main__":
    raise Timeout
    print(Timeout)
# %%
