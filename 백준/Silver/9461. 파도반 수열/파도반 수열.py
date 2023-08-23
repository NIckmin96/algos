# 파도반 수열
import sys
input = sys.stdin.readline
n = int(input().strip())
dp = [1]*101
dp[3],dp[4] = 2,2
for i in range(5,101):
    dp[i] = dp[i-1]+dp[i-5]
for _ in range(n):
    num = int(input().strip())
    print(dp[num-1])