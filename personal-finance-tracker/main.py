from services.finance_service import FinanceService
from services.report_service import ReportService
from utils.input_helper import get_float, get_int, get_non_empty

def show_menu():
    # just a simple menu for the terminal
    print("\n-------------------------------------")
    print("        My Money Tracker             ")
    print("-------------------------------------")
    print("1. Add new income")
    print("2. Add new expense")
    print("3. See all my records")
    print("4. Check my balance")
    print("5. Spending by category")
    print("6. Find a specific record")
    print("7. Delete a record")
    print("8. Print full report")
    print("9. Save and quit")
    print("-------------------------------------")

def add_transaction(service, kind):
    print(f"\n--- Adding {kind} ---")
    description = get_non_empty("What is this for? ")
    amount = get_float("How much? Rs. ", 0.01)
    category = get_non_empty("Which category? (e.g. Food, Rent): ")
    
    service.add_transaction(kind, description, amount, category)
    print("Awesome, added it to the list.")

def view_transactions(service):
    transactions = service.get_all_transactions()
    print("\n--- All Records ---")
    
    if not transactions:
        print("Nothing here yet!")
        return

    # removed the fancy spacing to keep it simple
    for t in transactions:
        print(f"ID {t.transaction_id} | {t.kind} | {t.description} | {t.category} | Rs. {t.amount}")

def show_summary(service):
    summary = service.get_summary()
    print("\n--- My Balance ---")
    print(f"Total In: Rs. {summary['income']}")
    print(f"Total Out: Rs. {summary['expense']}")
    print(f"Leftover: Rs. {summary['balance']}")
    print(f"Savings Rate: {summary['savings_rate']:.1f}%")

def category_summary(service):
    summary = service.category_summary()
    print("\n--- Where did my money go? ---")
    
    if not summary:
        print("No expenses to show.")
        return
        
    for category, amount in summary.items():
        print(f" - {category}: Rs. {amount}")

def search_transactions(service):
    keyword = get_non_empty("Type a word to search: ").lower()
    results = service.search(keyword)
    
    print("\n--- Search Results ---")
    if not results:
        print("Couldn't find anything matching that.")
        return
        
    for t in results:
        print(f"ID {t.transaction_id} | {t.kind} | {t.description} | {t.category} | Rs. {t.amount}")

def delete_transaction(service):
    transaction_id = get_int("Enter the ID number you want to delete: ", 1)
    
    if service.delete_transaction(transaction_id):
        print("Done! Record deleted.")
    else:
        print("Hmm, couldn't find a record with that ID.")

def main():
    service = FinanceService()
    report_service = ReportService()

    while True:
        show_menu()
        choice = get_int("Pick a number: ", 1, 9)

        if choice == 1:
            add_transaction(service, "income")
        elif choice == 2:
            add_transaction(service, "expense")
        elif choice == 3:
            view_transactions(service)
        elif choice == 4:
            show_summary(service)
        elif choice == 5:
            category_summary(service)
        elif choice == 6:
            search_transactions(service)
        elif choice == 7:
            delete_transaction(service)
        elif choice == 8:
            # prints the big report from the report service
            print(report_service.generate_report(service))
        elif choice == 9:
            service.save()
            print("Saved everything. See ya!")
            break

# run the script
if __name__ == "__main__":
    main()