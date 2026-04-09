import pandas as pd
from tools import scan_email_for_fraud
Data_Location = "data/Nigerian_Fraud.csv"
df = pd.read_csv(Data_Location)
print(df.head())
print(df.columns)
