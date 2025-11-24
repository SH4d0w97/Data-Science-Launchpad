import sqlite3
import pandas as pd
import os

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..', 'data', 'olist.db')
conn = sqlite3.connect(db_path)

def run_query(query):
    """Helper function to run SQL queries"""
    df = pd.read_sql_query(query, conn)
    print(f"\n📊 QUERY: {query}")
    print(df.head())
    return df


# ==========================================
# 📝 TASK 1: The "Sanity Check"
# Idea: Peek at the raw data to see column names
# ==========================================
query_task_1 = "SELECT * FROM customers LIMIT 5;"
run_query(query_task_1)

# ==========================================
# 📝 TASK 2: The "Filter"
# Idea: Find all customers located in 'SP' (Sao Paulo)
# ==========================================
query_task_2 = """SELECT CUSTOMER_ID, CUSTOMER_CITY, CUSTOMER_STATE FROM CUSTOMERS WHERE CUSTOMER_STATE = 'SP' LIMIT 5; """
run_query(query_task_2)

# ==========================================
# 📝 TASK 3: The "Business Question"
# Idea: Count how many unique cities we have customers in
# ==========================================
query_task_3 = """
SELECT COUNT(DISTINCT customer_city) AS total_unique_cities 
FROM customers;
"""
run_query(query_task_3)
