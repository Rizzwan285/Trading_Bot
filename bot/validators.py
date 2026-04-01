#validating inputs
def check_order(sym,side,kind,qty,price,stop_price):
 if not sym:
  raise ValueError("symbol is required")
 if side not in ['BUY','SELL']:
  raise ValueError("side must be BUY or SELL")
 if kind not in ['MARKET','LIMIT','STOP_LIMIT','OCO','TWAP','GRID']:
  raise ValueError("type must be MARKET LIMIT STOP_LIMIT OCO TWAP GRID")
 if float(qty)<=0:
  raise ValueError("quantity must be positive")
 if kind in ['LIMIT','STOP_LIMIT','OCO','GRID']:
  if not price or float(price)<=0:
   raise ValueError("price is required for this order type")
 if kind in ['STOP_LIMIT','OCO']:
  if not stop_price or float(stop_price)<=0:
   raise ValueError("stop price is required for this order type")
 return True
