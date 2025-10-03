import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Define the database file name
DB_FILE = "sales_data.db"

# --- 1. Database Setup: Connect, Create Table, and Insert Data ---
print(f"Connecting to database: {DB_FILE}")
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# SQL to create the sales table
create_table_sql = """
DROP TABLE IF EXISTS sales;
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
);
"""
cursor.executescript(create_table_sql)

# Sample sales data (Product, Quantity, Price)
sales_records = [
    ('Laptop', 5, 1200.00),
    ('Mouse', 50, 25.50),
    ('Monitor', 10, 350.00),
    ('Laptop', 2, 1200.00),
    ('Keyboard', 30, 75.00),
    ('Monitor', 5, 350.00),
    ('Mouse', 25, 25.50),
    ('Laptop', 8, 1200.00),
]

# Insert the data into the sales table
insert_sql = "INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)"
cursor.executemany(insert_sql, sales_records)
conn.commit()
print("Database created and sample data inserted successfully.")

# --- 2. Run SQL Query and Load into Pandas ---

# SQL Query to get total quantity and revenue grouped by product
summary_query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty_sold, 
    SUM(quantity * price) AS total_revenue
FROM 
    sales
GROUP BY 
    product
ORDER BY 
    total_revenue DESC;
"""

# Load the SQL query results directly into a Pandas DataFrame
df = pd.read_sql_query(summary_query, conn)

# Close the database connection
conn.close()

# --- 3. Display Output using Print ---
print("\n" + "="*40)
print("     SALES SUMMARY (Data Table)")
print("="*40)
print(df.to_string(index=False)) # Use to_string for clean console output

# --- 4. Plot Simple Bar Chart using Matplotlib/Pandas ---
print("\nGenerating bar chart...")

# Use the plot method built into pandas DataFrame
plt.figure(figsize=(8, 5))
df.plot(
    kind='bar', 
    x='product', 
    y='total_revenue', 
    legend=False,
    ax=plt.gca(), # Use the current axes
    color=['skyblue', 'salmon', 'lightgreen', 'gold']
)

# Customize the chart
plt.title('Total Revenue by Product', fontsize=16, pad=15)
plt.xlabel('Product', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)
plt.xticks(rotation=45, ha='right') # Rotate x-labels for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() # Adjust layout to prevent labels from being cut off

# Display the chart
print("Chart displayed successfully!")
plt.show() 