from datetime import datetime, timedelta
from typing import List

from ..mtapi.pyMTApi import *

from .setting import SETTINGS 
from .constant import (
    Direction,
    Offset,
    Exchange,
    OrderType,
    Product,
    Status,
    OptionType,
    Interval,
)
from .object import (
    BarData,
    TickData,
    OrderData,
    TradeData,
    PositionData,
    AccountData,
    ContractData,
    OrderRequest,
    CancelRequest,
    SubscribeRequest,
)
from enum import Enum, unique


@unique
class PRICETYPE(Enum):
    CLOSE = 0
    OPEN = 1
    HIGH = 2
    LOW = 3
    MEDIAN = 4 #中间值（高+低）/2
    TYPICAL = 5 #典型价格（高+低+收盘价）/3
    WEIGHTED = 6 #平均价格（高+低+收盘价格+开盘价格）/4
    AMOUNT = 7 #成交额
    VOLUME = 8 #成交量
    TICKVOLUME = 9 #跳动量
    AVPRICE = 10 #平均价（成交额/成交量）

@unique
class MATYPE(Enum):
    SMA = 0 #简单移动平均线 (SMA)：Simple Moving Average
    EMA = 1 #指数移动平均线 (EMA)：Exponential MA
    SMMA = 2 #通畅移动平均线 (SMMA)：Smoothed MA
    LWMA = 3 #线性权数移动平均线 (LWMA)：Linear Weighted MA
    DMA = 4 #动态移动平均线 Dynamic Moving Average
    #MDOE_TMA = 5 #递归移动平均
    #MODE_WMA = 6 #加权移动平均

class CMTApi:
    """
    Client for MTApi.
    """

    def __init__(self):
        """"""
        self.api = MTApi()
        self.api.on_exchange_update = self.on_exchange_update
        self.api.on_product_update = self.on_product_update
        self.api.on_commodity_update = self.on_commodity_update

    def Start(self, xml, xmlflag):
        self.api.Start(xml, xmlflag)

    def Stop(self):
        self.api.Stop()

    def Subscribe(self, req: SubscribeRequest):
        """"""
        pass

    def SendOrder(self, req: OrderRequest):
        """"""
        pass

    def CancelOrder(self, req: CancelRequest):
        """"""
        pass

    def QueryAccount(self):
        """"""
        pass

    def QueryPosition(self):
        """"""
        pass

    def on_exchange_update(self, dataset, flag):
        #print('on_exchange_update: ', dataset, flag)
        pass

    def on_product_update(self, dataset, flag):
        #print('OnFrontDisconnected: ', dataset, flag)
        pass

    def on_commodity_update(self, dataset, flag):
        #print('on_commodity_update: ', dataset, flag)
        tick = TickData(
            symbol=symbol,
            exchange=exchange)
        self.on_event(EVENT_TICK, tick)
        self.on_event(EVENT_TICK + tick.vt_symbol, tick)

    def sma(self, d, n, array=False):
        """
        Simple moving average.
        """
        result = self.api.Ref("MA", { 'applied_price':PRICETYPE.CLOSE, 'ma_period':n, 'ma_method':MATYPE.SMA }, d)
        if array:
            return result.MA()
        return result.MA()[-1]

    # def std(self, n, array=False):
    #     """
    #     Standard deviation
    #     """
    #     result = talib.STDDEV(self.close, n)
    #     if array:
    #         return result
    #     return result[-1]

    # def cci(self, n, array=False):
    #     """
    #     Commodity Channel Index (CCI).
    #     """
    #     result = talib.CCI(self.high, self.low, self.close, n)
    #     if array:
    #         return result
    #     return result[-1]

    # def atr(self, n, array=False):
    #     """
    #     Average True Range (ATR).
    #     """
    #     result = talib.ATR(self.high, self.low, self.close, n)
    #     if array:
    #         return result
    #     return result[-1]

    # def rsi(self, n, array=False):
    #     """
    #     Relative Strenght Index (RSI).
    #     """
    #     result = talib.RSI(self.close, n)
    #     if array:
    #         return result
    #     return result[-1]

    def macd(self, d, fast_period, slow_period, signal_period, array=False):
        """
        MACD.
        """
        result = self.api.Ref("MACD", { 'applied_price':PRICETYPE.CLOSE, 'fast_period':fast_period, 'slow_period':slow_period, 'slow_period':signal_period }, d)
        if array:
            return result.MACD(), result.DIF(), result.DEA()
        return result.MACD()[-1], result.DIF()[-1], result.DEA[-1]

    # def adx(self, n, array=False):
    #     """
    #     ADX.
    #     """
    #     result = talib.ADX(self.high, self.low, self.close, n)
    #     if array:
    #         return result
    #     return result[-1]

    # def boll(self, n, dev, array=False):
    #     """
    #     Bollinger Channel.
    #     """
    #     mid = self.sma(n, array)
    #     std = self.std(n, array)

    #     up = mid + std * dev
    #     down = mid - std * dev

    #     return up, down

    # def keltner(self, n, dev, array=False):
    #     """
    #     Keltner Channel.
    #     """
    #     mid = self.sma(n, array)
    #     atr = self.atr(n, array)

    #     up = mid + atr * dev
    #     down = mid - atr * dev

    #     return up, down

    # def donchian(self, n, array=False):
    #     """
    #     Donchian Channel.
    #     """
    #     up = talib.MAX(self.high, n)
    #     down = talib.MIN(self.low, n)

    #     if array:
    #         return up, down
    #     return up[-1], down[-1]

    def on_trade(self, trade: TradeData):
        """
        Trade event push.
        Trade event of a specific vt_symbol is also pushed.
        """
        # self.on_event(EVENT_TRADE, trade)
        # self.on_event(EVENT_TRADE + trade.vt_symbol, trade)
        pass

    def on_order(self, order: OrderData):
        """
        Order event push.
        Order event of a specific vt_orderid is also pushed.
        """
        # self.on_event(EVENT_ORDER, order)
        # self.on_event(EVENT_ORDER + order.vt_orderid, order)
        pass

    def on_position(self, position: PositionData):
        """
        Position event push.
        Position event of a specific vt_symbol is also pushed.
        """
        # self.on_event(EVENT_POSITION, position)
        # self.on_event(EVENT_POSITION + position.vt_symbol, position)
        pass

    def on_account(self, account: AccountData):
        """
        Account event push.
        Account event of a specific vt_accountid is also pushed.
        """
        # self.on_event(EVENT_ACCOUNT, account)
        # self.on_event(EVENT_ACCOUNT + account.vt_accountid, account)
        pass



mtapi = CMTApi()
