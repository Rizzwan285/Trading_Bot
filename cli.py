import click
from bot.validators import check_order
from bot.orders import place_market_order,place_limit_order,place_stop_limit
#setting up cli
@click.group()
def my_cli():
 pass
#adding place order command
@my_cli.command()
@click.option('--symbol',required=True,help='trading symbol')
@click.option('--side',required=True,help='buy or sell')
@click.option('--type','order_type',required=True,help='market limit stop_limit')
@click.option('--qty',required=True,help='order quantity')
@click.option('--price',help='order price')
@click.option('--stop-price',help='stop price')
def place_order(symbol,side,order_type,qty,price,stop_price):
 symbol=symbol.upper()
 side=side.upper()
 order_type=order_type.upper()
 #validating input
 check_order(symbol,side,order_type,qty,price,stop_price)
 #running order
 try:
  if order_type=='MARKET':
   res=place_market_order(symbol,side,qty)
  elif order_type=='LIMIT':
   res=place_limit_order(symbol,side,qty,price)
  elif order_type=='STOP_LIMIT':
   res=place_stop_limit(symbol,side,qty,price,stop_price)
  click.echo("order placed successfully")
  click.echo(res)
 except Exception as e:
  click.echo(f"failed placing order {e}")
if __name__=='__main__':
 my_cli()
