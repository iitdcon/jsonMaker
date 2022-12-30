import json
import os

import pandas as pd

datas = []
for i in os.listdir("ExcelData/publications"):
    data = pd.read_excel(f"ExcelData/publications/{i}")
    datas.append(data)

finalData = pd.concat(datas)
print(f"There were {len(finalData)}")
finalData.drop_duplicates(keep="first", inplace=True)
print(f"There are {len(finalData)}")
finalData.columns = ["year", "citation", "type", "doi"]
json_string = finalData.to_json(orient="records")
parsed = json.loads(json_string)
with open("data/publications.json", "w") as f:
    f.write(json.dumps(parsed, indent=4))
