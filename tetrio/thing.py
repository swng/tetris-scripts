import json

f = open("TL_leaderboard_07-16.json", "r")

base = json.load(f)

a = []

for i in range(len(base["data"]["users"])):
    if (True):
        apm = base["data"]["users"][i]["league"]["apm"]
        rank = base["data"]["users"][i]["league"]["rank"]
        
        if apm > 100 and rank == "u":
            a.append([base["data"]["users"][i]["username"], base["data"]["users"][i]["league"]["rank"], i])

print(a)