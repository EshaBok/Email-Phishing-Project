import pandas as pd
import glob
import os

path = os.path.join(os.path.dirname(__file__), '..', 'data')
all_files = glob.glob(os.path.join(path, "*csv"))

data_list = []

for filename in all_files:
    df = pd.read_csv(filename)
    data_list.append(df)

master_df = pd.concat(data_list, axis=0, ignore_index=True)

print(f"Files found: {all_files}")
print(f"Total Emails: {len(master_df)}")
print(master_df.columns)