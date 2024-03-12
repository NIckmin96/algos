# 쉬운 최단거리
import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline
# 목표지점에서 가까운 부분부터 거리 계산해나가기
n,m = map(int, input().strip().split())
graph = [list(map(int, input().strip().split())) for _ in range(n)]
# # 시작점 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            start = (i,j)
q = deque()
dist_graph = [[0]*m for _ in range(n)]
q.append(start)
# BFS로 접근해보기(수정)
while q:
    x,y = q.popleft()
    dist = dist_graph[x][y]
    for dx,dy in [(0,-1),(0,1),(-1,0),(1,0)]:
        try:
            if (x+dx<0)|(y+dy<0):
                continue
            if graph[x+dx][y+dy]==1:
                dist_graph[x+dx][y+dy]=dist+1
                graph[x+dx][y+dy]=0
                q.append((x+dx,y+dy))
        except IndexError:
            continue
# 원래갈 수 있는 땅에서 도달할 수 없는 땅
lst = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            lst.append((i,j))
for i,j in lst:
    dist_graph[i][j]=-1

for i in dist_graph:
    tmp = list(map(str, i))
    print((' ').join(tmp))