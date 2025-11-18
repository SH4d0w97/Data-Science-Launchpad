import pandas as pd
import sqlite3
import os

# --- CONFIGURATION ---
# This assumes the 'data' folder is one level up from this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Relative Paths
data_folder = os.path.join(current_dir, '..', 'data')
db_name = 'olist.db'
db_path = os.path.join(current_dir, '..', 'data', db_name)

# --- SETUP ---
print(f"📂 Looking for data in: {data_folder}")
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# --- LOADING ---
files_processed = 0

for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder, filename)
        
        # Clean table name: olist_orders_dataset.csv -> orders
        table_name = filename.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
        
        print(f"⏳ Loading {filename} into table '{table_name}'...")
        
        try:
            # Read CSV
            df = pd.read_csv(file_path)
            
            # Write to SQLite
            # if_exists='replace' ensures a clean start every time the script is run
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            
            print(f"   ✅ Loaded {len(df)} rows.")
            files_processed += 1
            
        except Exception as e:
            print(f"   ❌ Error loading {filename}: {e}")

# --- FINISH ---
conn.close()
print(f"\n🎉 Success! {files_processed} CSV files loaded into {db_name}")
print(f"   Database location: {db_path}")