import requests
import json

base_user_url = "https://ch.tetr.io/api/users/"

tetra_league_leaderboard_response = requests.get("https://ch.tetr.io/api/users/lists/league/all")
base = tetra_league_leaderboard_response.json()

# base data users

fractional_rds = []
users = []

for i in range(len(base["data"]["users"])):
    rd = base["data"]["users"][i]["league"]["rd"]
    username = base["data"]["users"][i]["username"]

    users.append(username)
    fractional_rds.append(rd % 1)

thing = [[y, x] for x, y in sorted(zip(fractional_rds, users), key=lambda pair: pair[0])]
thing.reverse()

with open('your_file.txt', 'w') as f:
    for item in thing:
        f.write("%s\n" % item)



