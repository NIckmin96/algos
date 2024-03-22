# 미로 탐색
n,m = map(int, input().strip().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
distance = [[0]*m for _ in range(n)]
from collections import deque
# bfs
q = deque([(0,0)]) # start
distance[0][0]=1e9
while q:
    x,y = q.popleft()
    dist = distance[x][y]
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]: # 위, 아래, 왼, 오
        try:
            if (graph[x+dx][y+dy]==1)&(distance[x+dx][y+dy]==0)&(x+dx>=0)&(y+dy>=0):
                q.append((x+dx,y+dy))
                distance[x+dx][y+dy]=dist+1
        except IndexError:
            continue
        
print(int(distance[n-1][m-1]-1e9+1))