def solution(x, y, n):
    dp = [1e9]*(y+1)
    dp[y]=0
    for i in range(y-1,0,-1):
        if i+n<=y:
            dp[i]=min(dp[i+n]+1,dp[i])
        if i*2<=y:
            dp[i]=min(dp[i*2]+1,dp[i])
        if i*3<=y:
            dp[i]=min(dp[i*3]+1,dp[i])
    # print(dp)
#     def func1(num):
#         if num-n>0:
#             dp[num-n] = min(dp[num-n],dp[num]+1)
#             func1(num-n)
#         else:
#             return
        
#     def func2(num):
#         if num%2==0 and num//2>0:
#             dp[num//2] = min(dp[num//2],dp[num]+1)
#             func2(num//2)
#         else:
#             return
    
#     def func3(num):
#         if num%3==0 and num//3>0:
#             dp[num//3] = min(dp[num//3],dp[num]+1)
#             func3(num//3)
#         else:
#             return
        
#     func1(y)
#     func2(y)
#     func3(y)
    
    # # x+n
    # num=y
    # while num-n>0:
    #     dp[num-n] = min(dp[num-n],dp[num]+1)
    #     num-=n
    # # x*2
    # num=y
    # while num%2==0 and num//2>0:
    #     dp[num//2] = min(dp[num//2],dp[num]+1)
    #     num//=2
    # # x*3
    # num=y
    # while num%3==0 and num//3>0:
    #     dp[num//3] = min(dp[num//3],dp[num]+1)
    #     num//=3
    
    if dp[x]==1e9:
        return -1
    else:
        return dp[x]