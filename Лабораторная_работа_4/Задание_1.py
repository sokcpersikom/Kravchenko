# TODO решите задачу
import json

def task() -> float:
    with open("input.json", "r") as json_file:
        obj = json.load(json_file)

    return round(sum(map(lambda x: x["score"] * x["weight"], obj)), 3)

print(task())
