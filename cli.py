import click
from bot.validators import check_order
from bot.orders import place_market_order,place_limit_order,place_stop_limit,place_oco,place_twap,place_grid
#setting up cli
@click.command()
@click.option('--symbol',help='trading symbol')
@click.option('--side',help='buy or sell')
@click.option('--type','order_type',help='market limit stop_limit oco twap grid')
@click.option('--qty',help='order quantity')
@click.option('--price',help='order price')
@click.option('--stop-price',help='stop price')
def place_order(symbol,side,order_type,qty,price,stop_price):
 #interactive menu if missing args
 if not symbol:
  click.clear()
  click.secho('--- interactive trade menu ---',fg='cyan',bold=True)
  symbol=click.prompt('enter symbol (e.g. BTCUSDT)',type=str)
  side=click.prompt('enter side (BUY/SELL)',type=click.Choice(['BUY','SELL'],case_sensitive=False))
  order_type=click.prompt('enter order type',type=click.Choice(['MARKET','LIMIT','STOP_LIMIT','OCO','TWAP','GRID'],case_sensitive=False))
  qty=click.prompt('enter quantity',type=float)
  if order_type in ['LIMIT','STOP_LIMIT','OCO','GRID']:
   price=click.prompt('enter target price',type=float)
  if order_type in ['STOP_LIMIT','OCO']:
   stop_price=click.prompt('enter stop price',type=float)
 symbol=symbol.upper()
 side=side.upper()
 order_type=order_type.upper()
 #validating input
 try:
  check_order(symbol,side,order_type,qty,price,stop_price)
 except Exception as e:
  click.secho(f"validation error: {e}",fg='red')
  return
 #running order
 try:
  click.secho('executing order...',fg='yellow')
  res=None
  if order_type=='MARKET':
   res=place_market_order(symbol,side,qty)
  elif order_type=='LIMIT':
   res=place_limit_order(symbol,side,qty,price)
  elif order_type=='STOP_LIMIT':
   res=place_stop_limit(symbol,side,qty,price,stop_price)
  elif order_type=='OCO':
   res=place_oco(symbol,side,qty,price,stop_price)
  elif order_type=='TWAP':
   res=place_twap(symbol,side,qty)
  elif order_type=='GRID':
   res=place_grid(symbol,side,qty,price)
  click.secho("order placed successfully",fg='green',bold=True)
  click.echo(res)
 except Exception as e:
  click.secho(f"failed placing order {e}",fg='red',bold=True)
if __name__=='__main__':
 place_order()
