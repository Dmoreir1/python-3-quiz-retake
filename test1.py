import pandas as pd
df = pd.read_csv("users.csv")
print(df.head())

df1 = df["GAMEREWARDS"]
max = df1.max()

print(df1.head())
