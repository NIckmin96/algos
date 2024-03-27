def solution(k, tangerine):
    answer = 0
    lst = [0]*(max(tangerine)+1)
    for i in tangerine:
        lst[i]+=1
    for i in sorted(lst, reverse=True):
        if k>0:
            k-=i
            answer+=1
        else:
            break
    
    return answer