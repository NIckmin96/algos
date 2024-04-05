# 토마토
import sys
from collections import deque
m,n,h = map(int, input().strip().split())
graph = [[[0]*m for _ in range(n)] for _ in range(h)]
for i in range(h,0,-1):
    graph[i-1] = [list(map(int, input().strip().split())) for _ in range(n)]
q = deque()
def bfs(q, graph):
    new_q = deque()
    while q:
        h,n,m = q.popleft()
        graph[h][n][m] = 2
        for dh, dn, dm in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]: # 위, 아래, 앞(2차원 위), 뒤(2차원 아래), 왼, 오
            try:
                if (graph[h+dh][n+dn][m+dm]==0)&(h+dh>=0)&(n+dn>=0)&(m+dm>=0):
                    graph[h+dh][n+dn][m+dm]=2
                    new_q.append((h+dh, n+dn, m+dm))
            except IndexError:
                continue
    return new_q, graph
# 1. 익은 토마토 위치 찾기(1)
_0 = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                q.append((i,j,k))
            if graph[i][j][k]==0:
                _0+=1
if _0:
    # 2. bfs
    cnt=-1
    while q:
        q,graph = bfs(q,graph)
        # print(graph)
        cnt+=1
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k]==0:
                    cnt=-1
                    break
    print(cnt)
else:
    print(0)