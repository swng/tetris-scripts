import requests
import json
import time

base_user_url = "https://ch.tetr.io/api/users/"

base_url = "https://ch.tetr.io/api/users/lists/xp"

all_badges = ["infdev", "early-supporter", "allclear", "100player", "20tsd", "secretgrade", "kod_founder", "superlobby", "wpl_1", "ttsdtc_1", "underdog_predict", "leaderboard1", "mmc_tabi_superlobby", "tiolatam_3", "underdog_3", "ttsdtc_2", "underdog_2", "underdog_1", "wpl_3", "mmc_tabi_3", "hdoxii_2", "ttsdtc_3", "mmc_tabi_2", "indev", "bugbounty", "ggc_3", "wpl_2", "hdoxii_3", "mmc_tabi_1", "heart", "poop", "founder", "tiolatam_2", "tiolatam_1", "ggc_2"]

after = 309750 # current max is musik at 20,000,000

response = requests.get(base_url, params={"limit":100,"after":after})
base = response.json()
users = base["data"]["users"]

while len(users) > 0: 
        print(users[0]["username"])
        for user in users:
            time.sleep(1) # wait a sec don't wannt overload tetrio servers on meaningless trivia hunt
            #print(user["username"])
            
            user_id = user["_id"]
            user_response = requests.get(base_user_url + user_id)
            user_json = user_response.json()

            user_badges = user_json['data']['user']['badges']

            for badge in user_badges:
                if badge['id'] not in all_badges:
                    print(badge['id'], badge['label'])
                    all_badges.append(badge['id'])
            
        after = users[-1]["xp"]
        response = requests.get(base_url, params={"limit":100,"after":after})
        if response.status_code == 200:
            base = response.json()
            users = base["data"]["users"]
        else:
            print("SOMETHING WENT WRONG")
            users = []

print(all_badges)