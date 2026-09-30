import json
from pathlib import Path
from models.transaction import Transaction

DATA_FILE = Path("data/transactions.json")

class FinanceService:
    # This class manages all the money math and saving/loading data

    def __init__(self):
        self.transactions = []
        # load the saved data right when the program starts
        self.load()

    def add_transaction(self, kind, description, amount, category):
        # figure out the next ID number
        if len(self.transactions) == 0:
            next_id = 1
        else:
            all_ids = [t.transaction_id for t in self.transactions]
            next_id = max(all_ids) + 1
            
        new_record = Transaction(next_id, kind, description, amount, category)
        self.transactions.append(new_record)
        
        # always save after adding
        self.save()

    def get_all_transactions(self):
        return self.transactions

    def get_summary(self):
        # calculate total money in and out
        total_income = sum(t.amount for t in self.transactions if t.kind == "income")
        total_expense = sum(t.amount for t in self.transactions if t.kind == "expense")
        
        current_balance = total_income - total_expense
        
        # avoid division by zero error if they have no income yet
        if total_income > 0:
            savings_rate = (current_balance / total_income) * 100
        else:
            savings_rate = 0
            
        return {
            "income": total_income,
            "expense": total_expense,
            "balance": current_balance,
            "savings_rate": savings_rate
        }

    def category_summary(self):
        # groups the expenses so we can see where the money is going
        result = {}
        for t in self.transactions:
            if t.kind == "expense":
                if t.category in result:
                    result[t.category] = result[t.category] + t.amount
                else:
                    result[t.category] = t.amount
        return result

    def search(self, keyword):
        found_items = []
        # look through description, category, and kind
        for t in self.transactions:
            if keyword in t.description.lower() or keyword in t.category.lower() or keyword in t.kind.lower():
                found_items.append(t)
        return found_items

    def delete_transaction(self, transaction_id):
        # loop through to find the right one to delete
        for t in self.transactions:
            if t.transaction_id == transaction_id:
                self.transactions.remove(t)
                self.save()
                return True
                
        # if we get here, it wasn't found
        return False

    def save(self):
        # make the data folder if it doesn't exist
        DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        with DATA_FILE.open("w", encoding="utf-8") as file:
            # convert all transaction objects to dicts so JSON can save them
            dict_list = [t.to_dict() for t in self.transactions]
            json.dump(dict_list, file, indent=4)

    def load(self):
        # if no file exists yet, just stop here
        if not DATA_FILE.exists():
            return
            
        try:
            with DATA_FILE.open("r", encoding="utf-8") as file:
                data = json.load(file)
            # turn the dicts back into actual Transaction objects
            self.transactions = [Transaction.from_dict(x) for x in data]
        except:
            # if something goes wrong reading the file, just start with an empty list
            self.transactions = []