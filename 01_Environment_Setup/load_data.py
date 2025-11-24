import pandas as pd
import sqlite3
import os

# --- CONFIGURATION ---
current_dir = os.path.dirname(os.path.abspath(__file__))
data_folder = os.path.join(current_dir, '..', 'data')
db_name = 'olist.db'
db_path = os.path.join(current_dir, '..', 'data', db_name)

# --- SETUP ---
print(f"📂 Looking for data in: {data_folder}")
print(f"📊 Generatng Week 3 Summary Report...\n")

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

files_processed = 0

for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder, filename)
        table_name = filename.replace('olist_', '').replace('_dataset.csv', '').replace('.csv', '')
        
        try:
            # 1. Read CSV
            df = pd.read_csv(file_path)
            
            # --- WEEK 3 TASK COMPLETION: PRINT SUMMARY ---
            print(f"🔹 Table: {table_name.upper()}")
            print(f"   • Rows:    {df.shape[0]:,}")  # Counts rows
            print(f"   • Columns: {df.shape[1]}")    # Counts columns
            print(f"   • Names:   {', '.join(df.columns[:3])}...") # Previews first 3 column names
            print("-" * 40)
            # ---------------------------------------------

            # 2. Load to SQLite
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            files_processed += 1
            
        except Exception as e:
            print(f"   ❌ Error loading {filename}: {e}")

conn.close()
print(f"\nSummary generated for {files_processed} files.")