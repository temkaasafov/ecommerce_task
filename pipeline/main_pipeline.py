from pipeline.extractors import File_Extractor, DB_Extractor
from pipeline.transformers import Sales_Transformer
from pipeline.loaders import File_Loader
import os


from pipeline.config import host, db_name, user, password

def run_pipeline():
    file_extractor = File_Extractor()
    db_extractor = DB_Extractor(f'postgresql://{user}:{password}@{host}/{db_name}')
    file_extractor.extract()
    db_extractor.extract()
    sales_transformer = Sales_Transformer()
    df = sales_transformer.transform()
    file_loader = File_Loader()
    file_loader.load(df)
    

    for filename in os.listdir('.'):
        if filename.endswith('.csv'):
            os.remove(filename)


