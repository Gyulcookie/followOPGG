import getData
import requests
encryptId = getData.encryptaccountId()
DEVELOPMENTAPIKEY = getData.apiKey()
headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": DEVELOPMENTAPIKEY,
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
APIURL = "https://kr.api.riotgames.com/lol/match/v4/matchlists/by-account/" + encryptId
res = requests.get(APIURL, headers=headers)
data = res.json()
#print(data["matches"][0]["gameId"])
#print(data)