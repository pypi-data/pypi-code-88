import sys
from enum import Enum
import dataclasses

import serial

import mp
import mp.micropythonshell
from mp.mpfshell import RemoteIOError
from mp.firmware.update import URL_README

FILENAME_IDENTIFICATION = mp.micropythonshell.FILENAME_IDENTIFICATION

class BoardqueryException(Exception):
    pass

@dataclasses.dataclass
class ProductId:
    vendorid: int
    productid: int
    name: str = None

class Product(Enum):
    ANY = None
    Pyboard = ProductId(0xF055, 0x9800)
    Espruino = ProductId(0xF055, 0x9800)
    BlackPill = ProductId(0xF055, 0x9800)
    Esp32 = ProductId(0x10C4, 0xEA60)
    RaspberryPico = ProductId(0x2E8A, 0x0005)

    def is_type(self, vendorid, productid):
        return (self.value.vendorid == vendorid) and (self.value.productid == productid)

    @classmethod
    def all(cls):
        return [product for product in cls if product != Product.ANY]

    @classmethod
    def find(cls, vendorid, productid):
        for product in Product.all():
            if product.is_type(vendorid, productid):
                return product
        return None


for product in Product.all():
    product.value.name = product.name

@dataclasses.dataclass
class Identification:
    FILENAME: str
    READ_ERROR: str = None
    FILECONTENT: str = None
    HWTYPE: str = None
    HWVERSION: str = None
    HWSERIAL: str = None

    def print(self, indent='', f=sys.stdout):
        for field in dataclasses.fields(self):
            name = field.name
            value = getattr(self, name)
            if value == None:
                continue
            if value and '\n' in value:
                # Pretty print multiline as FILECONTENT
                fileindent = f'\r\n{indent}     '
                value = fileindent + fileindent.join(value.splitlines())
            print(f'{indent}{self.FILENAME}.{name}: {value}', file=f)


class Board:
    def __init__(self, port, mpfshell, identification):
        assert isinstance(port, serial.tools.list_ports_common.ListPortInfo)
        assert isinstance(mpfshell, mp.micropythonshell.MicropythonShell)
        assert isinstance(identification, Identification)

        self.port = port
        self.mpfshell = mpfshell
        self.identification = identification
        self.micropython_sysname = self.mpfshell.MpFileExplorer.sysname
        self.micropython_release = self.mpfshell.MpFileExplorer.eval("uos.uname().release").decode("utf-8")
        self.micropython_machine = self.mpfshell.MpFileExplorer.eval("uos.uname().machine").decode("utf-8")

    def close(self):
        if isinstance(self.mpfshell, str):
            return
        self.mpfshell.close()

    @property
    def quickref(self):
        'returns "scanner_pyb_2020(pyboard/COM8)"'
        return f'{self.identification.HWTYPE}({self.micropython_sysname}/{self.port.name})'

    def systemexit_firmware_required(self, min: str=None, max: str=None):
        'Raise a exception if firmware does not fit requirements'
        fail = False
        text = self.micropython_release
        if min is not None:
            fail = fail or (min > self.micropython_release)
            text = f'{min}<={text}'
        if max is not None:
            fail = fail or (max < self.micropython_release)
            text = f'{text}<={max}'
        if fail:
            raise SystemExit(f'ERROR: {self.quickref} firmware {self.micropython_release} is installed, but {text} is required! To update see {URL_README}')

    def systemexit_hwtype_required(self, hwtype: str=None):
        'Raise a exception if hardwaretype does not fit requirements'
        if hwtype is not self.identification.HWTYPE:
            raise SystemExit(f'ERROR: {self.quickref}: Expected "{hwtype}" but the connected board is of HWTYPE "{self.identification.HWTYPE}"!')

    def systemexit_hwversion_required(self, min: str=None, max: str=None):
        'Raise a exception if hwversion does not fit requirements'
        fail = False
        text = self.identification.HWVERSION
        if min is not None:
            fail = fail or (min > self.identification.HWVERSION)
            text = f'{min}<={text}'
        if max is not None:
            fail = fail or (max < self.identification.HWVERSION)
            text = f'{text}<={max}'
        if fail:
            raise SystemExit(f'ERROR: {self.quickref} hwversion "{self.identification.HWVERSION}" is connected, but {text} is required!')

    def print(self, f=sys.stdout):
        print(f'    Board Query {self.port.name}', file=f)
        print(f'      pyserial.description: {self.port.description}', file=f)
        print(f'      pyserial.hwid: {self.port.hwid}', file=f)
        if isinstance(self.mpfshell, str):
            print(f'      mpfshell-error: {self.mpfshell}', file=f)
        else:
            print(f'      mpfshell.micropython_sysname: {self.micropython_sysname}', file=f)
            print(f'      mpfshell.micropython_release: {self.micropython_release}', file=f)
            print(f'      mpfshell.micropython_machine: {self.micropython_machine}', file=f)
        self.identification.print(indent='      ', f=f)


