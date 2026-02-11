import csv

def calculate_laundry_bill(service, weight):
    # Pricing per KG
    rates = {
        "Wash-Dry-Fold": 65.00,
        "Wash-Only": 35.00,
        "Dry-Clean": 150.00
    }
    return rates.get(service, 0) * weight

def run_laundry_dashboard():
    print("--- 🧺 MAY LAUREN'S SMART LAUNDRY SYSTEM ---")
    print(f"{'ID':<5} | {'Customer':<12} | {'Service':<15} | {'Bill':<10} | {'Status'}")
    print("-" * 60)
    
    total_revenue = 0
    
    with open('laundry_orders.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            weight = float(row['Weight_KG'])
            bill = calculate_laundry_bill(row['Service'], weight)
            total_revenue += bill
            
            print(f"{row['OrderID']:<5} | {row['Customer']:<12} | {row['Service']:<15} | ₱{bill:<9,.2f} | {row['Status']}")
            
    print("-" * 60)
    print(f"TOTAL PENDING REVENUE: ₱{total_revenue:,.2f}")

if __name__ == "__main__":
    run_laundry_dashboard()
