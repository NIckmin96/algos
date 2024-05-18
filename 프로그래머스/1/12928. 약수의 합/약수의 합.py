def solution(n):
    answer = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            div = int(n/i)
            answer+=i
            if i!=div:
                answer+=div
    return answer