class BoardQueryBase:
    def __init__(self, product: Product):
        assert isinstance(product, Product)
        self.board = None
        self.product = product
        self.matching_boards_found = 0

    def select_pyserial(self, port):
        assert isinstance(port, serial.tools.list_ports_common.ListPortInfo)
        if self.product is Product.ANY:
            return True
        product = Product.find(port.vid, port.pid)
        if product is None:
            # This hardware is unknown
            return False
        return product == self.product

    def select_identification(self, identification):
        assert isinstance(identification, Identification)
        return True

    @property
    def identification(self):
        raise Exception('Programming error: Please override')

    @staticmethod
    def read_identification(mpfshell):
        if isinstance(mpfshell, str):
            return Identification(READ_ERROR=mpfshell, FILENAME=FILENAME_IDENTIFICATION)
        try:
            source = mpfshell.MpFileExplorer.gets(src=FILENAME_IDENTIFICATION)
        except RemoteIOError as e:
            return Identification(READ_ERROR=str(e), FILENAME=FILENAME_IDENTIFICATION)
        globals = {}
        try:
            exec(source, globals)
        except SyntaxError as e:
            return Identification(READ_ERROR=str(e), FILENAME=FILENAME_IDENTIFICATION)
        # Only take keys in uppercase
        # identification = {key:value for key, value in globals.items() if key.isupper()}
        identification = Identification(FILENAME=FILENAME_IDENTIFICATION, FILECONTENT=source)
        for key, value in globals.items():
            if not key.isupper():
                continue
            setattr(identification, key, value)
        return identification


    @staticmethod
    def print_all(f=sys.stdout):
        print('*** Board Query: scan', file=f)
        boards = []
        try:
            for port in serial.tools.list_ports.comports():
                try:
                    mpfshell = mp.micropythonshell.MicropythonShell(str_port=port.device)
                except Exception as e:
                    print(f'*** {port}: {e}', file=f)
                    continue

                identification = BoardQueryBase.read_identification(mpfshell)
                board = Board(port, mpfshell, identification)
                boards.append(board)

            print('*** Board Query: Micropython boards found:', file=f)
            for board in boards:
                board.print(f=f)
        finally:
            for board in boards:
                board.close()

    @staticmethod
    def get_identification(queries):
        for q in queries:
            assert isinstance(q, BoardQueryBase)
            assert isinstance(q.identification, str)

        return ', '.join([q.identification for q in queries])

    @staticmethod
    def connect(queries, exactly_once=True):
        assert isinstance(queries, list)
        assert isinstance(BoardQueryBase.get_identification(queries), str)

        mpfshells_openend = []
        for port in serial.tools.list_ports.comports():
            mpfshell = None
            identification = None
            com_port_done = False
            for query in queries:
                if query.select_pyserial(port):
                    if mpfshell is None:
                        try:
                            mpfshell = mp.micropythonshell.MicropythonShell(str_port=port.device)
                            mpfshells_openend.append(mpfshell)
                        except Exception as e:
                            print(f"{e}")
                            # We can not connect: Stop searching for this com port
                            com_port_done = True
                            break

                    if identification is None:
                        identification = BoardQueryBase.read_identification(mpfshell)
                    if query.select_identification(identification):
                        if query.matching_boards_found == 0:
                            query.board = Board(port, mpfshell, identification)
                        query.matching_boards_found += 1
                        # A query matched: Stop searching for this com port
                        com_port_done = True
                        break
            
            if com_port_done:
                break

        all_queries_satisfied = True
        for query in queries:
            if query.matching_boards_found == 0:
                all_queries_satisfied = False
            if exactly_once:
                if query.matching_boards_found > 1:
                    raise BoardqueryException(f"Boardquery '{query.identification}' matches {query.matching_boards_found} times.")
        if all_queries_satisfied:
            # All micropython boards found
            return True

        # At lease one query is not satisfied
        # free allocated com-interfaces
        for mpfshell_open in mpfshells_openend:
            mpfshell_open.close()
        return False


