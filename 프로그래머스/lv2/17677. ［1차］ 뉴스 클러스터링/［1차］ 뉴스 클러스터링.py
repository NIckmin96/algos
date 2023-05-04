def solution(str1, str2):
    answer = 0
    dic1,dic2 = {},{}
    inter_lst,union_lst = [],[]
    
    def check(s):
        for i in s:
            if not i.isalpha():
                return False
        return True
    
    for i in range(len(str1)-1):
        if check(str1[i:i+2]):
            if str1[i:i+2].lower() not in dic1.keys():
                dic1[str1[i:i+2].lower()] = 1
            else:
                dic1[str1[i:i+2].lower()] += 1
                
    for i in range(len(str2)-1):
        if check(str2[i:i+2]):
            if str2[i:i+2].lower() not in dic2.keys():
                dic2[str2[i:i+2].lower()] = 1
            else:
                dic2[str2[i:i+2].lower()] += 1
                
    # print(dic1)
    # print(dic2)

    # 교집합 구하기
    inter = set(dic1.keys()).intersection(dic2.keys())
    # print(inter)
    ## 교집합에 있는 원소들 중, 최소값 구하기
    for i in inter:
        inter_lst += [i]*min(dic1[i], dic2[i])
    # print(inter_lst)
    # 합집합 구하기
    union = set(dic1.keys()).union(dic2.keys())
    # print(union)
    for i in union:
        if i not in dic1.keys():
            union_lst += [i]*dic2[i]
        elif i not in dic2.keys():
            union_lst += [i]*dic1[i]
        else:
            union_lst += [i]*max(dic1[i],dic2[i])
    # print(union_lst)
    
    if len(inter_lst)==0 and len(union_lst)==0:
        zaccard = 1
    else:
        zaccard = len(inter_lst)/len(union_lst)
    answer = int(zaccard*65536)
    
    return answer