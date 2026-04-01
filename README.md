# Binance Futures Testnet Bot

Hey there! This is a quick python cli tool i put together to place orders on the binance futures testnet. It uses the python-binance package under the hood and click for the command line stuff.

Right now it supports market, limit, and stop limit orders.

## What you need

Before running anything you need to get some testnet api keys from binance. Go to the binance futures testnet site, make an account and grab your keys.

Make sure you have python 3 installed.

## Setup

1. Clone this or just open the folder
2. Make a virtual env: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate` 
4. Install the requirements: `pip install -r requirements.txt`

You also need to make a `.env` file in the same folder as `cli.py`. It should look exactly like this:

```
client_key=your_api_key
secret_code=your_secret_key
```

## How to use it

It's pretty straightforward. open your terminal and use the `cli.py` script.

To place a market order (just buys at whatever the current price is):
`python cli.py place-order --symbol BTCUSDT --side BUY --type MARKET --qty 0.005`

For a limit order (you set the price):
`python cli.py place-order --symbol BTCUSDT --side SELL --type LIMIT --qty 0.005 --price 90000`

For a stop limit order (has a stop price and a limit price):
`python cli.py place-order --symbol BTCUSDT --side BUY --type STOP_LIMIT --qty 0.005 --price 60000 --stop-price 55000`

## Notes
- This only works on the testnet so you wont lose real money
- I assumed you have enough fake usdt to place these orders
- The output logs are saved to `bot.log` automatically so you can see what happened

Let me know if you run into any issues.