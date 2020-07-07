import json


def get_data(file_data):


    with open(file_data) as f:
        data = json.load(f)
    
    names = [m["name"] for m in data["members"]]
    print(names)

get_data("data.json")

print("The end oth this line of code")