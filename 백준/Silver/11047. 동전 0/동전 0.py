# 동전 0
import sys
input = sys.stdin.readline
n,k = map(int, input().split())
coins = sorted([int(input().strip()) for _ in range(n)], reverse = True)
cnt = 0
for coin in coins:
    if k ==0 : 
        break
    if coin > k:
        continue
    else:
        cnt += k//coin
        k = k%coin
        # while coin <= k:
        #     k -= coin
        #     cnt+=1  
print(cnt)