import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Connect to SQLite database (will create file if not exists)
conn = sqlite3.connect("customer360.db")

# Save to table
df.to_sql("telco_churn", conn, if_exists="replace", index=False)

print("✅ Data loaded into customer360.db (table: telco_churn)")
