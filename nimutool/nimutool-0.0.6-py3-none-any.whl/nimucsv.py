import argparse
from nimutool import *


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tool for reading nimu data from CAN bus')
    parser.add_argument('--trace-file', type=str, help='PCAN-View generated trace file')
    parser.add_argument('--hex2nimu', action='store_true', help='Convert PILogger can2hex output')
    parser.add_argument('--output', help='Output file, "ni_" or "pi_" prefix will be added based bus content', default='data.csv')
    parser.add_argument('--extras', action='store_true', help='Show some extra contents from CAN BUS')
    parser.add_argument('--nimu-protocol', default=2, help='Protocol version of Nimu CAN frames')
    parser.add_argument('--can-adapter', default='pcan', help='Can adapter to use, see options from python-can documentation')
    args = parser.parse_args()

    if args.hex2nimu:
        bus = PiLoggerCanBusReader()
    elif args.trace_file:
        bus = TraceFileCanBusReader(args.trace_file)
    else:
        bus = CanBusReader(can.interface.Bus(bustype=args.can_adapter, bitrate=1000000))
    for msg in read_bus(bus, f'ni_{args.output}', f'pi_{args.output}', args.extras, args.nimu_protocol):
        pass
