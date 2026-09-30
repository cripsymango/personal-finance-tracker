def validate_amount(amount):
    # Make sure the amount is actually a number and bigger than zero
    if type(amount) == int or type(amount) == float:
        if amount > 0:
            return True
            
    # If it's not a number or it's negative, fail the check
    return False

def validate_transaction_type(kind):
    # Check if the type is exactly one of our two options
    if kind == "income" or kind == "expense":
        return True
    else:
        return False