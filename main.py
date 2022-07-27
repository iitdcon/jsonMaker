import json

import pandas as pd


def processPGCourses():
    ans = []
    columns = ["id", "name", "credit", "description", "core"]
    data = pd.read_csv("csvData/pgcourses.csv")
    numCourses = data.shape[0]

    for i in range(numCourses):
        unit = {}
        for j in columns:
            unit[j] = data[j][i]
        ans.append(unit)
    result = json.dumps(ans, indent=4)
    with open("data/pgcourses.json", "w") as f:
        f.write(result)


def processPhDCourses():
    ans = []
    columns = ["id", "name", "credit", "description"]
    data = pd.read_csv("csvData/phdcourses.csv")
    numCourses = data.shape[0]

    for i in range(numCourses):
        unit = {}
        for j in columns:
            unit[j] = data[j][i]
        ans.append(unit)
    result = json.dumps(ans, indent=4)
    with open("data/phdcourses.json", "w") as f:
        f.write(result)


def processUGCourses():
    ans = []
    columns = ["id", "name", "credit", "description", "core"]
    data = pd.read_csv("csvData/ugcourses.csv")
    numCourses = data.shape[0]

    for i in range(numCourses):
        unit = {}
        for j in columns:
            unit[j] = data[j][i]
        ans.append(unit)
    result = json.dumps(ans, indent=4)
    with open("data/ugcourses.json", "w") as f:
        f.write(result)


if __name__ == "__main__":
    processPGCourses()
    processPhDCourses()
    processUGCourses()
