
vnpp是一套基于MTApi和vnpy的极速Python的开源量化交易系统开发框架，于2015年1月正式发布，在开源社区5年持续不断的贡献下一步步成长为全功能量化交易平台，目前国内外金融机构用户已经超过300家，包括：私募基金、证券自营和资管、期货资管和子公司、高校研究机构、自营交易公司、交易所、Token Fund等。

## 功能特点

1. 全功能量化交易平台（vnpy.trader），整合了多种交易接口，并针对具体策略算法和功能开发提供了简洁易用的API，用于快速构建交易员所需的量化交易应用。

2. 覆盖国内外所有交易品种的交易接口（vnpy.gateway）：

    * CTP(ctp)：国内期货、期权

    * 飞马(femas)：国内期货

    * 宽睿(oes)：国内证券（A股）

    * 中泰XTP(xtp)：国内证券（A股）

    * 富途证券(futu)：港股、美股

    * 老虎证券(tiger)：全球证券、期货、期权、外汇等

    * Interactive Brokers(ib)：全球证券、期货、期权、外汇等

    * BitMEX(bitmex)：数字货币期货、期权、永续合约

    * OKEX合约(okexf)：数字货币期货

    * 火币合约(hbdm)：数字货币期货

    * OKEX(okex)：数字货币现货

    * 火币(huobi)：数字货币现货
    
    * Bitfinex(bitfinex)：数字货币现货

    * 1Token(onetoken)：数字货币券商（现货、期货）

3. 开箱即用的各类量化策略交易应用（vnpy.app）：

    * cta_strategy：CTA策略引擎模块，在保持易用性的同时，允许用户针对CTA类策略运行过程中委托的报撤行为进行细粒度控制（降低交易滑点、实现高频策略）

    * cta_backtester：CTA策略回测模块，无需使用Jupyter Notebook，直接使用图形界面直接进行策略回测分析、参数优化等相关工作

    * algo_trading：算法交易模块，提供多种常用的智能交易算法：TWAP、Sniper、Iceberg、BestLimit等等，支持常用算法配置保存

    * csv_loader：CSV历史数据加载器，用于加载CSV格式文件中的历史数据到平台数据库中，用于策略的回测研究以及实盘初始化等功能，支持自定义数据表头格式

    * data_recorder：行情记录模块，基于图形界面进行配置，根据需求实时录制Tick或者K线行情到数据库中，用于策略回测或者实盘初始化

4. Python交易API接口封装（vnpy.api），提供上述交易接口的底层对接实现。

5. 简洁易用的事件驱动引擎（vnpy.event），作为事件驱动型交易程序的核心。

## 环境准备

* 推荐使用

## 安装步骤

运行以下命令安装：

**Windows**

    install.bat

**Ubuntu**

    bash install.sh


## 使用指南

1. 在[SimNow](http://www.simnow.com.cn/)注册CTP仿真账号，并在[该页面](http://www.simnow.com.cn/product.action)获取经纪商代码以及交易行情服务器地址。

2. 拉取代码

3. 下载并安装Anaconda3，如安装在C:\Anaconda3

4. 在C:\Anaconda3\Lib\site-packages建立vnpy软连接：mklink /D vnpy D:\work\scm\vnpp\vnpy

## 脚本运行

除了基于MTStation的图形化启动方式外，也可以在任意目录下创建run.py，写入以下示例代码：

```Python
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy.gateway.ctp import CtpGateway
from vnpy.app.cta_strategy import CtaStrategyApp
from vnpy.app.cta_backtester import CtaBacktesterApp

def main():
    """Start VN Trader"""
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    
    main_engine.add_gateway(CtpGateway)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()

if __name__ == "__main__":
    main()
```

在该目录下打开CMD（按住Shift->点击鼠标右键->在此处打开命令窗口/PowerShell）后运行下列命令启动VN Trader：

    python run.py


## 项目捐赠

长期维护捐赠清单，请在留言中注明是项目捐赠以及捐赠人的名字。


## 版权说明

MIT




