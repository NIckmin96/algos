def solution(n):
    answer = ''
    lst = sorted(list(str(n)), reverse=True)
    for i in lst:
        answer+=i
    
    return int(answer)