class BoardQueryPyboard(BoardQueryBase):
    '''
    Selects pyboards with a 'config_identification.py' of given 'hwtype'.
    Selects any board if hwtype is None
    '''
    def __init__(self, hwtype: str=None, product: Product = Product.ANY):
        super().__init__(product=product)
        self.hwtype = hwtype

    def select_pyserial(self, port):
        return super().select_pyserial(port)

    def select_identification(self, identification):
        assert isinstance(identification, Identification)
        if self.hwtype is None:
            # We want to select any pyboard
            return True
        return identification.HWTYPE == self.hwtype

    @property
    def identification(self):
        return f'pyboard(HWTYPE={self.hwtype})'

class BoardQueryHwtypeSerial(BoardQueryBase):
    '''
    Selects pyboards with a 'config_identification.py' of given 'hwtype' AND 'hwserial'.
    'hwtype' and 'hwserial' may be None
    '''
    def __init__(self, hwtype: str=None, hwserial: str=None, product: Product=Product.ANY):
        super().__init__(product=product)
        self.hwtype = hwtype
        self.hwserial = hwserial
 
    def select_pyserial(self, port):
        return super().select_pyserial(port)
 
    def select_identification(self, identification):
        assert isinstance(identification, Identification)
        if self.hwtype is not None:
            if identification.HWTYPE != self.hwtype:
                return False
        if self.hwserial is not None:
            if identification.HWSERIAL != self.hwserial:
                return False
        return True
 
    @property
    def identification(self):
        return f'pyboard(HWTYPE={self.hwtype}, HWSERIAL={self.hwserial})'

class BoardQueryComport(BoardQueryBase):
    '''
    Selects pyboards with a 'comport'.
    Selects first comport if comport is None.
    '''
    def __init__(self, comport: str=None, product: Product=Product.ANY):
        super().__init__(product)
        self.comport = comport

    def select_pyserial(self, port):
        if not super().select_pyserial(port):
            return False
        if self.comport is None:
            # Pick the first port
            return True
        return port.device.lower() == self.comport.lower()

    @property
    def identification(self):
        return f'(COM={self.comport})'


def Connect(list_queries):
    found = BoardQueryBase.connect(list_queries)
    if not found:
        msg = f'Pyboards not found! Query={BoardQueryBase.get_identification(list_queries)}'
        print(f'ERROR: {msg}')
        BoardQueryBase.print_all()
        raise BoardqueryException(msg)


def ConnectPyboard(hwtype=None, product: Product=Product.ANY):
    query = BoardQueryPyboard(hwtype, product=product)
    found = BoardQueryBase.connect([query])
    if not found:
        msg = f'Pyboard of HWTYPE={hwtype} not found!'
        print(f'ERROR: {msg}')
        BoardQueryBase.print_all()
        raise BoardqueryException(msg)
    return query.board


def ConnectComport(comport: str=None, product: Product=Product.ANY):
    query = BoardQueryComport(comport=comport, product=product)
    found = BoardQueryBase.connect([query])
    if not found:
        msg = f'Pyboard with comport "{comport}" and product "{product.name}" not found!'
        print(f'ERROR: {msg}')
        BoardQueryBase.print_all()
        raise BoardqueryException(msg)
    return query.board


def ConnectHwtypeSerial(hwtype: str=None, hwserial: str=None, product: Product=Product.ANY, exactly_once=True):
    query = BoardQueryHwtypeSerial(product=product, hwtype=hwtype, hwserial=hwserial)
    found = BoardQueryBase.connect([query], exactly_once=exactly_once)
    if not found:
        msg = f'{product} not found: {query.identification}'
        print(f'ERROR: {msg}')
        BoardQueryBase.print_all()
        raise BoardqueryException(msg)
    return query.board


def example_A():
    _board = ConnectComport('COM9')
    # This call will list a 'connected' com port.
    BoardQueryBase.print_all()


def example_B():
    print('start')
    scanner = BoardQueryPyboard('scanner_pyb_2020')
    compact = BoardQueryPyboard('compact_2012')
    Connect([compact, scanner])
    print('done')

def example_C():
    print('start')
    board = ConnectHwtypeSerial(product=Product.Pyboard, hwtype='compact_2012', hwserial='20000101_01')
    print('done')

def main():
    BoardQueryBase.print_all()
    example_C()

if __name__ == "__main__":
    main()
