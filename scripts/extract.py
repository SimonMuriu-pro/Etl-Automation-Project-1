import pandas as pd
import os
from sqlalchemy import create_engine
from config.database import db_config

# 1. Extract from Excel file from the data folder
import os
import pandas as pd

# 1. Extract from Excel file
def extract_from_excel():
    try:
        # Get path to the root directory (one level up from scripts/)
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(root_dir, 'data', 'orders_data.xlsx')

        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Failed to extract Excel data: {e}")
        return None


# 2. Extract from PostgreSQL Database
def extract_from_postgres():
    try:
        engine = create_engine(f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}")
        df = pd.read_sql("SELECT * FROM support_tickets", engine)
        return df
    except Exception as e:
        print(f"Failed to extract from PostgreSQL: {e}")
        return None

# 3. Extract from Google Sheets
def extract_from_google_sheet():
    try:
        sheet_url = "https://docs.google.com/spreadsheets/d/1mnf6BbbhYB652D1hkHxidy_liLzbQb9_4WU5qsAf6sg/export?format=csv"
        df = pd.read_csv(sheet_url)
        return df
    except Exception as e:
        print(f"Failed to extract from Google Sheets: {e}")
        return None
