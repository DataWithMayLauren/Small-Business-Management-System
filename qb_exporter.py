import csv

def export_for_quickbooks():
    print("--- 🛠️ QUICKBOOKS DATA PREP TOOL ---")
    
    qb_data = []
    # QuickBooks Sales Receipt Format headers
    headers = ['Customer', 'TransactionDate', 'RefNo', 'Item', 'Quantity', 'Rate', 'Amount']

    with open('laundry_orders.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['PaymentStatus'] == 'Paid':
                # Map our shop data to QB fields
                qb_data.append({
                    'Customer': row['Customer'],
                    'TransactionDate': "2026-02-12", # Current Date
                    'RefNo': row['OrderID'],
                    'Item': row['Service'],
                    'Quantity': row['Weight_KG'],
                    'Rate': 65.0 if "Wash-Dry-Fold" in row['Service'] else 35.0,
                    'Amount': float(row['Weight_KG']) * (65.0 if "Wash-Dry-Fold" in row['Service'] else 35.0)
                })

    with open('qb_import_ready.csv', mode='w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(qb_data)

    print("✅ SUCCESS: 'qb_import_ready.csv' generated for QuickBooks Online import.")

if __name__ == "__main__":
    export_for_quickbooks()
