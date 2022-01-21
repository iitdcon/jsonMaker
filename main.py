import json
import pandas as pd

with open("data/faculty.json") as f:
    data = json.load(f)

facultyFields = [
        'name',
        'position',
        'education',
        'research',
        'room',
        'email',
        'homepage',
        'avatar'
        ]

mega = []
for i in data:
    ans = []
    for field in facultyFields:
        ans.append(i[field])
    mega.append(ans)





