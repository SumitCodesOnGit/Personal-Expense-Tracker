
import tkinter as tk
from tkinter import ttk, messagebox
from models import Expense
from db_handler import DBHandler


class ExpenseTrackerApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("600x400")

        self.db = DBHandler()

        self.create_widgets()
        self.populate_expenses()



    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        tk.Label(frame, text="Description: ").grid(row=0, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(frame, width=30)
        self.desc_entry.grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Amount: ").grid(row=0, column=2, padx=5, pady=5)
        self.amount_entry = tk.Entry(frame,width=15)
        self.amount_entry.grid(row=0, column=3, padx=5)

        tk.Button(frame, text ="Add Expense", command=self.add_expense).grid(row=0, column=4, padx=5)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Description", "Amount", "Timestamp"), show='headings')
        self.tree.heading("ID", text="ID")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Amount", text="Amount")
        self.tree.heading("Timestamp", text="Timestamp")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        tk.Button(frame, text= "Delete Selected", command= self.delete_selected).grid(pady=5)




    def add_expense(self):
        desc = self.desc_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if not desc or not amount:
            messagebox.showwarning("Input Error", "All inputs are required")
            return
        
        try:
            amount = float(amount)
            new_expense = Expense(desc, amount)
            self.db.insert_expenses(new_expense)
            self.populate_expenses()
            self.desc_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Invalid Input", "Amount must be a number")




    def populate_expenses(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for exp in self.db.fetch_expenses():
            self.tree.insert('', tk.END, values=exp)



    def delete_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Selection Error", "Please select a record to delete")
            return
        
        confirm =messagebox.askyesno("Confirm Delete", "Are you sure you want to delete the selected record?")
        if confirm:
            expense_id = self.tree.item(selected_item[0])["values"][0]
            self.db.delete_expense(expense_id)
            self.populate_expenses()






if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTrackerApp(root)
    root.mainloop()







    






