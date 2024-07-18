def solution(queue1, queue2):
    from collections import deque
    q = queue1+queue2
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(q1)
    s2 = sum(q2)
    
    for i in range(3*len(q1)):
        if s1==s2:
            return i
        elif s1>s2:
            num = q1.popleft()
            q2.append(num)
            s1-=num
            s2+=num
        else:
            num = q2.popleft()
            q1.append(num)
            s1+=num
            s2-=num

    return -1