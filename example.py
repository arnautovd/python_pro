import json

with open("data.json") as f:
    data = json.load(f)
    
names = [m["name"] for m in data["members"]]
print(names)