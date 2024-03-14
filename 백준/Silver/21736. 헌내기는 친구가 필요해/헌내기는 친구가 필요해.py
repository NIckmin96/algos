# 헌내기는 친구가 필요해
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
# 시작점 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j]=='I':
            start = (i,j)
            break
q = deque()
q.append(start)
cnt = 0
# bfs
while q:
    x,y = q.popleft()
    if visited[x][y]==False:
        visited[x][y]=True
    for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        try:
            if (x+dx<0)|(y+dy<0):
                continue
            if (graph[x+dx][y+dy]=='O')&(visited[x+dx][y+dy]==False):
                q.append((x+dx,y+dy))
                visited[x+dx][y+dy]=True
            elif (graph[x+dx][y+dy]=='P')&(visited[x+dx][y+dy]==False):
                q.append((x+dx,y+dy))
                visited[x+dx][y+dy]=True
                cnt+=1
        except IndexError:
            continue
if cnt==0:
    print('TT')
else:
    print(cnt)