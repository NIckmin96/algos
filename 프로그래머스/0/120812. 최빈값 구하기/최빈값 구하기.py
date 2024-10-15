def solution(array):
    from collections import Counter
    dic = dict(Counter(array))
    num, count = sorted(dic.items(), key=lambda x:x[1])[-1]
    count_count = dict(Counter(dic.values()))
    if count_count[count]>1:
        return -1
    else:
        return num