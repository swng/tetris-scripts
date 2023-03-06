import requests
import json

# base_user_url = "https://ch.tetr.io/api/users/"

tetra_league_leaderboard_response = requests.get("https://ch.tetr.io/api/users/lists/league/all")
base = tetra_league_leaderboard_response.json()

users = []
ratios = []

for i in range(len(base["data"]["users"])):
    if (True):
        apm = base["data"]["users"][i]["league"]["apm"]
        pps = base["data"]["users"][i]["league"]["pps"]
        vs = base["data"]["users"][i]["league"]["vs"]

        app = apm / pps / 60
        ratio = vs / apm

        users.append(base["data"]["users"][i]["username"])
        ratios.append(ratio)


thing = [[x, y] for y, x in sorted(zip(ratios, users), key=lambda pair: pair[0])]
thing.reverse()
#print(thing)
with open('your_file.txt', 'w') as f:
    for item in thing:
        f.write("%s\n" % item)