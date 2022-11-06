import readtime
from questionTypes import questionTypes
def is_Speeding(payload):
    questions=payload['Questions']
    answers=payload['Responses']
    Total_Predicted_Time=0
    readTime=0
    writeTime=0
    temp=""
    
    temp+=questions[0]['txt']
    for i in range(1,len(questions)):
        temp+=' '+questions[i]['rtxt']['blocks'][0]['text']
    readTime=readtime.of_text(temp)
    
    Total_Predicted_Time+=readTime.seconds

    arr=[]
    answers_Array=answers['answers']
    for key,value in answers_Array:
        arr.append(key)
    for i in range(len(answers_Array)):
        if questionTypes['Text'] in answers_Array[i]:
            if 'data' in answers_Array[i][questionTypes['Text']]:
                words=(answers_Array[i][questionTypes['Text']]['data']).split()
                writeTime+=0.8*len(words)
        else:
            if answers_Array[i][arr[i]]['skipped']:
                continue
            else:
                writeTime+=0.5
   
    Total_Predicted_Time=readTime.seconds+writeTime
    if Total_Predicted_Time<answers['timeTaken']:
        return {"value":False,"Predicted_Time":Total_Predicted_Time,"Actual_Time":answers['timeTaken'],"score":0}
    return {"value":True,"Predicted_Time":Total_Predicted_Time,"Actual_Time":answers['timeTaken'],"score":1*0.5}




