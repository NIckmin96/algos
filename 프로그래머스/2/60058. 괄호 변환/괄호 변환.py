def solution(p):
    from collections import Counter
    
    def reverse(s):
        res = ''
        for char in s:
            if char=='(':
                res+=')'
            else:
                res+='('
        return res
    
    def check(s):
        # condition 1
        if s[0]!='(':
            return False
        # condition 2
        dic = dict(Counter(s))
        if dic['(']!=dic[')']:
            return False
        # condition 3
        for i in range(len(list(s))//2):
            s = s.replace('()','')
        if s!='':
            return False
        return True
    
    def func(p):
        if p=='':
            return ''
        if check(p):
            return p
        # 변환
        else: 
            l = len(list(p))
            start=0
            while True:
                dic = {'(':0, ')':0}
                for i in range(start,l):
                    char = p[i]
                    dic[char]+=1
                    if dic['(']==dic[')']:
                        if i==l-1:
                            u,v = p, ''
                        else:
                            u,v = p[:i+1], p[i+1:]
                        break
                    else:
                        start+=1
                        continue
                break
                    
            # print(u,v)
            # 3-1 u가 올바른 문자열인 경우
            if check(u):
                return u + func(v)
            # 4 u가 올바른 문자열이 아닌 경우
            else:
                s = '(' # 4-1
                s += func(v) # 4-2
                s += ')' # 4-3
                s += reverse(u[1:-1]) # 4-4
                return s
                    
    answer = func(p)
            
    return answer