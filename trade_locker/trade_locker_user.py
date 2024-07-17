import os
import datetime
from urllib.parse import urljoin

import requests
from dotenv import load_dotenv

from paths import (
    AUTH_JWT_TOKEN_PATH,
    AUTH_JWT_ALL_ACCOUNTS_PATH
)


load_dotenv()
BASE_URL = os.environ["BASE_URL"]


class TradeLockerUser:
    jwt_expire_date_format = '%Y-%m-%dT%H:%M:%S.000Z'

    def __init__(self, email, password, server):
        self.email = email
        self.password = password
        self.server = server
        self.jwt_access_token = None
        self.jwt_refresh_token = None
        self.jwt_expire_date = None

    def get_auth_headers(self):
        if self.jwt_access_token is None:
            raise ValueError('JWT ACCESS TOKEN not initialized!!!')
        
        return {
            'Authorization': f'Bearer {self.jwt_access_token}'
        }

    def get_jwt(self):
        url = urljoin(BASE_URL, AUTH_JWT_TOKEN_PATH)
        data = {
            "email": self.email, 
            "password": self.password, 
            "server": self.server
        }
        jwt_data = requests.post(url, json=data).json()
        expire_date = datetime.datetime.strptime(
            jwt_data["expireDate"], self.jwt_expire_date_format
        )

        return {
            'access_token': jwt_data['accessToken'],
            'refresh_token': jwt_data['refreshToken'],
            'expire_date': expire_date
        }

    def assign_jwt(self):
        jwt = self.get_jwt()
        self.jwt_access_token = jwt['access_token']
        self.jwt_refresh_token = jwt['refresh_token']
        self.jwt_expire_date = jwt['expire_date']
    
    def get_all_accounts(self):
        url = urljoin(BASE_URL, AUTH_JWT_ALL_ACCOUNTS_PATH)
        headers = self.get_auth_headers()
        response = requests.get(url, headers=headers)

        return response.json()['accounts']
