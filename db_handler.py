import sqlite3

from models import Expense
from tkinter import messagebox


class DBHandler:

    def __init__(self, db_name='expenses.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()


    def create_table(self):
        try:
            with self.conn:
                self.conn.execute("""
                    CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT NOT NULL,
                        amount REAL NOT NULL,
                        timestamp TEXT NOT NULL
                        )
                                        """)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", str(e))



    def insert_expenses(self, expense:Expense):
        try:
            with self.conn:
                self.conn.execute("INSERT INTO expenses (description, amount, timestamp) values (?,?,?)",(expense.description, expense.amount, expense.timestamp))
        except sqlite3.Error as e:
            messagebox.showerror("Insert Error: ", str(e))



    def fetch_expenses(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT id, description, amount, timestamp FROM expenses ORDER BY timestamp DESC")
            return cur.fetchall()
        except sqlite3.Error as e:
            messagebox.showerror("Fetch Error: ", str(e))
            return []
        


    def delete_expense(self, expense_id):
        try:
            with self.conn:
                self.conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        except sqlite3.Error as e:
            messagebox.showerror("Delete Error: ", str(e))



    
        



    



