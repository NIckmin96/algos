# 경로 찾기
import sys
input = sys.stdin.readline
n = int(input().strip())
graph = [list(map(int, input().strip().split())) for _ in range(n)]

# 플로이드 워셜
from copy import deepcopy
dist =  deepcopy(graph)
# 1. init distance
for i in range(n):
    for j in range(n):
        if dist[i][j]==0:
            dist[i][j]=1e9
# update distance
for k in range(n): # 거쳐갈 노드
    for i in range(n):
        if i==k:
            continue
        for j in range(n):
            if j==k:
                continue
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

for i in range(n):
    for j in range(n):
        if dist[i][j]!=1e9:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print('')