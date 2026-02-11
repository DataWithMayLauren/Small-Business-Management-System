import csv

def run_reconciliation():
    print("--- 🏦 MAY LAUREN'S BANK RECONCILIATION ---")
    
    # 1. Get the "Company Books" (Paid orders from your laundry file)
    company_paid_total = 0
    with open('laundry_orders.csv', mode='r') as file:
        reader = csv.DictReader(file)
        # Rates for calculation: Wash-Dry-Fold: 65, Wash-Only: 35
        for row in reader:
            if row['PaymentStatus'] == 'Paid':
                # Just a simple calc for this demo
                weight = float(row['Weight_KG'])
                rate = 65.0 if row['Service'] == 'Wash-Dry-Fold' else 35.0
                company_paid_total += (weight * rate)

    # 2. Get the "Bank Records" (Total Deposits)
    bank_deposit_total = 0
    with open('bank_statement.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row['Bank_Amount'])
            if amount > 0: # Only count deposits, not expenses
                bank_deposit_total += amount

    # 3. Compare
    difference = company_paid_total - bank_deposit_total

    print(f"Company Books (Paid Orders): ₱{company_paid_total:,.2f}")
    print(f"Bank Statement (Deposits):   ₱{bank_deposit_total:,.2f}")
    print("-" * 42)

    if difference == 0:
        print("✅ RECONCILED: The books match the bank!")
    else:
        print(f"❌ DISCREPANCY: ₱{abs(difference):,.2f} difference found!")
        print("   Check for unrecorded deposits or encoding errors.")
    print("------------------------------------------")

if __name__ == "__main__":
    run_reconciliation()
