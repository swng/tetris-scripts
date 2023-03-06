import requests
import json
import csv



blitz_leaderboard_response = requests.get("https://ch.tetr.io/api/streams/blitz_global")
base = blitz_leaderboard_response.json()

for i in range(999):

    if "disputed_until" in base["data"]["records"][i]:
        print(base["data"]["records"][i]["user"]["username"])
    



