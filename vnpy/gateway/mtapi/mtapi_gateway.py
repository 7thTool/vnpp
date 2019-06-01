"""
"""

from datetime import datetime

from vnpy.mtapi.mtapi import *

from vnpy.trader.constant import (
    Direction,
    Offset,
    Exchange,
    OrderType,
    Product,
    Status,
    OptionType
)
from vnpy.trader.gateway import BaseGateway
from vnpy.trader.object import (
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
from vnpy.trader.utility import get_folder_path
from vnpy.trader.event import EVENT_TIMER

symbol_exchange_map = {}
symbol_name_map = {}
symbol_size_map = {}

class MTApiGateway(BaseGateway):
    """
    VN Trader Gateway for MTApi .
    """

    default_setting = {
        "用户名": "",
        "密码": "",
        "经纪商代码": "",
        "交易服务器": "",
        "行情服务器": "",
        "产品名称": "",
        "授权编码": ""
    }

    def __init__(self, event_engine):
        """Constructor"""
        super(MTApiGateway, self).__init__(event_engine, "MTApi")

    def connect(self, setting: dict):
        """"""
        userid = setting["用户名"]
        password = setting["密码"]
        brokerid = setting["经纪商代码"]
        td_address = setting["交易服务器"]
        md_address = setting["行情服务器"]
        product_info = setting["产品名称"]
        auth_code = setting["授权编码"]
        
        if not td_address.startswith("tcp://"):
            td_address = "tcp://" + td_address
        if not md_address.startswith("tcp://"):
            md_address = "tcp://" + md_address
        
        mtapi.Start(self.event_engine)

        self.init_query()

    def subscribe(self, req: SubscribeRequest):
        """"""
        mtapi.Subscribe(req)

    def send_order(self, req: OrderRequest):
        """"""
        mtapi.SendOrder(req)

    def cancel_order(self, req: CancelRequest):
        """"""
        mtapi.CancelOrder()

    def query_account(self):
        """"""
        mtapi.QueryAccount()

    def query_position(self):
        """"""
        mtapi.QueryPosition()

    def close(self):
        """"""
        mtapi.Stop()

    def write_error(self, msg: str, error: dict):
        """"""
        error_id = error["ErrorID"]
        error_msg = error["ErrorMsg"]
        msg = f"{msg}，代码：{error_id}，信息：{error_msg}"
        self.write_log(msg)

    def process_timer_event(self, event):
        """"""
        self.count += 1
        if self.count < 2:
            return
        self.count = 0
        
        func = self.query_functions.pop(0)
        func()
        self.query_functions.append(func)
        
    def init_query(self):
        """"""
        self.count = 0
        self.query_functions = [self.query_account, self.query_position]
        self.event_engine.register(EVENT_TIMER, self.process_timer_event)
