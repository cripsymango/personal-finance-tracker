import unittest
from models.transaction import Transaction
from utils.validators import validate_amount, validate_transaction_type

class TestFinanceTracker(unittest.TestCase):
    
    def test_transaction_creation(self):
        # Let's make sure the Transaction class actually saves the data correctly
        my_expense = Transaction(1, "expense", "Movie ticket", 250, "Entertainment")
        
        # Check if the amount and category match what we put in
        self.assertEqual(my_expense.amount, 250)
        self.assertEqual(my_expense.category, "Entertainment")

    def test_serialization(self):
        # Testing if we can turn an object into a dictionary and back again (for saving to JSON)
        my_income = Transaction(1, "income", "Pocket Money", 5000, "Allowance")
        
        # turn it into a dictionary
        dict_data = my_income.to_dict()
        
        # build it back into a Python object
        loaded_back = Transaction.from_dict(dict_data)
        
        # verify it didn't lose the details in the process
        self.assertEqual(loaded_back.description, "Pocket Money")
        self.assertEqual(loaded_back.amount, 5000)

    def test_validators(self):
        # Testing our math and text checkers to make sure they catch bad inputs
        self.assertTrue(validate_amount(150))
        self.assertFalse(validate_amount(-50))  # negative amounts should fail
        self.assertFalse(validate_amount(0))
        
        self.assertTrue(validate_transaction_type("expense"))
        self.assertFalse(validate_transaction_type("investment"))  # should fail because it's not income/expense

if __name__ == "__main__":
    # runs the tests when we execute this file
    unittest.main()