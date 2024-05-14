# N과 M(5)
import sys
input = sys.stdin.readline
n,m = map(int, input().strip().split())
n_lst = sorted(list(map(int, input().strip().split())))
visited = {i:False for i in n_lst}

def dfs(stack):
    if len(stack)==m:
        print((' ').join(map(str, stack)))
        return 
    for num in n_lst:
        if not visited[num]:
            stack.append(num)
            visited[num]=True
            dfs(stack)
            visited[num]=False
            stack.pop()

for i in n_lst:
    visited[i]=True
    dfs([i])
    visited[i]=False