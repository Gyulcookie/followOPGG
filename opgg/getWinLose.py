import getData
import requests
import getMatch
encryptId = getData.encryptaccountId()
DEVELOPMENTAPIKEY = getData.apiKey()
summonerName = getData.summoner.replace(" ","").lower()
headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": DEVELOPMENTAPIKEY,
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"
    }
def WinorLose(index):
    matchId =  getMatch.data["matches"][index]["gameId"]
    APIURL = "https://kr.api.riotgames.com/lol/match/v4/matches/" + str(matchId)
    res = requests.get(APIURL, headers=headers)
    data = res.json()
    result = "패배"
    if(data["teams"][0]["win"]=="Fail"):
        for i in range(5,10):
            if(data["participantIdentities"][i]["player"]["summonerName"].replace(" ","").lower()==summonerName):
                result = "승리"
    if(data["teams"][0]["win"]=="Win"):
        for i in range(0,5):
            if(data["participantIdentities"][i]["player"]["summonerName"].replace(" ","").lower()==summonerName):
                result = "승리"
    print(result)
 
if __name__== "__main__":
    for j in range(0,10):
       WinorLose(j)