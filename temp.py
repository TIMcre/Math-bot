import pandas as pd
"""
data = ["hello", "dh57657"]

question = "(x + 0,2)²"

df = pd.read_csv("data.csv")


df = df.drop_duplicates()


df.loc[len(df)] = data

df.to_csv("data.csv")

#locs = df.loc[df["q"] == question]

#print(locs)
"""
df = pd.read_csv("data.csv", encoding='utf8')
question = "(x + 0,2)²"
print(df.query(question))