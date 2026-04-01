# Binance Futures Testnet Trading Bot

A Python application for placing orders on the Binance Futures Testnet (USDT-M). Built with `python-binance` for API interactions, featuring both a `click` powered CLI and a stunning premium Web UI powered by `Flask`.

Currently supports **Market**, **Limit**, and **Stop-Limit** orders.

---

## Prerequisites

Before running the bot, ensure you have the following:
* **Python 3.x** installed.
* **Binance Futures Testnet Account:** Create one at the [Binance Futures Testnet](https://testnet.binancefuture.com/) site.
* **Testnet API Keys:** Generate your API Key and Secret Key from your testnet account dashboard.

---

## Setup & Installation

1. **Clone or open the project directory:**
   Navigate to the folder containing the project files.

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**
   * **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   * **Windows:**
     ```bash
     venv\Scripts\activate
     ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(This includes `python-binance`, `click`, `python-dotenv`, `flask`, and `flask-cors`)*

5. **Configure your environment variables:**
   Create a `.env` file in the same directory as `cli.py` and `app.py`, adding your testnet credentials exactly like this:
   ```env
   client_key=your_api_key
   secret_code=your_secret_key
   ```

---

## Running the Premium Web UI

You can now use a beautiful, modern graphical interface to trade!

1. **Start the Flask Server:**
   ```bash
   python app.py
   ```
2. **Open your browser:**
   Navigate to `http://localhost:5000` to view the trading dashboard.
3. **Execute Trades:**
   Select your parameters (Market, Limit, Stop-Limit) and click submit. The UI will instantly display success or failure responses directly from the API.

---

## Running the CLI Script

If you prefer the command line, use the `cli.py` script.

### Market Order
Executes a buy or sell immediately at the current market price.
```bash
python cli.py place-order --symbol BTCUSDT --side BUY --type MARKET --qty 0.005
```

### Limit Order
Places an order to buy or sell at a specific price or better.
```bash
python cli.py place-order --symbol BTCUSDT --side SELL --type LIMIT --qty 0.005 --price 90000
```

### Stop-Limit Order
Combines a stop trigger and a limit order. Requires both a price and a stop-price.
```bash
python cli.py place-order --symbol BTCUSDT --side BUY --type STOP_LIMIT --qty 0.005 --price 60000 --stop-price 55000
```

---

## Important Notes

* **Testnet Only:** This bot is strictly configured for the Binance Testnet. No real funds are used or at risk.
* **Account Balance:** Ensure your testnet account is funded with sufficient mock USDT to place these orders.
* **Logging:** All API events, order executions, and errors (from both the CLI and Web UI) are automatically recorded in `bot.log` for debugging and review.