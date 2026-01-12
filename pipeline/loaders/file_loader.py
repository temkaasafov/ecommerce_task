import os
import pandas as pd
from pandas import DataFrame
from pipeline.loaders.interfaces import DataLoader

class File_Loader(DataLoader):
    def init(self, df):
        self.df = df
    def load(self, df: DataFrame):
        file_path = os.path.join('reports', 'sales_report.csv')
        os.mkdir('reports')
        df.to_csv(file_path, index=False)
        print(f"DataFrame successfully saved to {file_path}")