# 📈 Stock Portfolio Tracker

A beginner-friendly Python command-line application that calculates the total investment value of a stock portfolio using hardcoded stock prices.

Built as **Task 2** of a Python learning series — covering core concepts like dictionaries, user input/output, basic arithmetic, and file handling.

---

## 🚀 Features

- View a list of 14 available stocks with their current (hardcoded) prices
- Enter stock symbols and quantities interactively
- Calculates value per holding (`price × quantity`)
- Displays a formatted portfolio summary with grand total
- Identifies your largest position
- Optionally saves results as a **CSV** or **TXT** file

---

## 🧠 Key Python Concepts Used

| Concept | How it's used |
|---|---|
| **Dictionary** | `STOCK_PRICES = {"AAPL": 180, "TSLA": 250, ...}` stores all prices |
| **Input / Output** | `input()` collects stock names and quantities from the user |
| **Basic Arithmetic** | `price × quantity` per stock, summed for the total |
| **Loops** | `while True` loop keeps asking until the user types `done` |
| **Functions** | Code is split into named tasks (`def`) for clarity |
| **File Handling** | Results saved to `.csv` or `.txt` using `open()` and `write()` |

---

## 📦 Available Stocks

| Symbol | Company | Price (USD) |
|---|---|---|
| AAPL | Apple | $180 |
| TSLA | Tesla | $250 |
| GOOGL | Alphabet (Google) | $175 |
| MSFT | Microsoft | $420 |
| AMZN | Amazon | $195 |
| NVDA | NVIDIA | $850 |
| META | Meta Platforms | $500 |
| NFLX | Netflix | $680 |
| AMD | AMD | $165 |
| RELIANCE | Reliance Industries | ₹2950 |
| TCS | Tata Consultancy Services | ₹3900 |
| INFY | Infosys | ₹1820 |
| WIPRO | Wipro | ₹530 |
| HDFCBANK | HDFC Bank | ₹1680 |

> **Note:** Prices are hardcoded for learning purposes and do not reflect live market data.

---

## 🛠️ Installation & Usage

### Prerequisites

- Python 3.x installed on your system

### Run the program

```bash
python stock_portfolio_tracker.py
```

### Example session

```
╔══════════════════════════════════╗
║    STOCK PORTFOLIO TRACKER       ║
╚══════════════════════════════════╝

Available stocks:
AAPL         $180.00
TSLA         $250.00
...

Enter your stock holdings.
Type 'done' when finished.

Stock symbol (or 'done'): AAPL
  Quantity of AAPL: 10
  Added: 10.0 x AAPL @ $180.00

Stock symbol (or 'done'): TSLA
  Quantity of TSLA: 5
  Added: 5.0 x TSLA @ $250.00

Stock symbol (or 'done'): done

=======================================================
   PORTFOLIO SUMMARY
=======================================================
Symbol     Price          Qty         Value
AAPL      $180.00         10      $1,800.00
TSLA      $250.00          5      $1,250.00
=======================================================
TOTAL INVESTMENT               $3,050.00
=======================================================

  Largest position: AAPL ($1,800.00 — 59.0% of portfolio)

Would you like to save the results?
  1. Save as CSV
  2. Save as TXT
  3. Save both
  4. Skip
```

---

## 📁 Output Files

### portfolio.csv
Opens in Excel or Google Sheets.
```
Symbol,Price,Quantity,Value
AAPL,180,10,1800.00
TSLA,250,5,1250.00

Total,,,3050.00
```

### portfolio.txt
Plain text report, opens in any text editor.
```
Stock Portfolio Report — 2025-01-01
=======================================================
Symbol     Price        Qty       Value
AAPL      $180.00       10    $1,800.00
TSLA      $250.00        5    $1,250.00
=======================================================
Total Investment               $3,050.00
```

---

## 📂 Project Structure

```
stock-portfolio-tracker/
│
├── stock_portfolio_tracker.py   # Main program
├── README.md                    # Project documentation
├── portfolio.csv                # Generated output (after running)
└── portfolio.txt                # Generated output (after running)
```

---

## 🔮 Future Improvements

- [ ] Fetch live stock prices using an API (e.g. Yahoo Finance, Alpha Vantage)
- [ ] Support for multiple currencies
- [ ] Add a buy/sell history tracker
- [ ] Build a GUI version using Tkinter or a web app using Flask
- [ ] Add charts to visualize portfolio allocation


---

## 🧑‍💻 Author

Built as part of a Python programming learning journey.  
Feel free to fork, modify, and build on top of this!

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
