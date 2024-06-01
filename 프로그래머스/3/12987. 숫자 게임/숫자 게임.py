def solution(A, B):
    answer = 0
    from collections import deque
    A = sorted(A)
    B = sorted(B)
    q_A = deque(A)
    for num in B:
        if num>q_A[0]:
            q_A.popleft()
            answer+=1
    return answer