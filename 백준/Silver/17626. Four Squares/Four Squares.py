# Four squares
import math

n = int(input())
dp = [0]*(n+1)
dp[1]=1
for i in range(2,n+1):
    _min=1e9
    for j in range(1,int(math.sqrt(i))+1):
        _min = min(_min, dp[i-j**2])
    dp[i]=_min+1
print(dp[n])