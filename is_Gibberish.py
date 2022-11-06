from gibberish_detector import detector
from questionTypes import questionTypes

def is_gibberish(answer):
    Email=None
    if 'email' in answer:
        Email=answer['email']
    Detector = detector.create_from_model('big.model')
    cnt=0
    q_cnt=0
    if Email:
        for i in answer['answers']:
            if questionTypes['Text'] in i:
                if "data" in i[questionTypes["Text"]]:
                    q_cnt+=1
                    if Detector.is_gibberish(i[questionTypes["Text"]]["data"]):
                        cnt+=1
    if 2*cnt>=q_cnt:
        return {"value":True,"Total Questions: ":q_cnt,"No of Gibberish Responses: ":cnt,"score":1*0.7}
    return {"value":False,"Total Questions: ":q_cnt,"No of Gibberish Responses: ":cnt,"score":0}
    


