## Add `.env` file
To use this library you should add `.env` file in the root directory.
Template for `.env` file:
```
TRADELOCKER_BASE_URL=<TRADE_LOCKER_BASE_URL>

TRADELOCKER_EMAIL=<TRADE_LOCKER_ACCOUNT_EMAIL>
TRADELOCKER_PASSWORD=<TRADE_LOCKER_ACCOUNT_PASSWORD>
TRADELOCKER_SERVER=<TRADE_LOCKER_SERVER>

MT5_TERMINAL_PATH=<MT5_TERMINAL_PATH>

MT5_ACCOUNT_NUMBER=<MT5_ACCOUNT_NUMBER>
MT5_PASSWORD=<MT5_PASSWORD>
MT5_SERVER=<MT5_SERVER>
```
## Build
```
pip install -r requirements.txt 
```
## Test
on Ubuntu
```
python3 trade_locker/test.py
```
