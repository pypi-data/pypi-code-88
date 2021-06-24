import asyncio
import os
import aiohttp
from aiofile import async_open
from abc import ABC, abstractmethod
from datetime import datetime
from binance import AsyncClient, BinanceSocketManager
from .EnvLoader import EnvLoader


class BaseRobot(ABC):

    # Константы для ключей словарей
    CLOSES = 'closes'
    HIGHS = 'highs'
    LOWS = 'lows'

    # Индексы колонок в исторических данных по барам
    KLINE_CLOSE_INDEX = 4
    KLINE_HIGH_INDEX = 2
    KLINE_LOW_INDEX = 3

    def __init__(self):

        # Тикет инструмента
        self.ticket = EnvLoader.get_var('TICKET')

        # Клиент Бинанс
        self.client: AsyncClient = None

        # клиент сокета Бинанс
        self.bm: BinanceSocketManager = None

        # Количество знаков после запятой для объема
        self.quantity_precision = 0

        # Заблокированы ли действия
        self.block_actions = False

        # Путь файла общих логов
        self.log_common_path = os.path.join(os.path.abspath(os.curdir), 'logs', self.ticket + '_common.log')

        # Путь файла логов сделок
        self.log_trades_path = os.path.join(os.path.abspath(os.curdir), 'logs', self.ticket + '_trades.csv')

        # В позиции ли сейчас
        self.position = False

        # Объем позиции
        self.position_value = 0.0

        # сокет данных об аккаунте инициализирован
        self.socket_account_data_inited = False

    async def async_init(self):
        self.client = await AsyncClient.create(EnvLoader.get_api_key(), EnvLoader.get_api_secret())
        self.bm = BinanceSocketManager(self.client)
        await self.set_quantity_precision()
        await self.set_initial_position()

    async def set_quantity_precision(self):
        """ Установить точность цены инструмента """
        info = await self.client.futures_exchange_info()
        for i in info['symbols']:
            if i['symbol'] == self.ticket:
                self.quantity_precision = i['quantityPrecision']
                break

    async def log_info(self, msg):
        msg = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + " INFO: " + str(msg) + "\r"
        if int(EnvLoader.get_var('LOG_STDOUT')) == 1:
            print(msg)
        if int(EnvLoader.get_var('LOG_FILE')) == 1:
            await self.log_to_file(msg)

    async def log_error(self, msg):
        msg = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + " ERROR: " + str(msg) + "\r"
        if int(EnvLoader.get_var('LOG_STDOUT')) == 1:
            print(msg)
        if int(EnvLoader.get_var('LOG_FILE')) == 1:
            await self.log_to_file(msg)
        if int(EnvLoader.get_var('ERROR_TO_TELEGRAM')) == 1:
            await self.send_telegram_message('Я наебнулся (' + self.ticket + '): ' + str(msg))

    async def send_telegram_message(self, message):
        """  Отправить сообщение в телеграм """
        token = EnvLoader.get_var('TELEGRAM_TOKEN')
        url = "https://api.telegram.org/bot"
        channel_id = EnvLoader.get_var('TELEGRAM_CHANNEL')
        url += token + "/sendMessage"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data={
                "chat_id": channel_id,
                "text": message
            }) as response:
                print("Status:", response.status)

    async def log_to_file(self, msg):
        """ Залогировать в файл """
        try:
            async with async_open(self.log_common_path, 'ab+') as afp:
                await afp.write(str.encode(msg))
        except Exception as e:
            async with async_open(self.log_common_path, 'wb+') as afp:
                await afp.write(str.encode(msg))

    async def log_trade(self, msg):
        """ Залогировать в файл сделку """
        if int(EnvLoader.get_var('LOG_TRADES')) != 1:
            return
        try:
            async with async_open(self.log_trades_path, 'ab+') as afp:
                await afp.write(str.encode(msg))
        except Exception as e:
            async with async_open(self.log_trades_path, 'wb+') as afp:
                await afp.write(str.encode(msg))

    async def market_buy(self, value: float, reduceOnly: bool = False):
        """ Купить по рынку """
        await self.client.futures_create_order(
            symbol=self.ticket,
            side='BUY',
            type='MARKET',
            quantity=self.round_lot_size(value),
            reduceOnly='true' if reduceOnly is True else 'false'
        )
        await self.wait_action_block_disabling()

    async def market_sell(self, value: float, reduceOnly: bool = False):
        """  Продать по рынку"""
        await self.client.futures_create_order(
            symbol=self.ticket,
            side='SELL',
            type='MARKET',
            quantity=self.round_lot_size(value),
            reduceOnly='true' if reduceOnly is True else 'false'
        )
        await self.wait_action_block_disabling()

    def round_lot_size(self, lot_size: float):
        return "{:0.0{}f}".format(lot_size, self.quantity_precision)

    async def wait_action_block_disabling(self):
        """ Ожидать снятия блокировки """
        i = 0
        while self.block_actions:
            if i > 50:
                raise Exception('Долго нет ответа по заявке')
            i += 1
            await asyncio.sleep(0.1)

    @staticmethod
    def get_current_timestamp() -> int:
        return int(round(datetime.now().timestamp(), 0))

    @staticmethod
    def calculate_true_range(high, low, prev_close):
        """ Рассчитать True Range """
        return max(
            abs(high - low),
            abs(high - prev_close),
            abs(low - prev_close)
        )

    async def set_initial_position(self):
        """ Установить позицию на момент инициализации """
        info = await self.client.futures_position_information()
        for i in info:
            if i['symbol'] == self.ticket:
                position_value = float(i['positionAmt'])
                if abs(position_value) > 0.000000001:
                    self.position = True
                    self.position_value = position_value

    async def up_account_data_fetching(self):
        fds = self.bm.futures_socket()
        async with fds:
            while True:
                if self.socket_account_data_inited is False:
                    asyncio.create_task(self.make_decision())
                    self.socket_account_data_inited = True
                event = await fds.recv()
                await self.process_account_data(event)

    @abstractmethod
    async def make_decision(self):
        pass

    @abstractmethod
    async def process_account_data(self, event):
        """  """
        pass

    @abstractmethod
    async def run(self):
        """Запустить робота """
        pass

    async def close(self):
        """ Закрыть соединения по инструменту """
        await self.log_info('--CLOSE--')
        await self.client.close_connection()