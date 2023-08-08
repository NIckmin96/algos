# ATM
import sys
input = sys.stdin.readline
n = int(input().strip())
lst = sorted(list(map(int, input().split())))
res = 0
for i in range(n):
    res += sum(lst[:i+1])
print(res)