# 구간 합 구하기 4
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
lst = list(map(int, input().split()))
res = [0]*(n+1)
res[0]=lst[0]
for i in range(1,len(lst)):
    res[i]=lst[i]+res[i-1]
for _ in range(m):
    i,j = map(int, input().split())
    print(res[j-1]-res[i-2])
#     print(sum(lst[i-1:j]))