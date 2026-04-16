import re
import pandas as pd
from tools import scan_email_for_fraud
from tools import extracting_domain
Data_Location = "data/Nazario.csv"
df = pd.read_csv(Data_Location)
print(df.head(20))
print(df.columns)
domain = re.search(r'[\w\.-]+@([\w\.-]+)', df['sender'][0])
print(domain.group(1))

df['domain'] = df['sender'].apply(extracting_domain)
