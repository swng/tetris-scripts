import json

f = open("TL_leaderboard_06-27.json", "r")

base = json.load(f)

a = []

for i in range(len(base["data"]["users"])):
    if (base["data"]["users"][i]["username"] == "stqrm"):
        print(base["data"]["users"][i]["league"]["rating"])

