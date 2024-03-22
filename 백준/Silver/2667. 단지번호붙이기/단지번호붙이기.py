# 단지 번호 붙이기
# 그래프 순회 하면서, 1인 경우 찾기 -> bfs로 연결된 부분 찾아내고 라벨링 -> 다시 순회 하면서, 1인 경우 찾기
n = int(input())
graph = [list(map(int, list(input()))) for _ in range(n)]
cluster = -1
from collections import deque
cnt_lst = []
def bfs(x,y):
    global graph, cluster, cnt_lst
    q = deque()
    q.append((x,y))
    graph[x][y]=cluster
    cnt=1
    while q:
        x,y = q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if (0<=x+dx<n)&(0<=y+dy<n):
                if (graph[x+dx][y+dy]==1):
                    q.append((x+dx,y+dy))
                    graph[x+dx][y+dy]=cluster
                    cnt+=1
    cluster-=1
    cnt_lst.append(cnt)
# 그래프 순회
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            bfs(i,j)
print(abs(cluster)-1)
for i in sorted(cnt_lst):
    print(i)