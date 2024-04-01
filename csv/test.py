import os
import pandas as pd

# Scan for all CSV files in the current directory.
csv_files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]

# Iterate over the list of CSV files and print their headers.
for file_name in csv_files:
    df = pd.read_csv(file_name, nrows=1) # Read only the first row to get the headers
    print(f'File name: {file_name}')
    print('Headers:', df.columns.tolist())