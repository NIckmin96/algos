# 바이러스
import sys
input = sys.stdin.readline
n = int(input().strip())
k = int(input().strip())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(k): # Create Graph
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# Graph원소 1번부터 하나씩 돌면서, visited 체크하고 count하기
def bfs(i):
    if visited[i]:
        return None
    else:
        visited[i]=True
        lst = graph[i]
        for k in lst:
            bfs(k)

bfs(1)
print(sum(visited)-1)
    
