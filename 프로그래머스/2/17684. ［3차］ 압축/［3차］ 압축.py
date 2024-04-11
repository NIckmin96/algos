def solution(msg):
    answer = []
    import re
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P',
               'Q','R','S','T','U','V','W','X','Y','Z']
    dic = {v:i+1 for i,v in enumerate(alphabet)}
    # print(sorted(dic.keys(), key=lambda x:[len(x),x]))
    def dp(msg):
        for k in sorted(dic.keys(), key=lambda x:[-len(x),x]):
            res = re.match(f'{k}',msg)
            if res:
                word = res.group()
                # print(word)
                answer.append(dic[word])
                start,end = res.span()
                if end<len(msg):
                    dic[word+msg[end]]=max(dic.values())+1
                    msg = msg[end:]
                else:
                    msg = ''
                return msg
    # dp(msg)
    
    # print(re.match('KA','KAKAO'))
                
    while msg:
        msg = dp(msg)
    
    return answer