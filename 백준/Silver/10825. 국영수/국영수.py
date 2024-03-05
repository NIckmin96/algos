# 국영수
import sys
input = sys.stdin.readline
n = int(input().strip())
lst = []
for _ in range(n):
    lst.append(input().strip().split())
# 정렬(multiple keys)
lst = sorted(lst, key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in lst:
    print(i[0])