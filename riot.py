import requests
import json
import os
API_KEY = str(os.environ['riotToken'])
HEADURL = "https://kr.api.riotgames.com/"

def get_SummonerId(summonerName):
    url = f"{HEADURL}lol/summoner/v4/summoners/by-name/{summonerName}/?api_key={API_KEY}"
    req = requests.get(url)
    if req.status_code == 200:
        return req.json()
    elif req.status_code == 403:
        return 403
    else:
        return req.status_code

def get_summonerRank(summoner):
    url = f"{HEADURL}lol/league/v4/entries/by-summoner/{summoner}/?api_key={API_KEY}"
    req = requests.get(url)
    if req.status_code == 200:
        return json.loads(req.text)
    elif req.status_code == 403:
        print(req.status_code)
        return 403
    else:
        print(req.status_code)
        return req.status_code
    