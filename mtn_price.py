import os
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

dataset_name = "redpen12/mtn-gh-stock-price-dataset"
download_path = os.path.join(os.getcwd(), 'mtn_gh_stock_price')

api.dataset_download_files(dataset_name, path=download_path, unzip=True)

print(f"Dataset downloaded to: {download_path}")



import pandas as pd

# Load the dataset (update filename if different)
df = pd.read_csv("mtn_gh_stock_price/Daily Shares  ETFs 2023.csv")



# Show the first 5 rows
print(df.head())


import pandas as pd

# Load the dataset
df = pd.read_csv("mtn_gh_stock_price/Daily Shares  ETFs 2023.csv")

# Show the first few rows
print("Preview of dataset:")
print(df.head())

# Show basic info
print("\nDataset Info:")
print(df.info())

# Show summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))


# Standardize column names (strip spaces, lower case)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")







# Optional: sort by date
df = df.sort_values('Daily Date')


# Preview cleaned data
print("\nCleaned data:")
print(df.head())



import matplotlib.pyplot as plt

# Replace with your actual column name
plt.figure(figsize=(10, 5))
plt.plot(df.index, df['closing_price'], label='Closing Price', color='blue')

plt.title('MTN Ghana Stock Price Trend')
plt.xlabel('Time (Index)')
plt.ylabel('Price (GHS)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


print(df.columns)

