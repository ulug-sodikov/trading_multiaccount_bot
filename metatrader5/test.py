import os

from dotenv import load_dotenv

from metatrader5 import MetaTraderTerminal


load_dotenv()

# WARNING: DO NOT EXECUTE THIS WITH REAL ACCOUNT
def do_some_operations():
    mt5_terminal = MetaTraderTerminal(os.environ['MT5_TERMINAL_PATH'])
    mt5_terminal.connect()
    mt5_terminal.login_into_account(
        int(os.environ['MT5_ACCOUNT_NUMBER']),
        os.environ['MT5_ACCOUNT_PASSWORD'],
        os.environ['MT5_SERVER']
    )
    mt5_terminal.display_account_info()
    mt5_terminal.order_buy(symbol="XAUUSD", lot=0.1, comment='some')

# WARNING: DO NOT EXECUTE THIS WITH REAL ACCOUNT
if __name__ == '__main__':
    do_some_operations()
