def solution(s):
    answer = 0
    def check(s):
        for _ in range(len(s)//2):
            if '()' in s:
                s = s.replace('()','')
            elif '[]' in s:
                s = s.replace('[]','')
            elif '{}' in s:
                s = s.replace('{}','')
        if s=='':
            return True
        else:
            return False
            
    if len(s)%2==0:
        # 0번째
        if check(s):
            answer+=1
        for i in range(1,len(s)):
            tmp = s[i:]+s[:i]
            if check(tmp):
                answer+=1
    return answer