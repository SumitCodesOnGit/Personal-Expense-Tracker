from datetime import datetime

class Expense:

    def __init__(self, description, amount, timestamp=None):
        self.description = description
        self.amount = amount
        self.timestamp = timestamp if timestamp else datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    


    


