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

    def get_buy_order_request(self, *, symbol, sl, tp, lot):
        return {
            'action': mt5.TRADE_ACTION_DEAL,
            'symbol': symbol,
            'volume': lot,
            'type': mt5.ORDER_TYPE_BUY,
            'sl': sl,
            'tp': tp,
            'price': mt5.symbol_info_tick(symbol).bid,
            'type_time': mt5.ORDER_TIME_GTC,
            'type_filling': mt5.ORDER_FILLING_RETURN
        }

    def order_buy(self, *, symbol, sl, tp, lot):
        result = mt5.order_send(self.get_buy_order_request(
            symbol=symbol, sl=sl, tp=tp, lot=lot
        ))
        if result is None:
            raise MT5Exception("failed to place order!")

        if not result.deal:
            raise MT5Exception(f'comment from server "{result.comment}"')
