import pandas as pd

df = pd.read_csv("dataset/row/emails.csv", header=2)
print(df.dtypes)
print(df.describe())
