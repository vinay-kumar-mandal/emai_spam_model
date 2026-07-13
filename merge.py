import pandas as pd

df1 = pd.read_csv('dataset/row/emails.csv')
df2 = pd.read_csv('dataset/row/spam_ham_dataset.csv')
df3 = pd.read_csv('dataset/row/collected_spam_data.csv')

combined_df = pd.concat([df1, df2, df3], ignore_index=True)

combined_df.to_csv('combined_output.csv', index=False)