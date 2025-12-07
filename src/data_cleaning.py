# The purpose of this script is to make sure the data is clean so that we can follow through with our coding project.

# importing pandas
import pandas as pd
# loading the data set - sales_data_raw.csv
data = pd.read_csv('data/raw/sales_data_raw.csv')
# standardize the column names
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
# strip whitespace from product names and categories
data['prodname'] = data['prodname'].str.strip()
data['category'] = data['category'].str.strip()
# drop missing prices and quantities
data = data.dropna(subset=['price', 'qty'])
# convert price and quantity to numeric
data['price'] = pd.to_numeric(data['price'], errors='coerce')
data['qty'] = pd.to_numeric(data['qty'], errors='coerce')

# save to cleaned data file
data.to_csv('data/processed/sales_data_clean.csv', index=False)