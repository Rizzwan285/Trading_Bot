import os
from dotenv import load_dotenv
from binance.client import Client
#loading env variables
load_dotenv()
#getting api credentials
client_key=os.getenv('client_key')
secret_code=os.getenv('secret_code')
#creating binance client
def get_client():
 return Client(api_key=client_key,api_secret=secret_code,testnet=True)
