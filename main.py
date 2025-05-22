import os
from scripts.extract import extract_from_excel, extract_from_postgres, extract_from_google_sheet
from scripts.transform import (
    transform_csv_data, remove_csv_duplicates, remove_csv_null_values,
    transform_postgres_data, remove_postgres_duplicates, remove_postgres_null_values,
    transform_google_sheet_data, remove_google_sheet_duplicates, remove_google_sheet_null_values
)
from scripts.load import create_schema_if_not_exists, load_to_postgres
from scripts.email import send_success_email
from config.database import engine
from config.settings import SAVE_LOCALLY
from logs.logger import logger

# === Ensure output folder is correctly set ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'output')
if SAVE_LOCALLY and not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

if __name__ == "__main__":
    try:
        # Extract
        try:
            excel_df = extract_from_excel()
        except Exception as e:
            logger.error(f"❌ Failed to extract Excel data: {e}")
            excel_df = None

        try:
            postgres_df = extract_from_postgres()
        except Exception as e:
            logger.error(f"❌ Failed to extract PostgreSQL data: {e}")
            postgres_df = None

        try:
            google_df = extract_from_google_sheet()
        except Exception as e:
            logger.error(f"❌ Failed to extract Google Sheet data: {e}")
            google_df = None

        print("✅ ETL Extract completed successfully.")

        # Transform
        if excel_df is not None:
            excel_df = transform_csv_data(excel_df)
            excel_df = remove_csv_duplicates(excel_df)
            excel_df = remove_csv_null_values(excel_df)

        if postgres_df is not None:
            postgres_df = transform_postgres_data(postgres_df)
            postgres_df = remove_postgres_duplicates(postgres_df)
            postgres_df = remove_postgres_null_values(postgres_df)

        if google_df is not None:
            google_df = transform_google_sheet_data(google_df)
            google_df = remove_google_sheet_duplicates(google_df)
            google_df = remove_google_sheet_null_values(google_df)

        logger.info("✅ ETL Transform complete")
        print("✅ ETL Transform completed successfully.")

        # Save locally
        if SAVE_LOCALLY:
            try:
                if excel_df is not None:
                    path = os.path.join(OUTPUT_FOLDER, 'orders_cleaned.csv')
                    excel_df.to_csv(path, index=False)
                   

                if postgres_df is not None:
                    path = os.path.join(OUTPUT_FOLDER, 'support_tickets_cleaned.csv')
                    postgres_df.to_csv(path, index=False)
                    

                if google_df is not None:
                    path = os.path.join(OUTPUT_FOLDER, 'feedback_data_cleaned.csv')
                    google_df.to_csv(path, index=False)
                    

                print("✅ Cleaned files saved locally to 'output' folder.")
            except Exception as e:
                logger.error(f"❌ Failed to save cleaned files: {e}")
                print(f"❌ Failed to save cleaned files: {e}")

        # Load to PostgreSQL
        create_schema_if_not_exists(engine, 'cleaned')

        tables = {
            'orders_cleaned': excel_df,
            'support_tickets_cleaned': postgres_df,
            'feedback_data_cleaned': google_df
        }

        for table_name, df in tables.items():
            load_to_postgres(df, table_name)

        logger.info("✅ ETL Load complete")
        print("✅ ETL Load to postgre database completed successfully.")

        # Notify
        send_success_email()

    except Exception as e:
        logger.error(f"❌ ETL process failed: {e}")
        print(f"❌ ETL process failed: {e}")
