def solution(s):
    answer = []
    cnt = 0
    zeros = 0
    
    def transform(x,zeros):
        res = ''
        zeros += x.count('0')
        x = x.replace('0','')
        x = len(x)
        
        while x!=0:
            leftover = x%2
            x = x//2
            res+=str(leftover)
            
        return res[::-1],zeros
    	
    while s!='1':
        s,zeros = transform(s,zeros)
        cnt+=1
        
    answer = [cnt,zeros]
    
    return answer