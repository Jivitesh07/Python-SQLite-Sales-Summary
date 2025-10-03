# Python-SQLite-Sales-Summary

The primary goal of this project is to quickly connect to a tiny local SQLite database, execute a summary SQL query, and present the results in both a tabular format and a simple bar chart. This serves as a foundational exercise for extracting key business insights from structured data.

Key Features & Results - 

Database Creation: Programmatically creates a local SQLite file (sales_data.db) and a sales table.
Data Population: Inserts sample sales records (Product, Quantity, Price) for analysis.
SQL Aggregation: Runs a key SQL query to calculate:
total_qty_sold (Total quantity sold per product)
total_revenue (Total revenue generated per product)
This uses the SUM() and GROUP BY SQL clauses.
Tabular Report: Prints the summarized results to the console using a Pandas DataFrame.
Data Visualization: Generates a professional bar chart illustrating the Total Revenue by Product.
