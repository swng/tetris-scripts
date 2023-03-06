import requests
import json

from matplotlib import pyplot as plt
import numpy as np



f = open("TL_leaderboard_07-15.json", "r")
base = json.load(f)

#tetra_league_leaderboard_response = requests.get("https://ch.tetr.io/api/users/lists/league/all")
#base = tetra_league_leaderboard_response.json()

data = []
data_x = []

for i in range(len(base["data"]["users"])):
    tr = base["data"]["users"][i]["league"]["rating"]
    data.append(tr)
    data_x.append(i/len(base["data"]["users"])*100)


plt.scatter(data_x, data, s = .001)
plt.xlabel("percentile")
plt.ylabel("TR")
plt.grid(True)
plt.yticks([y*1000 for y in range(26)])
plt.xticks([5*x for x in range(21)])
plt.show()