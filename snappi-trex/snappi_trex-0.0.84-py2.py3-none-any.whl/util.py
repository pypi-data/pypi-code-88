class Util:
    """
    This class contains miscellaneous utility functions
    """
    def get_mask(bits):
        """
        returns a mask of 1's of size bits
        """
        result = (1 << bits) - 1
        return result

    
    def uint_to_int(uint, size):
        """
        converts an unsigned int of size n to a signed int of size n
        """
        result = uint & Util.get_mask(size)
        if result >= (1 << (size-1)):
            result -= (1 << size)
        return result


    def convert_to_long(value, layer_type):
        """
        Parses address values into a long int
        args:
            - value: A string or long representing the address
            - layer_type: A string representing the layer type
        """
        if isinstance(value, int): 
            return value

        if layer_type == 'IP':
            elements = value.split('.')
            result = 0
            for e in elements:
                result = result << 8
                if len(e) == 0:
                    continue
                result += int(e)
            return result

        if layer_type == 'Ethernet':
            elements = value.split(':')
            result = 0
            for e in elements:
                result = result << 8
                if len(e) == 0:
                    continue
                result += int(e, 16)
            return result
        
        return value