import os

from dotenv import load_dotenv

from trade_locker_user import TradeLockerUser


load_dotenv()


def display_accounts():
    trade_locker_user = TradeLockerUser(
        email=os.environ["TRADELOCKER_EMAIL"],
        password=os.environ["TRADELOCKER_PASSWORD"],
        server=os.environ["TRADELOCKER_SERVER"]
    )
    trade_locker_user.assign_jwt()

    for acc in trade_locker_user.get_all_accounts():
        msg = ''.join(f'{key}: {acc[key]}\n' for key in acc)
        print(msg, flush=True)



if __name__ == "__main__":
    display_accounts()
