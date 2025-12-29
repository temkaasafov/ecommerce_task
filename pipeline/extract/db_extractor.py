import pandas as pd
from sqlalchemy import create_engine, text
connection_string = "postgresql+psycopg2://myuser:mypassword@localhost:5432/ecommerce_db"
engine = create_engine(connection_string)
sql_query = 'SELECT * FROM customers'
df = pd.read_sql_query(text(sql_query), con=engine.connect())
print(df.to_string())