def get_non_empty(prompt):
    # Keeps asking until the user actually types something
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("Hey, you can't leave this blank. Try again.")

def get_int(prompt, minimum=None, maximum=None):
    # Makes sure they type a whole number (like for menu choices)
    while True:
        try:
            user_input = int(input(prompt))
            
            # Check if it's too small
            if minimum is not None and user_input < minimum:
                print(f"That number is too small. It needs to be at least {minimum}.")
                continue
                
            # Check if it's too big
            if maximum is not None and user_input > maximum:
                print(f"That number is too big. The maximum is {maximum}.")
                continue
                
            return user_input
            
        except:
            print("Oops, please type a valid whole number.")

def get_float(prompt, minimum=None, maximum=None):
    # Makes sure they type a decimal number (like for money amounts)
    while True:
        try:
            user_input = float(input(prompt))
            
            if minimum is not None and user_input < minimum:
                print("Value too low. You can't enter a negative amount.")
                continue
                
            if maximum is not None and user_input > maximum:
                print(f"Value too high. The maximum is {maximum}.")
                continue
                
            return user_input
            
        except:
            print("That doesn't look like a valid money amount. Try again.")