import requests
from questionTypes import questionTypes

def phone_Number_Check(answers):
    q_cnt=0
    cnt=0
    url="https://api.apilayer.com/number_verification/validate"
    for i in answers:
        if questionTypes['PhoneNumber'] in i:
            q_cnt+=1
            if "data" in i[questionTypes["PhoneNumber"]]:
                res=requests.get(url,params={"number":i[questionTypes["PhoneNumber"]]["data"]},headers={"apikey":"k0O2cwWQuT7ewl3JFh9eNzEeRccAtwr3"})
                if not res.json()['valid']:
                    cnt+=1
    if cnt>0:
        return{"value":True,"No of PhoneNumberType Questions":q_cnt,"No of invalid phone Numbers":cnt,"score":1}
    return{"value":False,"No of PhoneNumberType Questions":q_cnt,"No of invalid phone Numbers":cnt,"score":0}

