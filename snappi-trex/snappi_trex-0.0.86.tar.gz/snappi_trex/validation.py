from snappi_trex.exceptions import SnappiTrexException
from snappi_trex.util import Util

class Validation(object):
    """This class contains functions to validate the input of various
    configuration components
    """
    
    def validate_rate(rate):
        """
        """
        pps = bps = percent = None
        if rate['choice'] == 'pps':
            pps = rate['pps']
        elif rate['choice'] == 'bps':
            bps = rate['bps']
        elif rate['choice'] == 'kbps':
            bps = rate['kbps'] * 1000
        elif rate['choice'] == 'mbps':
            bps = rate['mbps'] * 1000000
        elif rate['choice'] == 'gbps':
            bps = rate['gbps'] * 1000000000
        elif rate['choice'] == 'percentage':
            percent = rate['percentage']
        else:
            raise SnappiTrexException('Invalid \'rate\' choice')

        if pps is not None:
            if not isinstance(pps, float) and not isinstance(pps, int):
                print(isinstance(pps, float))
                raise SnappiTrexException('\'pps\' must be integer or float')
        if bps is not None:
            if not isinstance(bps, float) and not isinstance(bps, int):
                raise SnappiTrexException('\'(k/m/g)bps\' must be integer or float')
        if percent is not None:
            if not isinstance(percent, float) and not isinstance(percent, int):
                raise SnappiTrexException('\'percentage\' must be integer or float')

    def validate_duration(duration):
        """
        """
        if duration['choice'] == 'fixed_packets':
            if not isinstance(duration['fixed_packets']['packets'], int):
                raise SnappiTrexException('\'fixed_packets\' must be integer')

        elif duration['choice'] == 'fixed_seconds':
            raise SnappiTrexException('T-Rex does not support fixed_seconds duration choice')

        elif duration['choice'] == 'continuous':
            """"""

        elif duration['choice'] == 'burst':
            if 'inter_burst_gap' in duration['burst']:
                if duration['burst']['inter_burst_gap']['choice'] == 'nanoseconds':
                    ibg = duration['burst']['inter_burst_gap']['nanoseconds']
                elif duration['burst']['inter_burst_gap']['choice'] == 'microseconds':
                    ibg = duration['burst']['inter_burst_gap']['microseconds']
                elif duration['burst']['inter_burst_gap']['choice'] == 'bytes':
                    raise SnappiTrexException('T-Rex does not support bytes \'inter_burst_gap\' choice')
                else:
                    raise SnappiTrexException('Invalid \'inter_burst_gap\' option')

                if not isinstance(ibg, float) and not isinstance(ibg, int):
                    raise SnappiTrexException('\'inter_burst_gap\' must be integer or float')
        else:
            raise SnappiTrexException('Invalid \'duration\' choice')

    
    def validate_packet(packet_headers):
        """
        """
        for header in packet_headers:
            if header['choice'] == 'ethernet':
                if 'src' in header['ethernet']:
                    Validation.validate_value_option(header['ethernet']['src'], 'Ethernet', 48)
                if 'dst' in header['ethernet']:
                    Validation.validate_value_option(header['ethernet']['dst'], 'Ethernet', 48)
                
            elif header['choice'] == 'ipv4':
                if 'src' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['src'], 'IP', 32)
                if 'dst' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['dst'], 'IP', 32)
                if 'version' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['version'], 'IP', 4)
                if 'header_length' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['header_length'], 'IP', 4)
                if 'priority' in header['ipv4']:
                    if 'raw' in header['ipv4']['priority']:
                        Validation.validate_value_option(header['ipv4']['priority']['raw'], 'IP', 8)
                    else:
                        raise SnappiTrexException('ipv4 \'priority\' only supports \'raw\' option')
                if 'total_length' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['total_length'], 'IP', 16)
                if 'identification' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['identification'], 'IP', 16)
                if 'reserved' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['reserved'], 'IP', 1)
                if 'dont_fragment' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['dont_fragment'], 'IP', 1)
                if 'more_fragments' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['more_fragments'], 'IP', 1)
                if 'fragment_offset' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['fragment_offset'], 'IP', 13)
                if 'time_to_live' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['time_to_live'], 'IP', 8)
                if 'protocol' in header['ipv4']:
                    Validation.validate_value_option(header['ipv4']['protocol'], 'IP', 8)

            elif header['choice'] == 'udp':
                if 'src_port' in header['udp']:
                    Validation.validate_value_option(header['udp']['src_port'], 'UDP', 16)
                if 'dst_port' in header['udp']:
                    Validation.validate_value_option(header['udp']['dst_port'], 'UDP', 16)
                if 'length' in header['udp']:
                    Validation.validate_value_option(header['udp']['length'], 'UDP', 16)

            elif header['choice'] == 'tcp':
                if 'src_port' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['src_port'], 'TCP', 16)
                if 'dst_port' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['dst_port'], 'TCP', 16)
                if 'seq_num' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['seq_num'], 'TCP', 32)
                if 'ack_num' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ack_num'], 'TCP', 32)
                if 'data_offset' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['data_offset'], 'TCP', 4)
                if 'ecn_ns' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ecn_ns'], 'TCP', 1)
                if 'ecn_cwr' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ecn_cwr'], 'TCP', 1)
                if 'ecn_echo' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ecn_echo'], 'TCP', 1)
                if 'ctl_urg' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ctl_urg'], 'TCP', 1)
                if 'ctl_ack' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ctl_ack'], 'TCP', 1)
                if 'ctl_psh' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ctl_psh'], 'TCP', 1)
                if 'ctl_rst' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ctl_rst'], 'TCP', 1)
                if 'ctl_syn' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ctl_syn'], 'TCP', 1)
                if 'ctl_fin' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['ctl_fin'], 'TCP', 1)
                if 'window' in header['tcp']:
                    Validation.validate_value_option(header['tcp']['window'], 'TCP', 16)
            else:
                raise SnappiTrexException('Invalid packet \'header\' choice')

    def validate_size(f_size):
        if f_size['choice'] == 'increment':
            start = f_size['increment']['start']
            end = f_size['increment']['end']
            step = f_size['increment']['step']
            if not isinstance(start, int):
                raise SnappiTrexException('increment packet size \'start\' must be integer')
            if not isinstance(end, int):
                raise SnappiTrexException('increment packet size \'end\' must be integer')
            if not isinstance(step, int):
                raise SnappiTrexException('increment packet size \'step\' must be integer')

        elif f_size['choice'] == 'random':
            start = f_size['random']['min']
            end = f_size['random']['max']
            if not isinstance(start, int):
                raise SnappiTrexException('random packet size \'start\' must be integer')
            if not isinstance(end, int):
                raise SnappiTrexException('random packet size \'end\' must be integer')

        elif f_size['choice'] == 'fixed':
            val = f_size['fixed']
            if not isinstance(val, int):
                raise SnappiTrexException('\'fixed\' packet size must be integer')

        else:
            raise SnappiTrexException('Invalid packet \'size\' choice')


    def validate_value_option(header_field, layer_type, length):
        if header_field['choice'] == 'value':
            Validation.validate_address(header_field['value'], layer_type, length)
        elif header_field['choice'] == 'values':
            for val in header_field['values']:
                Validation.validate_address(val, layer_type, length)
        elif header_field['choice'] == 'increment':
            Validation.validate_increment(header_field['increment'], layer_type, length, 1)
        elif header_field['choice'] == 'decrement':
            Validation.validate_increment(header_field['decrement'], layer_type, length, -1)
        else: 
            raise SnappiTrexException('Invalid field value choice')

    
    def validate_increment(field_inc, layer_type, length, dir):
        Validation.validate_address(field_inc['start'], layer_type, length)
        Validation.validate_address(field_inc['step'], layer_type, length)
        if not isinstance(field_inc['count'], int):
            raise SnappiTrexException('\'count\' must be integer')
        start = Util.convert_to_long(field_inc['start'], layer_type)
        step = Util.convert_to_long(field_inc['step'], layer_type)
        cnt = field_inc['count']
        if step * cnt > Util.get_mask(length):
            raise SnappiTrexException('step*count cannot exceed the header field range')
        if length == 64 and start + dir*step*cnt > Util.get_mask(64) and start + dir*step*cnt < 0:
            raise SnappiTrexException('step*count is too high. Overflow is not support for 8 byte fields')

    
    def validate_address(addr, layer_type, length):
        error = False
        try:
            val = Util.convert_to_long(addr, layer_type)
            if val > Util.get_mask(length):
                error = True
        except ValueError as e:
            error = True
        if error:
            raise SnappiTrexException('{0} is not a valid {1} address'.format(addr, layer_type))
