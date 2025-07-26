import requests
import pandas as pd

url = 'https://dev.kwayisi.org/apis/gse/live/MTNGH'
response = requests.get(url)


if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame([data])

    print("Latest MTNGH Stock Info:\n")
    print(df.T)


else:
    print(f"Error fetching data: {response.status_code}")
    