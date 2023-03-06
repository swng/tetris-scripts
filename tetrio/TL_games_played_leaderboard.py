import requests
import json

# base_user_url = "https://ch.tetr.io/api/users/"

tetra_league_leaderboard_response = requests.get("https://ch.tetr.io/api/users/lists/league/all")
base = tetra_league_leaderboard_response.json()

#f = open("TL_leaderboard_07-25.json", "r")
#base = json.load(f)

base_user_url = "https://ch.tetr.io/api/users/"


users = []
games = []

for i in range(len(base["data"]["users"])):
    if (True):
        try:
            username = base["data"]["users"][i]["username"]
            users.append(username)
            #games.append(base["data"]["users"][i]["league"]["gamesplayed"])
            user_response = requests.get(base_user_url + username)
            user_json = user_response.json()

            games.append(user_json['data']['user']['gamesplayed'])
        except:
            print(base["data"]["users"][i]["username"])
            exit()


thing = [[y, x] for x, y in sorted(zip(games, users), key=lambda pair: pair[0])]
thing.reverse()
#print(thing)
with open('your_file.txt', 'w') as f:
    for item in thing:
        f.write("%s\n" % item)