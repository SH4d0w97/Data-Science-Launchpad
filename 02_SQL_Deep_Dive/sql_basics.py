import sqlite3
import pandas as pd
import os

db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..', 'data', 'olist.db')
print(f"Loading data from {db_path}")