def solution(ingredient):
    from collections import deque
    q = deque(ingredient)
    answer = 0
    ### FAIL ###
    # ingredient = ('').join(list(map(str,ingredient)))
    # cnt = ingredient.count('1231')
    # while cnt>0:
    #     ingredient = ingredient.replace('1231','')
    #     answer+=1
    #     cnt = ingredient.count('1231')
    #     print(ingredient)
    
    res=''
    while q:
        if res[-4:]=='1231':
            answer+=1
            res=res[:-4]
            # res=res.replace('1231','')
        res+=str(q.popleft())
        # print(res)
            
    if res[-4:]=='1231':
        answer+=1
            
    
    return answer