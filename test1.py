import pandas as pd
df = pd.read_csv("users.csv")
print(df.head())

df1 = df["GAMEREWARDS"]
print(df1.head())
