from sqlalchemy import create_engine, text
from config.database import db_config
import logging

def create_schema_if_not_exists(engine, schema_name):
    try:
        with engine.connect() as conn:
            # Check if schema exists
            check_schema_sql = f"SELECT schema_name FROM information_schema.schemata WHERE schema_name = '{schema_name}'"
            result = conn.execute(text(check_schema_sql))
            
            if result.fetchone() is None:
                create_schema_sql = f"CREATE SCHEMA {schema_name}"
                conn.execute(text(create_schema_sql))
                logging.info(f"Schema '{schema_name}' created.")
            else:
                logging.info(f"Schema '{schema_name}' already exists.")
    except Exception as e:
        logging.error(f"Error creating schema '{schema_name}': {str(e)}")
