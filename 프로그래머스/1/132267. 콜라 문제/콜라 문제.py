def solution(a, b, n):
    answer = 0
    while n>=a:
        n-=a
        answer+=b
        n+=b
    return answer