import tkinter as tk
from tkinter import messagebox

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        messagebox.showinfo("Deposit", f"Deposit of {amount} successful. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            messagebox.showerror("Withdrawal", "Insufficient funds.")
        else:
            self.balance -= amount
            messagebox.showinfo("Withdrawal", f"Withdrawal of {amount} successful. New balance is {self.balance}.")

    def get_balance(self):
        messagebox.showinfo("Balance", f"Current balance is {self.balance}.")

class BankApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bank Account")
        self.geometry("300x200")
        self.account = BankAccount(12345, 100)

        self.amount_label = tk.Label(self, text="Amount:")
        self.amount_entry = tk.Entry(self)
        self.deposit_button = tk.Button(self, text="Deposit", command=self.deposit)
        self.withdraw_button = tk.Button(self, text="Withdraw", command=self.withdraw)
        self.balance_button = tk.Button(self, text="Check Balance", command=self.check_balance)

        self.amount_label.pack()
        self.amount_entry.pack()
        self.deposit_button.pack()
        self.withdraw_button.pack()
        self.balance_button.pack()

    def deposit(self):
        amount = float(self.amount_entry.get())
        self.account.deposit(amount)

    def withdraw(self):
        amount = float(self.amount_entry.get())
        self.account.withdraw(amount)

    def check_balance(self):
        self.account.get_balance()

if __name__ == "__main__":
    app = BankApp()
    app.mainloop()