# Binance Futures Testnet Trading Bot

A Python application for placing orders on the Binance Futures Testnet (USDT-M). Built with `python-binance` for API interactions, featuring a fully-fledged premium Web UI (`Flask`) and a robust interactive command-line interface (`click`).

Currently supports **Market**, **Limit**, **Stop-Limit**, **OCO**, **TWAP**, and **Grid** order types.

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

You can use a beautifully styled, modern graphical interface to cleanly execute all six types of trades!

1. **Start the Flask Server:**
   ```bash
   python app.py
   ```
2. **Open your browser:**
   Navigate to `http://localhost:5000` to view the primary trading dashboard.
3. **Execute Trades:**
   Select your parameters (Market, Limit, Stop-Limit, OCO, TWAP, or Grid) and click submit. The UI will instantly display success or failure responses cleanly formatted directly from the API.

---

## Running the CLI Script

If you prefer the command line, use the `cli.py` script. The CLI has been natively **enhanced with interactive menus**!

### Interactive Mode (Enhanced UX)
Simply run the script with no arguments. It will wipe your terminal and cleanly launch a step-by-step interactive menu that walks you through formatting your parameters effectively!
```bash
python cli.py
```

### Direct Execution Examples
You can bypass the interactive setup prompts by passing your parameters directly over the terminal:

**Market Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.005
```

**Limit Order:**
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.005 --price 90000
```

**Stop-Limit Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --qty 0.005 --price 60000 --stop-price 55000
```

**OCO Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type OCO --qty 0.005 --price 60000 --stop-price 55000
```

**TWAP Algorithm Order:**
```bash
python cli.py --symbol BTCUSDT --side BUY --type TWAP --qty 0.005
```

**Grid Algorithm Order:**
```bash
python cli.py --symbol BTCUSDT --side SELL --type GRID --qty 0.005 --price 90000
```

---

## Assumptions Made

* **Testnet Only:** This bot is strictly configured for the Binance Testnet. No real funds are used or at risk.
* **Account Balance:** Assumes your testnet account is adequately funded with sufficient mock USDT to facilitate these orders.
* **Algorithmic Simulation:** TWAP and Grid orders are natively simulated locally by slicing the core quantity and executing chunks via basic time-sleep loops or percentage brackets off the master price.
* **Logging:** All API events, order executions, and errors (from both the CLI and Web UI) are inherently recorded inside `bot.log` for clean debugging per the explicit project requirements.