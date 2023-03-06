import sys, os, requests, json
from dotenv import load_dotenv

load_dotenv()
TETRIO_TOKEN = os.getenv('TETRIO_TOKEN')

r = requests.get('https://tetr.io/api/games/'+sys.argv[1],headers={"Authorization":'Bearer ' + TETRIO_TOKEN})
json.dump(r.json()['game'],open(sys.argv[1]+'.ttr','w'))