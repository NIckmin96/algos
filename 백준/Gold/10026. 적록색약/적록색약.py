# 적록색약
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())
graph = [list(input().strip()) for _ in range(n)]
new_graph = [[i.replace('G','R') for i in row] for row in graph]

def bfs(x,y,graph):
    q = deque()
    q.append((x,y))
    graph[x][y]=0
    while q:
        x,y = q.popleft()
        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            if (0<=x+dx<n)&(0<=y+dy<n):
                if (graph[x+dx][y+dy]==color):
                    q.append((x+dx,y+dy))
                    graph[x+dx][y+dy]=0
    return graph

# 정상 케이스
cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            color=graph[i][j]
            graph = bfs(i,j,graph)
            # q = deque()
            # q.append((i,j))
            # graph[i][j]=0
            # while q:
            #     x,y = q.popleft()
            #     for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
            #         if (0<=x+dx<n)&(0<=y+dy<n):
            #             if (graph[x+dx][y+dy]==color):
            #                 q.append((x+dx,y+dy))
            #                 graph[x+dx][y+dy]=0
            cnt+=1
print(cnt, end=' ')
# 색약 케이스
cnt = 0
for i in range(n):
    for j in range(n):
        if new_graph[i][j]:
            color=new_graph[i][j]
            # new_graph = bfs(i,j,new_graph)
            q = deque()
            q.append((i,j))
            new_graph[i][j]=0
            while q:
                x,y = q.popleft()
                for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                    if (0<=x+dx<n)&(0<=y+dy<n):
                        if (new_graph[x+dx][y+dy]==color):
                            q.append((x+dx,y+dy))
                            new_graph[x+dx][y+dy]=0
            
            cnt+=1
print(cnt)