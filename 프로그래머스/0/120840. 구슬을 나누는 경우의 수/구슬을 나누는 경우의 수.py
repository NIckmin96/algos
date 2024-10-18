def solution(balls, share):
    import math
    if balls!=share:
        answer = math.factorial(balls)//math.factorial(share)//math.factorial(balls-share)
    else:
        answer=1
    return answer