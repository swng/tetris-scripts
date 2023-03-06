import requests
import json

base_user_url = "https://ch.tetr.io/api/users/"

tetra_league_leaderboard_response = requests.get("https://ch.tetr.io/api/users/lists/league/all")
base = tetra_league_leaderboard_response.json()

# base data users
users = []
times = []

for i in range(len(base["data"]["users"])):
    if (base["data"]["users"][i]["league"]["rank"] == "u"):
        username = base["data"]["users"][i]["username"]
        user_response = requests.get(base_user_url + username + '/records')
        user_json = user_response.json()
        if 'records' in user_json['data']:
            if user_json['data']['records']['40l']['record'] is not None:
                time = float(user_json['data']['records']['40l']['record']['endcontext']['finalTime'])
                users.append(username)
                times.append(time)


thing = [x for _, x in sorted(zip(times, users), key=lambda pair: pair[0])]
print(thing)



