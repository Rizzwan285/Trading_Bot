# Application Task – Python Developer (Trading Bot on Binance Futures Testnet)

**Estimated time:** Less than 60 minutes

---

Thanks for applying. As the first step in our hiring process, please complete the task below. Candidates who meet the acceptance criteria will be shortlisted for an interview.

---

## Objective

Create a small Python application that can place orders on **Binance Futures Testnet (USDT-M)** and provide a clean, reusable structure with proper logging and error handling.

---

## Setup

1. Register and activate a [Binance Futures Testnet](https://testnet.binancefuture.com) account.
2. Generate API credentials.
3. Use this testnet base URL for all API interactions: `https://testnet.binancefuture.com`
4. You may use either:
   - `python-binance` library, **or**
   - Direct REST calls (`requests` / `httpx`)

---

## Core Requirements (Must-Have)

**Language:** Python 3.x

Your app must:

### 1. Order Placement

Place **Market** and **Limit** orders on Binance Futures Testnet (USDT-M). Support both sides: **BUY** and **SELL**.

### 2. CLI Input & Validation

Accept and validate user input via CLI (e.g., `argparse` / `Typer` / `Click`):

| Parameter    | Description                    |
| ------------ | ------------------------------ |
| `symbol`     | e.g., `BTCUSDT`               |
| `side`       | `BUY` / `SELL`                |
| `order type` | `MARKET` / `LIMIT`            |
| `quantity`   | Order quantity                 |
| `price`      | Required for `LIMIT` orders   |

### 3. Clear Output

Print the following to the console:

- Order request summary
- Order response details (`orderId`, `status`, `executedQty`, `avgPrice` if available)
- Success / failure message

### 4. Code Quality

Implement:

- **Structured code** — separate client/API layer and command/CLI layer
- **Logging** of API requests, responses, and errors to a log file
- **Exception handling** — invalid input, API errors, network failures

---

## Deliverables

Please submit:

### 1. Source Code

A **public GitHub repository** (preferred) OR a **zip folder** containing:

- Source code
- `README.md` with:
  - Setup steps
  - How to run examples
  - Any assumptions
- `requirements.txt` (or `pyproject.toml`)

### 2. Log Files

Log files from at least:

- One **MARKET** order
- One **LIMIT** order

---

## Bonus (Optional — Choose Any One)

- Add a third order type: **Stop-Limit** / **OCO** / **TWAP** / **Grid**
- Add an **enhanced CLI UX** (menus, prompts, validation messages)
- Add a **lightweight UI** (optional)

---

## Suggested Project Structure (Optional)

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py            # Binance client wrapper
│   ├── orders.py            # Order placement logic
│   ├── validators.py        # Input validation
│   └── logging_config.py
├── cli.py                   # CLI entry point
├── README.md
└── requirements.txt
```

---

## Evaluation Criteria

| Criteria                        | What We Grade                              |
| ------------------------------- | ------------------------------------------ |
| **Correctness**                 | Places orders successfully on testnet      |
| **Code Quality**                | Readability, structure, reuse              |
| **Validation + Error Handling** | Robust input checks and graceful failures  |
| **Logging Quality**             | Useful, not noisy                          |
| **README + Instructions**       | Clear setup and runnable examples          |

---

## How to Apply

> **PLEASE SUBMIT THROUGH THE GOOGLE FORM DOC SHARED — NOT BY EMAIL**

We'll notify shortlisted candidates by **Saturday** after submission.

---

**Thanks,**
Sonika
Primetrade.ai Hiring Team
