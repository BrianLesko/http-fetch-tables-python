import pandas as pd
import requests
from bs4 import BeautifulSoup
from io import StringIO

# Fetch the webpage
url = "https://en.wikipedia.org/wiki/Timeline_of_programming_languages"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all tables on the page
tables = soup.find_all('table', class_='wikitable')

# List to hold all DataFrames
dfs = []

# Loop through and convert tables to DataFrames
for i, table in enumerate(tables):
    df = pd.read_html(StringIO(str(table)))[0]
    dfs.append(df)
    print(f'Table {i + 1} added to list')

# Concatenate all DataFrames into one
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv('combined_tables.csv', index=False)
print('combined_tables.csv created')