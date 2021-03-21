import requests
import json

url = "https://m.land.naver.com/cluster/ajax/articleList"
HEAD = {
        'User-Agent': "PostmanRuntime/7.20.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "adbba748-cb85-4fb4-8f6a-4be441f19cc3",
        'Host': "m.land.naver.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

def getSoup(DONG,LAT,LON,PAGE):
##행정동 및 위도 경도##변수 입력
    dong={"cortarNo":DONG}
    lat={"lat":LAT}
    lon={"lon":LON}
    page={"page":PAGE}
  ##고정값
    con1= {"rletTpCd":"DDDGG%3AGM"} ## 검색물건
    con2= {"tradTpCd":"A1"} ##거래방법 A1 : 매매
    con3={"showR0":""}    ## 그외조건 없음
    con4 = {"z":"7"}  ## 축척
  ##검색조건
    space1={"spcMin":"132"} ##40평이상
    space2={"spcMax":"900000000"} ## 무한
    price1={"dprcMin":"30000"} ##3억이상 10억 미만
    price2={"dprcMax":"100000"}
  ##mapping 고정값
    rgt = {"rgt": str(float(lat["lat"])+0.3475542)}
    lft = {"lft": str(float(lat["lat"])-0.3475542)}
    top = {"top": str(float(lon["lon"])+0.0538928)}
    btm = {"btm": str(float(lon["lon"])-0.0538928)}
    qstring={**con1,**con2,**con3,**con4,**space1,**space2,**price1,**price2,**dong,**lat,**lon,**lft,**rgt,**top,**btm,**page}
    result=requests.request("GET",url,headers=HEAD,params=qstring,timeout=5)
    text=json.loads(result.text)
    return text