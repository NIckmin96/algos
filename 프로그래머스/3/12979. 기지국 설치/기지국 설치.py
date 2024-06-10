def solution(n, stations, w):
    answer = 0
    # 전파가 닿지 않는 지점 -> segment -> w의 거리(양옆)으로 나눈 몫+1(if mod>0)
    lst = []
    end = 0
    for station in stations:
        start = station-w
        # lst.append(start-end-1)
        div,mod = divmod(start-end-1,2*w+1)
        if mod>0:
            answer+=(div+1)
        else:
            answer+=div
        end = station+w
    if end<n:
        # lst.append(n-end)
        div,mod = divmod(n-end,2*w+1)
        if mod>0:
            answer+=(div+1)
        else:
            answer+=div
    # for i in lst:
    #     div,mod = divmod(i,2*w+1)
    #     if mod>0:
    #         answer+=(div+1)
    #     else:
    #         answer+=div

    return answer