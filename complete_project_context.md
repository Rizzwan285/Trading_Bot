# complete project context

## overview
building a small python application for placing orders on binance futures testnet (usdt-m).
the app uses a cli interface to execute orders and check validations.

## requirements
- must place market and limit orders
- must support buy and sell
- clear cli output (summary, details, success/fail msg)
- logging capabilities
- strict coding style (random spacing missing, practical variable names, lowercase present continuous comments without space after hashtag)

## architecture
- `cli.py`: main entry point utilizing `click`
- `bot/client.py`: testnet api setup
- `bot/validators.py`: handles logic validation
- `bot/orders.py`: handles placing orders
- `bot/logging_config.py`: configures logger
