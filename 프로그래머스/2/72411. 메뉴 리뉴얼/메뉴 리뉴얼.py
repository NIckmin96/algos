def solution(orders, course):
    from itertools import combinations
    answer = []
    for c in course: # 10
        s = set()
        for i in range(len(orders)): # 20
            for j in range(i+1,len(orders)): # 20
                inter = ''.join(list(set(orders[i])&set(orders[j])))
                # print(inter)
                if len(inter)>=c:
                    combs = list(combinations(list(inter),c))
                    combs = list(map(lambda x:''.join(sorted(x)), combs))
                    for comb in combs:
                        s.add(comb)
        _max = 0
        lst = []
        for x in s:
            cnt = 0
            for order in orders:
                if len(set(x)&set(order))==c:
                    cnt+=1
            if _max<cnt:
                lst = []
                lst.append(x)
                _max=cnt
            elif _max==cnt:
                lst.append(x)
        answer += lst
                    
    return sorted(answer)