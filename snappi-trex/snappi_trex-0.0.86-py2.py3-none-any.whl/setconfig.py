from snappi_trex.util import Util
from trex.stl.api import *
from snappi_trex.valueoptions import ValueOptions
from snappi_trex.validation import Validation

class SetConfig:

    def set_rate(rate):
        """
        Returns packets per second, bits per second, and percent values.
        (Only one of the three will be set, the rest will be Null)
        args: 
            - rate: A dictionary object containing all of the rate configuration info
        """
        Validation.validate_rate(rate)
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
        return pps, bps, percent

    
    def set_duration(duration, pps, bps, percent):
        """
        Returns a STLTXMode object with correct rate and duration configurations
        args: 
            - duration: A dictionary object containing all of the duration config info
            - pps: packets per second
            - bps: bits per second
            - percent: percent of layer 2 bit rate
            Note: Only one of (pps, bps, percent) will have a value. The rest are None.
        """
        Validation.validate_duration(duration)
        if duration['choice'] == 'fixed_packets':
            mode = STLTXSingleBurst(
                total_pkts=duration['fixed_packets']['packets'], 
                pps=pps, bps_L2=bps, percentage=percent
            )

        elif duration['choice'] == 'continuous':
            mode = STLTXCont(pps=pps, bps_L2=bps, percentage=percent)

        elif duration['choice'] == 'burst':
            # TODO: Fix the ibg param to inter burst gap, not gap
            ibg = 0.0
            if 'inter_burst_gap' in duration['burst']:
                if duration['burst']['inter_burst_gap']['choice'] == 'nanoseconds':
                    ibg = duration['burst']['inter_burst_gap']['nanoseconds']
                elif duration['burst']['inter_burst_gap']['choice'] == 'microseconds':
                    ibg = duration['burst']['inter_burst_gap']['microseconds'] / 1000
            mode = STLTXMultiBurst(
                pkts_per_burst=duration['burst']['packets'],
                ibg=ibg,
                count=duration['burst']['bursts'],
                pps=pps, bps_L2=bps, percentage=percent)

        return mode

    
    def set_packet_headers(packet_headers):
        """
        Returns list of VM instructions to correctly configure each packet header
        and each header field with correct value configurations. Also returns a list
        of packet headers added. Also returns list of strings representing the appended
        layers.
        args:
            - packet_headers: An array of objects that represent packet headers and all
            of their fields
        """
        Validation.validate_packet(packet_headers)
        header_info = Util.get_header_info()
        pkt_headers = []
        vm_cmds = []
        layers = [] # Keeps track of all of the layer types in order
        layer_cnt = {} # Counts the occurrences of each layer type
        for header in packet_headers:

            # ETHERNET HEADER FIELDS CONFIGURATION
            if header['choice'] == 'ethernet':
                pkt_headers.append(Ether()); layers.append('Ether')
                layer_cnt['Ether'] = layer_cnt['Ether']+1 if 'Ether' in layer_cnt else 1

                for field in header['ethernet']:
                    field_info = header_info['ethernet'][field]
                    vm_cmds += ValueOptions.get_value_cmds(
                        layer_type='Ethernet', 
                        layer_cnt=layer_cnt['Ether'], 
                        header_field=header['ethernet'][field], 
                        length=field_info['length'], 
                        field_str=field_info['field_str'],
                        bit_fixup=field_info['bit_fixup']
                    )
                
            # IPv4 HEADER FIELDS CONFIGURATION
            elif header['choice'] == 'ipv4':
                pkt_headers.append(IP()); layers.append('IP')
                layer_cnt['IP'] = layer_cnt['IP']+1 if 'IP' in layer_cnt else 1

                for field in header['ipv4']:
                    field_info = header_info['ipv4'][field]
                    if field == 'priority':
                        header_field = header['ipv4'][field]['raw']
                    else:
                        header_field = header['ipv4'][field]
                    vm_cmds += ValueOptions.get_value_cmds(
                        layer_type='IP', 
                        layer_cnt=layer_cnt['IP'], 
                        header_field=header_field, 
                        length=field_info['length'], 
                        field_str=field_info['field_str'],
                        bit_fixup=field_info['bit_fixup']
                    )

            # UDP HEADER FIELDS CONFIGURATION
            elif header['choice'] == 'udp':
                pkt_headers.append(UDP()); layers.append('UDP')
                layer_cnt['UDP'] = layer_cnt['UDP']+1 if 'UDP' in layer_cnt else 1

                for field in header['udp']:
                    field_info = header_info['udp'][field]
                    vm_cmds += ValueOptions.get_value_cmds(
                        layer_type='UDP', 
                        layer_cnt=layer_cnt['UDP'], 
                        header_field=header['udp'][field], 
                        length=field_info['length'], 
                        field_str=field_info['field_str'],
                        bit_fixup=field_info['bit_fixup']
                    )

            # TCP HEADER FIELDS CONFIGURATION
            elif header['choice'] == 'tcp':
                pkt_headers.append(TCP()); layers.append('TCP')
                layer_cnt['TCP'] = layer_cnt['TCP']+1 if 'TCP' in layer_cnt else 1

                for field in header['tcp']:
                    field_info = header_info['tcp'][field]
                    vm_cmds += ValueOptions.get_value_cmds(
                        layer_type='TCP', 
                        layer_cnt=layer_cnt['TCP'], 
                        header_field=header['tcp'][field], 
                        length=field_info['length'], 
                        field_str=field_info['field_str'],
                        bit_fixup=field_info['bit_fixup']
                    )
            
        return vm_cmds, pkt_headers, layers


    def set_packet_size(f_size, pkt_base, layers):
        """
        Returns a list of VM instructions to configure the correct size option. Also 
        returns a stream of bytes representing the padding of the packets
        args: 
            - f_size: A dictionary object containing all of the flow packet size config info
            - pkt_base: A Scapy packet containing all of the header information for every layer
            - layers: An ordered list of strings representing the order of headers on the packet base
                    Strings must conform to supported Scapy protocols
        """
        Validation.validate_size(f_size)
        vm_cmds = []
        if f_size['choice'] == 'increment':
            needs_trim = True
            start = f_size['increment']['start']
            max_pkt_size = end = f_size['increment']['end']
            step = f_size['increment']['step']
            vm_cmds.append(STLVmFlowVar(name = 'pkt_len', size = 2, op = 'inc', step = step,
                                            min_value = start,
                                            max_value = end))

        elif f_size['choice'] == 'random':
            needs_trim = True
            start = f_size['random']['min']
            max_pkt_size = end = f_size['random']['max']
            vm_cmds.append(STLVmFlowVar(name = 'pkt_len', size = 2, op = 'random',
                                            min_value = start,
                                            max_value = end))

        elif f_size['choice'] == 'fixed':
            needs_trim = False
            max_pkt_size = f_size['fixed']

        # Trim packets and fix len field if needed
        if needs_trim:
            vm_cmds.append(STLVmTrimPktSize('pkt_len'))
            layers_with_len = {'IP': 0, 'UDP': 0}
            for i, layer in enumerate(layers):
                if layer in layers_with_len:
                    pkt_offset = "{0}:{1}.len".format(layer, layers_with_len[layer])
                    vm_cmds.append(STLVmWrFlowVar(fv_name='pkt_len',
                                                pkt_offset=pkt_offset,
                                                add_val=len(pkt_base[i])-len(pkt_base)
                    ))
                    layers_with_len[layer] += 1

        # Fill the rest of the packet with x's
        pad = max(0, max_pkt_size - len(pkt_base)) * 'x'

        return vm_cmds, pad
