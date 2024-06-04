def solution(routes):
    answer = 1
    routes = sorted(routes,key=lambda x:(x[0],-x[1]))
    # inter = None
    # for start,end in routes:
    #     if not inter:
    #         inter = set(range(start,end+1))
    #     else:
    #         inter = inter&set(range(start,end+1))
    #     if not inter:
    #         answer+=1
    #         inter = set(range(start,end+1))
    start,end = -30000,30000
    for s,e in routes:
        start = max(start,s)
        end = min(end,e)
        # print(start,end)
        if start>end:
            start = s
            end = e
            answer+=1
        
            
        
    return answer