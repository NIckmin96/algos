# 1, 2, 3 더하기
import sys
input = sys.stdin.readline
t = int(input().strip())
dp = [0]*11
dp[1]=1
dp[2]=2*dp[1]
dp[3]=2*dp[2]

# dp Update
for i in range(4,11):
    dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
    
for _ in range(t):
    num = int(input().strip())
    print(dp[num])