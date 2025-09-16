import pandas as pd
from datetime import datetime, timedelta

# Define product catalog with prices (based on the video style)
products = [
    ("Smartphone", 899.99),
    ("Laptop", 599.99),
    ("Tablet", 199.99),
    ("Headphones", 99.99),
    ("Camera", 299.99),
    ("Smartwatch", 249.99),
    ("Monitor", 199.99),
    ("Keyboard", 49.99),
    ("Mouse", 29.99),
    ("Printer", 129.99)
]

# Generate 50 records
records = []
start_date = datetime.strptime("2023-01-01", "%Y-%m-%d")

for i in range(50):
    customer_id = i + 1
    date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
    product, price = products[i % len(products)]
    quantity = (i % 5) + 1
    records.append([customer_id, date, product, price, quantity])

# Create DataFrame and save as CSV
df = pd.DataFrame(records, columns=["CustomerID", "Date", "Product", "Price", "Quantity"])
df.to_csv("Sales.csv", index=False)

print("Sales.csv file created with 50 records!")