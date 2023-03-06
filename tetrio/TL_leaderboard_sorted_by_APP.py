import requests
import json

# base_user_url = "https://ch.tetr.io/api/users/"

tetra_league_leaderboard_response = requests.get("https://ch.tetr.io/api/users/lists/league/all")
base = tetra_league_leaderboard_response.json()

#f = open("TL_leaderboard_07-25.json", "r")
#base = json.load(f)

users = []
apps = []
ranks = []

for i in range(len(base["data"]["users"])):
    if (True):
        apm = base["data"]["users"][i]["league"]["apm"]
        pps = base["data"]["users"][i]["league"]["pps"]
        vs = base["data"]["users"][i]["league"]["vs"]

        app = apm / pps / 60
        ratio = vs / apm

        users.append(base["data"]["users"][i]["username"])
        apps.append(ratio)
        ranks.append(base["data"]["users"][i]["league"]["rank"])


thing = [[y, x, z] for x, y, z in sorted(zip(apps, users, ranks), key=lambda pair: pair[0])]
thing.reverse()
#print(thing)
with open('your_file.txt', 'w') as f:
    for item in thing:
        f.write("%s\n" % item)