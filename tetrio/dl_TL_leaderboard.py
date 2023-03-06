import requests
import json
import datetime

temp = requests.get("https://ch.tetr.io/api/users/lists/league/all")
json.dump(temp.json(), open('TL_leaderboard_' + datetime.date.today().strftime('%m-%d')+'.json','w'))