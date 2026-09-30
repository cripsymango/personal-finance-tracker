class Transaction:
    # A simple class to hold our money details
    
    def __init__(self, trans_id, kind, desc, amount, category):
        self.transaction_id = trans_id
        self.kind = kind
        self.description = desc
        self.amount = float(amount)
        self.category = category

    # We need to turn this into a dictionary so we can save it to the text/JSON file
    def to_dict(self):
        return {
            "transaction_id": self.transaction_id,
            "kind": self.kind,
            "description": self.description,
            "amount": self.amount,
            "category": self.category
        }

    # This helps us load the saved dictionary data back into a real python object
    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            data_dict["transaction_id"],
            data_dict["kind"],
            data_dict["description"],
            data_dict["amount"],
            data_dict["category"]
        )