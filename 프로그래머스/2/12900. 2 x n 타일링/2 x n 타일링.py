def solution(n):
    # 1,2의 조합으로 n을 만드는 경우의 수 -> combination 개념으로 점화식 만들수 있음
    # def combination(a,b):
    #     res = 1
    #     for i in range(a,a-b,-1):
    #         res*=i
    #     for i in range(1,b+1):
    #         res/=i
    #     return int(res)
    # lst = [combination(n-i,i)%1000000007 for i in range(n//2+1)]
    # answer = sum(lst)
    # print(lst)
    
    dp = [0]*(n+1)
    dp[0]=1
    dp[1]=1
    
    for i in range(2,n+1):
        dp[i]=(dp[i-2]+dp[i-1])%1000000007
        
    answer=dp[n]
    
    # def fibo(num):
    #     if dp[num]:
    #         return dp[num]
    #     else:
    #         dp[num] = (fibo(num-1)+fibo(num-2))%1000000007
    #         return dp[num]
    # answer = fibo(n)
        
    return answer