import pandas as pd 

data = pd.read_csv("Bengaluru_House_Data.csv")

print(data.describe())
print(data.info())