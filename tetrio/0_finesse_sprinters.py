import requests
import json

base_user_url = "https://ch.tetr.io/api/users/"

sprint_leaderboard_response = requests.get("https://ch.tetr.io/api/streams/40l_global")
base = sprint_leaderboard_response.json()

pros = []

for i in range(len(base["data"]["records"])):
    temp = base["data"]["records"][i]["endcontext"]
    if "finesse" in temp:
        if temp["finesse"]["faults"] == 0:
            placement = i+1
            username = base["data"]["records"][i]["user"]["username"]
            time = temp["finalTime"]

            pros.append([placement, username, time])
    
for pro in pros:
    print(pro)