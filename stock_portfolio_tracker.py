# ============================================
#   Stock Portfolio Tracker
#   Task 2 - Key Concepts: dictionary, input/output,
#             basic arithmetic, file handling
# ============================================

# Hardcoded stock price dictionary (in USD)
STOCK_PRICES = {
    "AAPL":  180,
    "TSLA":  250,
    "GOOGL": 175,
    "MSFT":  420,
    "AMZN":  195,
    "NVDA":  850,
    "META":  500,
    "NFLX":  680,
    "AMD":   165,
    "RELIANCE": 2950,
    "TCS":   3900,
    "INFY":  1820,
    "WIPRO":  530,
    "HDFCBANK": 1680,
}


def display_available_stocks():
    """Display all available stocks and their prices."""
    print("\n" + "=" * 40)
    print("   AVAILABLE STOCKS")
    print("=" * 40)
    print(f"{'Symbol':<12} {'Price':>10}")
    print("-" * 40)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<12} ${price:>9,.2f}")
    print("=" * 40)


def get_portfolio_from_user():
    """Prompt the user to enter stock names and quantities."""
    portfolio = {}

    print("\nEnter your stock holdings.")
    print("Type 'done' when finished.\n")

    while True:
        symbol = input("Stock symbol (or 'done'): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"  '{symbol}' not found. Available: {', '.join(STOCK_PRICES.keys())}\n")
            continue

        try:
            qty = float(input(f"  Quantity of {symbol}: ").strip())
            if qty <= 0:
                print("  Quantity must be greater than 0.\n")
                continue
        except ValueError:
            print("  Invalid quantity. Please enter a number.\n")
            continue

        # Accumulate if stock entered more than once
        portfolio[symbol] = portfolio.get(symbol, 0) + qty
        print(f"  Added: {qty} x {symbol} @ ${STOCK_PRICES[symbol]:,.2f}\n")

    return portfolio


def calculate_portfolio(portfolio):
    """Calculate value per holding and total investment."""
    results = []
    total = 0.0

    for symbol, qty in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * qty
        total += value
        results.append({
            "symbol": symbol,
            "price":  price,
            "qty":    qty,
            "value":  value,
        })

    # Sort by value descending
    results.sort(key=lambda x: x["value"], reverse=True)
    return results, total


def display_portfolio(results, total):
    """Print a formatted portfolio summary to the console."""
    print("\n" + "=" * 55)
    print("   PORTFOLIO SUMMARY")
    print("=" * 55)
    print(f"{'Symbol':<10} {'Price':>10} {'Qty':>8} {'Value':>14}")
    print("-" * 55)

    for row in results:
        print(f"{row['symbol']:<10} ${row['price']:>9,.2f} "
              f"{row['qty']:>8.4g} ${row['value']:>13,.2f}")

    print("=" * 55)
    print(f"{'TOTAL INVESTMENT':<30} ${total:>13,.2f}")
    print("=" * 55)

    if results:
        top = results[0]
        pct = (top['value'] / total * 100) if total else 0
        print(f"\n  Largest position : {top['symbol']} "
              f"(${top['value']:,.2f} — {pct:.1f}% of portfolio)")


def save_to_csv(results, total, filename="portfolio.csv"):
    """Save the portfolio to a CSV file."""
    with open(filename, "w") as f:
        f.write("Symbol,Price,Quantity,Value\n")
        for row in results:
            f.write(f"{row['symbol']},{row['price']},{row['qty']:.4g},{row['value']:.2f}\n")
        f.write(f"\nTotal,,,{total:.2f}\n")
    print(f"\n  CSV saved  -> {filename}")


def save_to_txt(results, total, filename="portfolio.txt"):
    """Save the portfolio to a plain-text file."""
    from datetime import date
    with open(filename, "w") as f:
        f.write(f"Stock Portfolio Report — {date.today()}\n")
        f.write("=" * 55 + "\n")
        f.write(f"{'Symbol':<10} {'Price':>10} {'Qty':>8} {'Value':>14}\n")
        f.write("-" * 55 + "\n")
        for row in results:
            f.write(f"{row['symbol']:<10} ${row['price']:>9,.2f} "
                    f"{row['qty']:>8.4g} ${row['value']:>13,.2f}\n")
        f.write("=" * 55 + "\n")
        f.write(f"{'Total Investment':<30} ${total:>13,.2f}\n")
    print(f"  TXT saved  -> {filename}")


def ask_save(results, total):
    """Ask the user if they want to save the results."""
    print("\nWould you like to save the results?")
    print("  1. Save as CSV")
    print("  2. Save as TXT")
    print("  3. Save both")
    print("  4. Skip")

    choice = input("\nChoice (1/2/3/4): ").strip()

    if choice == "1":
        save_to_csv(results, total)
    elif choice == "2":
        save_to_txt(results, total)
    elif choice == "3":
        save_to_csv(results, total)
        save_to_txt(results, total)
    else:
        print("  No file saved.")


# ── Main Program ─────────────────────────────
def main():
    print("\n╔══════════════════════════════════╗")
    print("║    STOCK PORTFOLIO TRACKER       ║")
    print("╚══════════════════════════════════╝")

    display_available_stocks()

    portfolio = get_portfolio_from_user()

    if not portfolio:
        print("\nNo stocks entered. Exiting.")
        return

    results, total = calculate_portfolio(portfolio)
    display_portfolio(results, total)
    ask_save(results, total)

    print("\nThank you for using the Stock Portfolio Tracker!\n")


if __name__ == "__main__":
    main()
...
... save = input("\nSave to file? (txt/csv/no): ").lower()
...
... if save == "txt":
...
...     with open("portfolio.txt", "w") as f:
...
...         for stock, qty in portfolio.items():
...
...             value = STOCK_PRICES[stock] * qty
...
...             f.write(f"{stock} x{qty} = ${value:,.2f}\n")
...
...         f.write(f"\nTotal: ${total:,.2f}\n")
...
...     print("Saved to portfolio.txt")
...
... elif save == "csv":
...
...     with open("portfolio.csv", "w") as f:
...
...         f.write("Symbol,Price,Quantity,Value\n")
...
...         for stock, qty in portfolio.items():
...
...             f.write(f"{stock},{STOCK_PRICES[stock]},{qty},{STOCK_PRICES[stock]*qty:.2f}\n")
...
...         f.write(f"Total,,,{total:.2f}\n")
...
...     print("Saved to portfolio.csv")




