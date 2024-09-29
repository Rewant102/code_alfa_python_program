import tkinter as tk
from tkinter import messagebox
import yfinance as yf

# Stock Portfolio Tracker Class
class StockPortfolioTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Portfolio Tracker")
        self.root.geometry("400x300")

        # Portfolio dictionary to store stock symbols and number of shares
        self.portfolio = {}

        # Labels and Entry widgets for stock symbol and number of shares
        self.stock_label = tk.Label(root, text="Stock Symbol (e.g., AAPL):")
        self.stock_label.pack()

        self.stock_entry = tk.Entry(root)
        self.stock_entry.pack()

        self.shares_label = tk.Label(root, text="Number of Shares:")
        self.shares_label.pack()

        self.shares_entry = tk.Entry(root)
        self.shares_entry.pack()

        # Add, Remove, and Track buttons
        self.add_button = tk.Button(root, text="Add Stock", command=self.add_stock)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text="Remove Stock", command=self.remove_stock)
        self.remove_button.pack()

        self.track_button = tk.Button(root, text="Track Portfolio", command=self.track_portfolio)
        self.track_button.pack()

        # Label to show portfolio value and stock details
        self.output_label = tk.Label(root, text="", wraplength=350)
        self.output_label.pack()

    # Function to add stock to the portfolio
    def add_stock(self):
        symbol = self.stock_entry.get().upper()
        try:
            shares = int(self.shares_entry.get())
            if symbol and shares > 0:
                self.portfolio[symbol] = self.portfolio.get(symbol, 0) + shares
                messagebox.showinfo("Success", f"Added {shares} shares of {symbol}.")
                self.stock_entry.delete(0, tk.END)
                self.shares_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Enter valid stock symbol and shares.")
        except ValueError:
            messagebox.showwarning("Input Error", "Shares must be an integer.")

    # Function to remove stock from the portfolio
    def remove_stock(self):
        symbol = self.stock_entry.get().upper()
        if symbol in self.portfolio:
            del self.portfolio[symbol]
            messagebox.showinfo("Success", f"Removed {symbol} from the portfolio.")
        else:
            messagebox.showwarning("Input Error", "Stock not found in portfolio.")
        self.stock_entry.delete(0, tk.END)

    # Function to track the portfolio and display stock prices and total value
    def track_portfolio(self):
        if not self.portfolio:
            messagebox.showinfo("Portfolio Empty", "Your portfolio is empty.")
            return

        total_value = 0
        output = []
        for symbol, shares in self.portfolio.items():
            stock = yf.Ticker(symbol)
            try:
                price = stock.history(period='1d')['Close'][0]
                value = shares * price
                total_value += value
                output.append(f"{symbol}: {shares} shares @ ${price:.2f} = ${value:.2f}")
            except IndexError:
                messagebox.showwarning("Error", f"Could not fetch data for {symbol}.")
                continue

        output.append(f"\nTotal Portfolio Value: ${total_value:.2f}")
        self.output_label.config(text="\n".join(output))

# Main function to run the tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = StockPortfolioTracker(root)
    root.mainloop()
