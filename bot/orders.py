from bot.client import get_client
from bot.logging_config import setup_logger
from binance.exceptions import BinanceAPIException
#initializing logger
my_log=setup_logger()
#getting client
bot_client=get_client()
#placing market order
def place_market_order(sym,side,qty):
 my_log.info(f"placing market order for {sym} {side} {qty}")
 try:
  res=bot_client.futures_create_order(symbol=sym,side=side,type='MARKET',quantity=qty)
  my_log.info(f"order success {res}")
  return res
 except BinanceAPIException as e:
  my_log.error(f"api error {e}")
  raise e
 except Exception as e:
  my_log.error(f"error {e}")
  raise e
#placing limit order
def place_limit_order(sym,side,qty,price):
 my_log.info(f"placing limit order for {sym} {side} {qty} at {price}")
 try:
  res=bot_client.futures_create_order(symbol=sym,side=side,type='LIMIT',timeInForce='GTC',quantity=qty,price=price)
  my_log.info(f"order success {res}")
  return res
 except BinanceAPIException as e:
  my_log.error(f"api error {e}")
  raise e
 except Exception as e:
  my_log.error(f"error {e}")
  raise e
#placing stop limit
def place_stop_limit(sym,side,qty,price,stop_price):
 my_log.info(f"placing stop limit for {sym} {side} {qty} price {price} stop {stop_price}")
 try:
  res=bot_client.futures_create_order(symbol=sym,side=side,type='STOP',timeInForce='GTC',quantity=qty,price=price,stopPrice=stop_price)
  my_log.info(f"order success {res}")
  return res
 except BinanceAPIException as e:
  my_log.error(f"api error {e}")
  raise e
 except Exception as e:
  my_log.error(f"error {e}")
  raise e
