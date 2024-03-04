# 특정 거리의 도시 찾기
import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n,m,k,x = map(int, input().strip().split())
graph = {i:[] for i in range(1,n+1)}
for _ in range(m):
    a,b = map(int, input().strip().split())
    graph[a].append(b)
visited = [False]*(n+1)
# bfs
q = deque([x]) # start
distance=0
def bfs(q):
    global visited, graph, distance, k
    next_q = deque()
    while q:
        node = q.popleft()
        visited[node]=True
        next = graph[node]
        for i in next:
            if not visited[i]:
                next_q.append(i)
                visited[i]=True
    distance+=1
    if distance==k:
        return next_q
    elif next_q:
        return bfs(next_q)
    return []

res = bfs(q)
if len(res)==0:
    print(-1)
else:
    for i in sorted(res):
        print(i)