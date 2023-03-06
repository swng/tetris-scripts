import requests
import json
import csv



blitz_leaderboard_response = requests.get("https://ch.tetr.io/api/streams/blitz_global")
base = blitz_leaderboard_response.json()

thing = []

for i in range(100):

    placement = i+1
    username = base["data"]["records"][i]["user"]["username"]
    score = base["data"]["records"][i]["endcontext"]["score"]

    method = "idk"

    clears = base["data"]["records"][i]["endcontext"]["clears"]
    pc_count = clears["allclear"]
    if (pc_count > 10):
        # PC loop, DPC loop, BT loop
        tsd_to_pc = clears["tspindoubles"] / pc_count
        tst_to_pc = clears["tspintriples"] / pc_count

        if (tsd_to_pc < .1):
            method = "PC Loop?"
        else:
            if (tsd_to_pc < .5):
                method = "DPC Loop?"
            else:
                if (tst_to_pc > .5):
                    method = "BT Loop?"
    else:
        if (base["data"]["records"][i]["endcontext"]["topbtb"] > 30):
            method = "LST/ST/freestyle?"

    thing.append([placement, username, score, method])
    
with open('blitz_thing.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(thing)




