import pandas as pd
df = pd.read_csv("Student_info.csv")
print(df)
print(df.columns)
print(df.head)
print(df.shape)
print(df.tail)
print(df["class"].mean())
topper =df.loc[df["marks"].idxmax()]
print(df.groupby("subject")["marks"].mean())
