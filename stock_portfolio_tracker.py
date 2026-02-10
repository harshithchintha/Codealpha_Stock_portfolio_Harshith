# stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "SMSG": 290,
    "NFTY": 260,
}

portfolio = {}
total_investment = 0

n = int(input("How many different stocks do you want to enter? "))

for _ in range(n):
    name = input("Enter stock name (AAPL/TSLA/GOOG/MSFT/SMSG/NFTY): ").upper()
    
    if name not in stock_prices:
        print("Stock not available. Skipping.")
        continue
    
    qty = int(input(f"Enter quantity of {name}: "))
    portfolio[name] = qty

# Calculating total
for name, qty in portfolio.items():
    value = stock_prices[name] * qty
    total_investment += value
    print(f"{name}: {qty} × {stock_prices[name]} = {value}")

print("\nTotal Investment Value =", total_investment)
