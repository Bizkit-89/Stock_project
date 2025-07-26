import pandas as pd

#Loading my CSV
file_path = r'C:\Users\user\Desktop\stock project\mtn_gh_stock_price\Daily Shares  ETFs 2023.csv'
df = pd.read_csv(file_path)

#Keeping only columns i wanna work with
df = df[['Daily Date', 'Year High (GH¢)', 'Year Low (GH¢)']]

#Coverting daily date to datetime format
df['Daily Date'] = pd.to_datetime(df['Daily Date'], errors = 'coerce')

#drooping rows with invalid or missing dates
df = df.dropna(subset=['Daily Date'])

#sort by date
df = df.sort_values('Daily Date')
df = df.reset_index(drop=True)

#save the cleaned data to a new csv file
df.to_csv('cleaned_mtn_sprice.csv', index=False)

print("Datacleaned and saved as 'cleaned_mtn_sprice.csv'")


