def solution(n):
    answer = 0
    lst = []
    num=1
    for i in range(1,101):
        while True:
            if ('3' in str(num))|(num%3==0):
                num+=1
            else:
                lst.append(num)
                num+=1
                break
        
    answer = lst[n-1]
    
    return answer