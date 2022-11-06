def null_Count(answers,questions):
    cnt=0
    q_cnt=0
    arr=[]
    for key,value in answers:
        arr.append(key)
    for i in range(len(answers)):
        q_cnt+=1
        if answers[i][arr[i]]['skipped']:
            cnt+=1
    if q_cnt!=len(questions):
        q_cnt+=1
        cnt+=1
    score=0
    if q_cnt>0:
        score=cnt/q_cnt
    if cnt>=q_cnt//2:
        return {"value":True,"Total Questions":q_cnt,"Number of questions skipped":cnt,"score":score*0.3}
    return {"value":False,"Total Questions":q_cnt,"Number of questions skipped":cnt,"score":score}