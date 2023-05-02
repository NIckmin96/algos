def solution(s):
    answer = ''
    s = s.lower()
    for i,v in enumerate(s):
        if (i==0) | (s[i-1]==' '):
            answer+=v.upper()
        else:
            answer+=v
    
    return answer