import requests
import json



blitz_leaderboard_response = requests.get("https://ch.tetr.io/api/streams/blitz_global")
base = blitz_leaderboard_response.json()

users = []
b2bs = []


for i in range(999):

    b2b =  (base["data"]["records"][i]["endcontext"]["topbtb"])
    placement = i+1
    username = base["data"]["records"][i]["user"]["username"]
    score = base["data"]["records"][i]["endcontext"]["score"]

    users.append(username)
    b2bs.append(b2b)


    

    #print([b2b, placement, username, score])
    


thing = [[x, y] for y, x in sorted(zip(b2bs, users), key=lambda pair: pair[0])]
thing.reverse()
print(thing)
