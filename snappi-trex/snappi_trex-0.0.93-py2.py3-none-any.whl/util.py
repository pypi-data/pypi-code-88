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

    def get_header_info():
        return {
            "ethernet": {
                "src": {"field_str": "src", "length": 48, "bit_fixup": 0},
                "dst": {"field_str": "dst", "length": 48, "bit_fixup": 0}
            },
            "ipv4": {
                "src": {"field_str": "src", "length": 32, "bit_fixup": 0},
                "dst": {"field_str": "dst", "length": 32, "bit_fixup": 0},
                "version": {"field_str": "version", "length": 4, "bit_fixup": 0},
                "header_length": {"field_str": "ihl", "length": 4, "bit_fixup": 0},
                "priority": {"field_str": "tos", "length": 8, "bit_fixup": 0},
                "total_length": {"field_str": "len", "length": 16, "bit_fixup": 0},
                "identification": {"field_str": "id", "length": 16, "bit_fixup": 0},
                "reserved": {"field_str": "flags", "length": 1, "bit_fixup": 0},
                "dont_fragment": {"field_str": "flags", "length": 1, "bit_fixup": 1},
                "more_fragments": {"field_str": "flags", "length": 1, "bit_fixup": 2},
                "fragment_offset": {"field_str": "frag", "length": 13, "bit_fixup": 3},
                "time_to_live": {"field_str": "ttl", "length": 8, "bit_fixup": 0},
                "protocol": {"field_str": "proto", "length": 8, "bit_fixup": 0}
            },
            "udp": {
                "src_port": {"field_str": "sport", "length": 16, "bit_fixup": 0},
                "dst_port": {"field_str": "dport", "length": 16, "bit_fixup": 0},
                "length": {"field_str": "len", "length": 16, "bit_fixup": 0}
            },
            "tcp": {
                "src_port": {"field_str": "sport", "length": 16, "bit_fixup": 0},
                "dst_port": {"field_str": "dport", "length": 16, "bit_fixup": 0},
                "seq_num": {"field_str": "seq", "length": 32, "bit_fixup": 0},
                "ack_num": {"field_str": "ack", "length": 32, "bit_fixup": 0},
                "data_offset": {"field_str": "dataofs", "length": 4, "bit_fixup": 0},
                "ecn_ns": {"field_str": "flags", "length": 1, "bit_fixup": 7},
                "ecn_cwr": {"field_str": "flags", "length": 1, "bit_fixup": 8},
                "ecn_echo": {"field_str": "flags", "length": 1, "bit_fixup": 9},
                "ctl_urg": {"field_str": "flags", "length": 1, "bit_fixup": 10},
                "ctl_ack": {"field_str": "flags", "length": 1, "bit_fixup": 11},
                "ctl_psh": {"field_str": "flags", "length": 1, "bit_fixup": 12},
                "ctl_rst": {"field_str": "flags", "length": 1, "bit_fixup": 13},
                "ctl_syn": {"field_str": "flags", "length": 1, "bit_fixup": 14},
                "ctl_fin": {"field_str": "flags", "length": 1, "bit_fixup": 15},
                "window": {"field_str": "window", "length": 16, "bit_fixup": 0}
            }
        }