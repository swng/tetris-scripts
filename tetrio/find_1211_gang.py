import requests
import json

# base_user_url = "https://ch.tetr.io/api/users/"

tetra_league_leaderboard_response = requests.get("https://ch.tetr.io/api/users/lists/league/all")
base = tetra_league_leaderboard_response.json()

pros = []

for i in range(len(base["data"]["users"])):
    username = base["data"]["users"][i]["username"]
    if "1211" in username:
        pros.append(username)

print(pros)


