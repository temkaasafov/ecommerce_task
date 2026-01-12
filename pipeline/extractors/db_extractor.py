import pandas as pd
from sqlalchemy import create_engine
from pipeline.extractors.interfaces import DbExtractor


class DB_Extractor(DbExtractor):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def extract(self):
        try:
            engine = create_engine(self.connection_string)
            customers_df = pd.read_sql('SELECT * from customers', engine)
            products_df = pd.read_sql('SELECT * from products', engine)
            customers_df.to_csv('customers_data.csv', index=False, sep=',', encoding='utf-8')
            products_df.to_csv('products_data.csv', index=False, sep=',', encoding='utf-8')
        except Exception as _ex:
            print(_ex)