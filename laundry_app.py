import csv

def run_accounting_system():
    print("--- 🧺 MAY LAUREN'S FINANCIAL DASHBOARD ---")
    
    # 1. Calculate Accounts Receivable (What customers owe us)
    receivable = 0
    rates = {"Wash-Dry-Fold": 65.0, "Wash-Only": 35.0, "Dry-Clean": 150.0}
    
    with open('laundry_orders.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['PaymentStatus'] == 'Unpaid':
                bill = rates.get(row['Service'], 0) * float(row['Weight_KG'])
                receivable += bill
    
    # 2. Calculate Accounts Payable (What we owe others)
    payable = 0
    with open('expenses.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Status'] == 'Unpaid':
                payable += float(row['Amount'])

    print(f"💰 Accounts Receivable (Incoming): ₱{receivable:,.2f}")
    print(f"💸 Accounts Payable (Outgoing):  ₱{payable:,.2f}")
    print("-" * 40)
    print(f"💼 Net Cash Position:           ₱{receivable - payable:,.2f}")
    print("------------------------------------------")

if __name__ == "__main__":
    run_accounting_system()
