def solution(clothes):
    answer = 1
    # 종류, 의상 구분하기
    dic = {}
    for v,k in clothes:
        if k in dic.keys():
            dic[k].append(v)
        else:
            dic[k]=[v]
            
    for v in dic.keys():
        answer*=(len(dic[v])+1)
    answer-=1
    return answer