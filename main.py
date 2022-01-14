import json
import pandas as pd

with open("data/faculty.json") as f:
    data = json.load(f)


for i in data:
    print(i['name'])

while True:
    print("This is a test")
    break


df = pd.read_csv("data/faculty.csv")
print(df.head())    


