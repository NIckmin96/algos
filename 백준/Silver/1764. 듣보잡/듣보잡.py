# 듣보잡
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
hear = set([input().strip() for _ in range(n)])
see = set([input().strip() for _ in range(m)])
res = sorted(list(hear.intersection(see)))
print(len(res))
for i in res:
    print(i)