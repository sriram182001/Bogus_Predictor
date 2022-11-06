from flask import Flask
from flask import request
from is_Gibberish import is_gibberish 
from null_Count import null_Count
from is_Speeding import is_Speeding
from email_Valid import is_Email_InValid
from phone_Number_Check import phone_Number_Check

app = Flask(__name__)

@app.route('/is_spam', methods=["POST"])
def isSpam():
    try:
        
        if not request.is_json:
            return "Not a Json"
        payload=request.get_json()
        
        Response_Payload={}
        Response_Payload['is_Gibberish']=is_gibberish(payload['Responses'])
        Response_Payload['Null_Count']=null_Count(payload['Responses']['answers'],payload['Questions'])
        Response_Payload["is_Speeding"]=is_Speeding(payload)
        if 'email' in payload['Responses']:
            Response_Payload["is_Email_InValid"]=is_Email_InValid(payload['Responses']['email'])
        Response_Payload["is_Phone_Number_InValid"]=phone_Number_Check(payload['Responses']['answers'])
        
        is_spam=False
        aggregate=0
        no_of_spamField=0
        is_spam=False
        score=0


        for i in Response_Payload:
            if Response_Payload[i]['value']==True:
                aggregate+=Response_Payload[i]["score"]
                no_of_spamField+=1

        
        if no_of_spamField>0:
            score=aggregate/no_of_spamField
            if aggregate/no_of_spamField>0.5:
                is_spam=True
        
        return {"is_spam":is_spam,"parameters":Response_Payload,"score":score}
    except Exception as exp:
        print(repr(exp))
        return "Sometrhing went Wrong",500
    

@app.route('/',methods=["GET"])
def index():
    if request.method == 'GET':
        return "HI"
    else:
        return "Wrong Method"

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
     
    