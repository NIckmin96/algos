# 회의실 배정
import sys
input = sys.stdin.readline
n = int(input().strip())
lst = []
for _ in range(n):
    start,end = map(int, input().strip().split())
    lst.append([start, end])
# 1. 끝나는 시간 기준으로 정렬 + 빨리 시작하는 시간 기준 정렬
sorted_lst = sorted(lst, key=lambda x:(x[1], x[0]))
min_end = min(list(map(lambda x:x[1], sorted_lst)))
res = []
# 2. 끝나는 시간과 다음 시작 시간 비교해서, 끝나는 시간보다 크거나 같은 경우 cnt++
start,end = sorted_lst[0]
cnt = 1
for i in range(1,n):
    if sorted_lst[i][0]>=end:
        cnt+=1
        end=sorted_lst[i][1]
print(cnt)