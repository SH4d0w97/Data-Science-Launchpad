import sqlite3
import pandas as pd
import os

#====CONNECTING TO DB====
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..', 'data', 'olist.db')
conn = sqlite3.connect(db_path)

def run_query(query):
    """Helper function to run SQL queries"""
    try:
        df = pd.read_sql_query(query, conn)
        print(f"\n📊 QUERY: {query}")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error running query: {e}")
        return None


# ==========================================
# 📝 TASK 1: Join Orders and Customers
# Goal: Connect an Order to its Customer's State
# ==========================================
# query_test = """select * FROM customers LIMIT 5;"""
# run_query(query_test)   

query_task_1 = """SELECT O.order_id, O.customer_id, C.customer_state, C.customer_city, O.order_status 
FROM orders O
INNER JOIN customers C ON O.customer_id = C.customer_id
LIMIT 5;"""

# 1. RUN THE QUERY
run_query(query_task_1)

# 2. PRINT THE COLUMN NAMES
# print("\n📝 Column Names:")
# print(run_query(query_task_1).columns.tolist())

# ==========================================
# 📝 TASK 2: Join Orders and Items
# Goal: See the PRICE for each order
# ==========================================
# query_test = """select * FROM order_items LIMIT 5;"""
# run_query(query_test) 

QUERY_TASK_2 = """SELECT O.order_id, O.customer_id,I.price, I.freight_value, O.order_status 
FROM orders O
INNER JOIN order_items I ON O.order_id = I.order_id
LIMIT 5;"""

run_query(QUERY_TASK_2)