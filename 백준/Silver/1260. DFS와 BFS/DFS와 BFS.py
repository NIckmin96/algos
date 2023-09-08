# DFS와 BFS
import sys
from collections import deque
input = sys.stdin.readline
n,m,v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs, visited_bfs = [False]*(n+1), [False]*(n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 모범답안
def dfs(start):
    if not visited_dfs[start]:
        visited_dfs[start]=True
        print(start, end=' ')
        for i in sorted(graph[start]):
            if not visited_dfs[i]:
                dfs(i)

def bfs(start):
    q = deque([start])
    while q:
        i = q.popleft()
        if not visited_bfs[i]:
            visited_bfs[i]=True
            print(i, end=' ')
            for j in sorted(graph[i]):
                q.append(j)
    
# recursion error
# def dfs(start):
#     if sum(visited_dfs)==n:
#         return None
#     if visited_dfs[start]:
#         if len(graph[start])>0:
#             leaf = graph[start]
#             for i in sorted(leaf):
#                 dfs(i)
#         else:
#             return None
#     else:
#         visited_dfs[start]=True
#         print(start, end=' ')
#         leaf = graph[start]
#         for i in sorted(leaf):
#             if visited_dfs[i]:
#                 continue
#             else:
#                 dfs(i)
    
# def bfs(start):
#     if sum(visited_bfs)==n:
#         return None
#     if visited_bfs[start]:
#         if len(graph[start])>0:
#             leaf = graph[start]
#             for i in sorted(leaf):
#                 if visited_bfs[i]:
#                     continue
#                 visited_bfs[i]=True
#                 print(i,end= ' ')
#             return bfs(min(leaf))
#         else:
#             return None
#     else:
#         visited_bfs[start]=True
#         print(start, end=' ')
#         leaf = graph[start]
#         for i in sorted(leaf):
#             if visited_bfs[i]:
#                 continue
#             visited_bfs[i]=True
#             print(i, end=' ')
#         bfs(min(leaf))
        
dfs(v)
print('')
bfs(v)