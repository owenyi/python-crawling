import pandas as pd
from libs.getSoup import getSoup

def getPages(DONG, LAT, LON):
    datas = pd.DataFrame()
    data_fin = pd.DataFrame()

    for i in range(1, 20):
        if getSoup(DONG, LAT, LON, i)["more"] == True:
            data = getSoup(DONG, LAT, LON, i)["body"]
            datas = datas.append(data)
            colname = ["atclNo", "cortarNo", "rletTpCd", "tradTpCd", "flrInfo", "prc", "spc1", "spc2", "direction",
                       "lat", "lng", "atclFetrDesc", "tagList", "rltrNm"]
            data_fin = datas[colname]
            print("ok")
            i += 1
        elif getSoup(DONG, LAT, LON, i)["more"] == False:
            print("no")
            break
    data_fin.to_csv("../static/csv/gangnam.csv", header=True, index=False, encoding="utf-8")
    return data_fin