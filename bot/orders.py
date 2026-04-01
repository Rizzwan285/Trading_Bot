from bot.client import get_client
from bot.logging_config import setup_logger
from binance.exceptions import BinanceAPIException
import time
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
#placing oco order
def place_oco(sym,side,qty,price,stop_price):
 my_log.info(f"placing oco for {sym} {side} {qty} price {price} stop {stop_price}")
 try:
  r1=bot_client.futures_create_order(symbol=sym,side=side,type='LIMIT',timeInForce='GTC',quantity=qty,price=price)
  r2=bot_client.futures_create_order(symbol=sym,side=side,type='STOP_MARKET',timeInForce='GTC',quantity=qty,stopPrice=stop_price)
  my_log.info(f"oco success {r1} {r2}")
  return {"orderId":"multiple","status":"OCO_PLACED","executedQty":0,"avgPrice":0,"symbol":sym}
 except Exception as e:
  my_log.error(f"oco error {e}")
  raise e
#placing twap order
def place_twap(sym,side,qty):
 my_log.info(f"placing twap for {sym} {side} {qty}")
 try:
  total_chunks=3
  chunk_qty=round(float(qty)/total_chunks,3)
  for i in range(total_chunks):
   bot_client.futures_create_order(symbol=sym,side=side,type='MARKET',quantity=chunk_qty)
   if i<total_chunks-1:
    time.sleep(1)
  my_log.info(f"twap success")
  return {"orderId":"twap","status":"TWAP_DONE","executedQty":qty,"avgPrice":0,"symbol":sym}
 except Exception as e:
  my_log.error(f"twap error {e}")
  raise e
#placing grid order
def place_grid(sym,side,qty,price):
 my_log.info(f"placing grid for {sym} {side} {qty} around {price}")
 try:
  grids=3
  chunk_qty=round(float(qty)/grids,3)
  for i in range(grids):
   p=float(price)*(1+(i*0.01)) if side=='SELL' else float(price)*(1-(i*0.01))
   bot_client.futures_create_order(symbol=sym,side=side,type='LIMIT',timeInForce='GTC',quantity=chunk_qty,price=round(p,2))
  my_log.info(f"grid success")
  return {"orderId":"grid","status":"GRID_PLACED","executedQty":0,"avgPrice":0,"symbol":sym}
 except Exception as e:
  my_log.error(f"grid error {e}")
  raise e
