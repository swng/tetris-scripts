import requests
import json


f = open("all.json", "r")
countries_json = json.load(f)

base_url = "https://ch.tetr.io/api/users/lists/xp"

for country in countries_json:
    response = requests.get(base_url, params={"country":country["alpha-2"]})
    if response.status_code == 200:
        base = response.json()
        users = base["data"]["users"]
        for user in users:
            if user["role"] == "bot":
                print(user["username"], country["name"])