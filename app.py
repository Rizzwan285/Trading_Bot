from flask import Flask,request,jsonify
from flask_cors import CORS
from bot.validators import check_order
from bot.orders import place_market_order,place_limit_order,place_stop_limit
#starting flask server
my_app=Flask(__name__,static_url_path='',static_folder='static')
CORS(my_app)
#serving starting page
@my_app.route('/')
def home():
 return my_app.send_static_file('index.html')
#handling new orders
@my_app.route('/api/order',methods=['POST'])
def handle_trade():
 payload=request.json
 sym=payload.get('symbol','').upper()
 side=payload.get('side','').upper()
 kind=payload.get('type','').upper()
 qty=payload.get('qty')
 price=payload.get('price')
 stop=payload.get('stop_price')
 try:
  #checking inputs
  check_order(sym,side,kind,qty,price,stop)
  #sending orders
  if kind=='MARKET':
   res=place_market_order(sym,side,qty)
  elif kind=='LIMIT':
   res=place_limit_order(sym,side,qty,price)
  elif kind=='STOP_LIMIT':
   res=place_stop_limit(sym,side,qty,price,stop)
  return jsonify({"success":True,"data":res})
 except Exception as err:
  return jsonify({"success":False,"error":str(err)}),400
if __name__=='__main__':
 my_app.run(debug=True,port=5000)
