def solution(n):
    import sys
    sys.setrecursionlimit(100000)
    answer = 0
    lst = [0]*100001
    
    def fibo(n):
        if n==0:
            lst[0] = 0
            return lst[0]
        
        elif n==1:
            lst[1] = 1
            return lst[1]
        
        else:
            if lst[n]!=0:
                return lst[n]
            else:
                lst[n] = fibo(n-2)+fibo(n-1)
                return lst[n]
    
    fibo(n)
    # fibo(100000)
    answer = lst[n]%1234567
    # print(lst[:10])
    
    return answer