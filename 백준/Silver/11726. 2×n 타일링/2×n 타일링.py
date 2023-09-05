# 2×n 타일링 -> 피보나치
import sys
input = sys.stdin.readline
n = int(input().strip())
dp = [0]*1001
dp[0]=1
dp[1]=1
for i in range(2,1001):
    dp[i] = dp[i-2]+dp[i-1]
    
print(dp[n]%10007)