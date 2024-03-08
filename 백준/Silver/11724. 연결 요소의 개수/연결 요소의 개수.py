# 연결 요소의 개수
# dfs로 접근 / 다시 원래의 노드로 돌아오면 연결 요소 count
import sys
input = sys.stdin.readline
n,m = map(int, input().strip().split())
graph_dic = {i:[] for i in range(1,n+1)}
for _ in range(m):
    u,v = map(int,input().strip().split())
    graph_dic[u].append(v)
    graph_dic[v].append(u)
visited = [False]*(n+1)

# while sum(visited)<n:
for i in range(1, len(visited)):
    if not visited[i]:
        start = i
        break

cnt = 0
# dfs
def dfs(start, visited):
    global cnt
    stack = [start]
    while stack:
        start = stack.pop()
        if not visited[start]:
            visited[start]=True
            for i in graph_dic[start]:
                if i not in stack:
                    stack.append(i)
    cnt+=1
    if sum(visited)==n:
        return cnt
    else:
        for i in range(1, len(visited)):
            if not visited[i]:
                start = i
                break
        return dfs(start, visited)

    
cnt = dfs(start, visited)
print(cnt)
        