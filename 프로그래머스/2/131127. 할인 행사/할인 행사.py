def solution(want, number, discount):
    answer = 0
    dic = dict(zip(want, number))
    for i in range(len(discount)+1-10):
        tmp=dic.copy()
        for j in discount[i:i+10]:
            if (j in tmp.keys()):
                if tmp[j]>0:
                    tmp[j]-=1
        if sum(list(tmp.values()))==0:
            answer+=1
    return answer