def solution(n, lost, reserve):
    answer = 0
    inter = set(reserve).intersection(set(lost))
    reserve = list(set(reserve)-inter)
    lost = list(set(lost)-inter)
    for i in sorted(reserve):
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    answer = n-len(lost)
            
    return answer