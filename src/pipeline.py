import pandas as pd
from src.campaign import Campaign

def load_data(path):
    return pd.read_csv(path)

def process_data(df):
    return [Campaign.from_row(row) for _, row in df.iterrows()]