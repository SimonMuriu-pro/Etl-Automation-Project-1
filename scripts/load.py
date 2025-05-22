from sqlalchemy import create_engine, text
from config.database import db_config

def create_schema_if_not_exists(engine, schema_name):
    try:
        with engine.connect() as conn:
            check_schema_sql = f"""
                SELECT schema_name FROM information_schema.schemata 
                WHERE schema_name = '{schema_name}'
            """
            result = conn.execute(text(check_schema_sql))
            if result.fetchone() is None:
                create_schema_sql = f"CREATE SCHEMA {schema_name}"
                conn.execute(text(create_schema_sql))
                print(f"✅ Schema '{schema_name}' created.")
            else:
                print(f"✅ Schema '{schema_name}' already exists.")
    except Exception as e:
        print(f"❌ Error creating schema '{schema_name}': {str(e)}")

def load_to_postgres(df, table_name, schema='cleaned'):
    if df is None:
        print(f"⚠️ Skipping load for table '{table_name}' because DataFrame is None.")
        return
    
    engine = create_engine(
        f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
    )
    
    df.to_sql(table_name, engine, schema=schema, if_exists='replace', index=False)
    
