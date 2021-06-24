import asyncio
from abc import ABC, abstractmethod
from .BaseRobot import BaseRobot
from binance.enums import FuturesType


class KlineRobot(BaseRobot, ABC):

    def __init__(self):
        super().__init__()

        # Количество раз неудачно пропингованный
        self.ping_bad = 0

        # ts последнего обновления сокета мнутных данных
        self.last_kline_update = self.get_current_timestamp()

    async def ping_client(self):
        """ Пинговать клиента на стабильность соединения"""
        while True:
            try:
                await self.client.ping()
                self.ping_bad = 0
            except Exception as e:
                if self.ping_bad > 2:
                    raise e
                else:
                    self.ping_bad += 1
                    await self.log_info(str(e))
            if self.get_current_timestamp() - self.last_kline_update > 70:
                raise Exception('Длительное ожидание сокета минутных данных')
            await asyncio.sleep(10)

    async def up_klines_fetching(self):
        ks = self.get_futures_kline_socket(self.ticket, interval=self.client.KLINE_INTERVAL_1MINUTE)
        async with ks:
            while True:
                kline = await ks.recv()
                self.last_kline_update = self.get_current_timestamp()
                if kline['data']['k']['x'] is True:
                    await self.process_new_data(kline)

    def get_futures_kline_socket(self, symbol, interval):
        """ Костыль для получения сокета для свечей """
        path = f'{symbol.lower()}@kline_{interval}'
        return self.bm._get_futures_socket(path, futures_type=FuturesType.USD_M)

    @abstractmethod
    async def process_new_data(self, kline):
        """ Обработать новые данные по минутным данным """
        pass
