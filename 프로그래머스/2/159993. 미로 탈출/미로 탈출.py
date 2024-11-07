def solution(maps):
    from copy import deepcopy
    from collections import deque
    answer=0
    n = len(maps)
    m = len(maps[0])
    visited = [[0]*m for _ in range(n)]
    # locate [start, exit, lever]
    for i in range(n):
        for j in range(m):
            if maps[i][j]=='S':
                start = (i,j)
            elif maps[i][j]=='E':
                exit = (i,j)
            elif maps[i][j]=='L':
                lever = (i,j)
    # bfs
    def bfs(visited, start, end):
        q = deque([start])
        visited[start[0]][start[1]]=1
        while q:
            x,y = q.popleft()
            if x==end[0] and y==end[1]:
                return visited[x][y]-1
            for nx,ny in [(x-1,y), (x,y+1), (x+1,y), (x, y-1)]:
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and maps[nx][ny]!='X' :
                    q.append((nx,ny))
                    visited[nx][ny]=visited[x][y]+1
                    
        return visited[end[0]][end[1]]-1
            
    # start ~ lever 까지의 최소시간
    dist1 = bfs(deepcopy(visited),start,lever)
    # lever ~ exit 까지의 최소시간
    dist2 = bfs(deepcopy(visited),lever,exit)
    
    if dist1==-1 or dist2==-1:
        return -1
    else:
        answer = dist1+dist2
        
    return answer