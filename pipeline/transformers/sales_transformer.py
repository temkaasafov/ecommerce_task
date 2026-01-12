from pipeline.transformers.interfaces import DataTransformer
import pandas as pd

class Sales_Transformer(DataTransformer):
    def transform(self):
        event_df = pd.read_csv('events_data.csv')
        filtered_df = event_df[event_df['event_type'] == 'purchase']
        products_df = pd.read_csv('products_data.csv')
        merged_df = pd.merge(filtered_df, products_df, on='product_id', how='inner')
        customers_df = pd.read_csv('customers_data.csv')
        merged_df = pd.merge(merged_df, customers_df, on='customer_id', how='inner')
        merged_df['total_revenue'] = merged_df['quantity'] * merged_df['price']
        grouped_df = merged_df.groupby(['category', 'segment'], as_index=False).agg(
            total_revenue = ('total_revenue', 'sum'),
            units_sold = ('quantity', 'sum'),
            unique_customers = ('customer_id', 'nunique')
        )
        return grouped_df
