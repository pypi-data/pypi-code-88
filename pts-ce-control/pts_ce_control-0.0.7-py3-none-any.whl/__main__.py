import web_app
import argparse

parser = argparse.ArgumentParser(description='PTS Cell Emulator control')
parser.add_argument('-n','--cell-emulators', default=1,type=int,
                    help='number of ce to add')

parser.add_argument('-i','--interface', default="pcan",
                    help='interface typ ("pcan" or "vector"), defaults to pcan')

parser.add_argument('-a','--app-name', default='CANalyzer',
                    help='Vector CAN Application Name defaults to CANalyzer, channel is always 0')

args = parser.parse_args()

def main():
    print(f"Setting up controller for {args.cell_emulators}")
    web_app.no_cell_emulators = args.cell_emulators
    web_app.interface = args.interface
    web_app.vector_app = args.app_name
    web_app.run_webapp()

if __name__ == '__main__':
    main()
