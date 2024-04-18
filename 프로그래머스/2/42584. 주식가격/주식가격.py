def solution(prices):
    answer = []
    from collections import deque
    q = deque(prices)
    while q:
        tmp = q.popleft()
        cnt=0
        if q:
            for i in q:
                cnt+=1
                if i<tmp:
                    break
        else:
            cnt=0
        answer.append(cnt)
    return answer