import MetaTrader5 as mt5

from exceptions import MT5Exception


class MetaTraderTerminal:
    def __init__(self, path):
        self.path = path

    def connect(self):
        if not mt5.initialize(self.path):
            raise MT5Exception("can't connect to metatrader5 terminal!")

    def login_into_account(self, account_number, password, server):
        if not mt5.login(account_number, password, server):
            raise MT5Exception("authorization failed!")

    def display_account_info(self):
        info = mt5.account_info()
        if info is None:
            raise MT5Exception("failed getting account info!")

        print(
            f'{"-"*10} Account info {"-"*10}\n'
            f'Account number:   {info.login}\n'
            f'Balance:          {info.balance} {info.currency}\n'
        )

    def get_buy_order_request(
        self, *, symbol, lot, sl=None, tp=None, comment=None
    ):
        request = {
            'action': mt5.TRADE_ACTION_DEAL,
            'symbol': symbol,
            'volume': lot,
            'type': mt5.ORDER_TYPE_BUY,
            'deviation': 100,
            'price': mt5.symbol_info_tick(symbol).ask,
            'type_time': mt5.ORDER_TIME_GTC,
            'type_filling': mt5.ORDER_FILLING_RETURN
        }

        if sl is not None:
            request['sl'] = sl

        if tp is not None:
            request['tp'] = tp

        if comment is not None:
            request['comment'] = comment

        return request

    def order_buy(
        self, *, symbol, lot, sl=None, tp=None, comment=None
    ):
        result = mt5.order_send(self.get_buy_order_request(
            symbol=symbol, sl=sl, tp=tp, lot=lot, comment=comment
        ))
        if result is None:
            raise MT5Exception("failed to place order!")

        if not result.deal:
            raise MT5Exception(f'comment from server "{result.comment}"')
