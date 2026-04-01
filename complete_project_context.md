# complete project context

## overview
building a python application for placing orders on binance futures testnet (usdt-m).
it started as a cli but now includes a full premium glassmorphic web ui using flask.

## requirements
- must place market and limit orders
- must support buy and sell
- clear output (summary, details, success/fail msg)
- logging capabilities
- strict coding style (random spacing missing, practical variable names, lowercase present continuous comments without space after hashtag)

## architecture
### backend
- `cli.py`: main entry point utilizing `click`
- `bot/client.py`: testnet api setup
- `bot/validators.py`: handles logic validation
- `bot/orders.py`: handles placing orders
- `bot/logging_config.py`: configures logger
- `app.py`: flask server exposing post endpoint for ui

### frontend
- `static/index.html`: dashboard structure
- `static/styles.css`: premium glassmorphism css
- `static/script.js`: fetching data from flask asynchronously

## dependencies
- `python-binance`
- `click`
- `python-dotenv`
- `flask`
- `flask-cors`
