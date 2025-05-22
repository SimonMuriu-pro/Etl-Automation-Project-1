import pandas as pd

# Transformations for CSV data (orders)
def transform_csv_data(df):
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], errors='coerce')
    return df

def remove_csv_duplicates(df):
    df = df.drop_duplicates()
    return df

def remove_csv_null_values(df):
    df = df.dropna()
    return df

# Transformations for PostgreSQL data (support_tickets)
def transform_postgres_data(df):
    df['createddate'] = pd.to_datetime(df['createddate'], errors='coerce')
    return df

def remove_postgres_duplicates(df):
    df = df.drop_duplicates()
    return df

def remove_postgres_null_values(df):
    df = df.dropna()
    return df

# Transformations for Google Sheets data (feedback_data)
def transform_google_sheet_data(df):
    df['SubmittedDate'] = pd.to_datetime(df['SubmittedDate'], errors='coerce')
    return df

def remove_google_sheet_duplicates(df):
    df = df.drop_duplicates()
    return df

def remove_google_sheet_null_values(df):
    df = df.dropna()
    return df






