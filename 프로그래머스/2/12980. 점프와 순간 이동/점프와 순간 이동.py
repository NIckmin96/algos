def solution(n):
    ans = 0
#     dp = [0]*(n+1)
#     # 1칸 이동
#     dp[1] = 1
#     for i in range(2, n+1):
#         if (i%2==0):
#             dp[i] = dp[i//2]
#         else:
#             dp[i] = dp[i-1]+1
            
#     ans = dp[n]
    cnt = 1
    while n>1:
        if n%2==0:
            n//=2
        else:
            n-=1
            cnt+=1
    ans=cnt
    
    return ans