import requests
from urllib import parse
summoner = "원딜 억제기"
DEVELOPMENTAPIKEY = "RGAPI-a3f179b2-640b-4872-8b60-cef1d83f077e"
encodingSummonerName = parse.quote(summoner)
APIURL = "https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + encodingSummonerName
headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": DEVELOPMENTAPIKEY,
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
res = requests.get(APIURL, headers=headers)
data = res.json()
def apiKey():
    return DEVELOPMENTAPIKEY
def encryptaccountId():
    return data["accountId"]
