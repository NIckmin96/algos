def solution(s):
    from collections import deque
    answer = 0
    q_s = deque(s)
    q = deque([])
    # 문자열에서 큐로 하나씩 옮겨 중복 확인하기
    while q_s:
        q.append(q_s.popleft())
        if (len(q)>1) & (q[len(q)-1]==q[len(q)-2]):
            for i in range(2):
                q.pop()
            # print(q)
    # print(q)
    
    if len(q)==0:
        answer=1        

    return answer