def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    distance = [[0]*m for _ in range(n)]
    # bfs
    from collections import deque
    q = deque([(0,0,0)])
    maps[0][0]=-1
    
    while q:
        x,y,dist = q.popleft()
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if (0<=x+dx<n)&(0<=y+dy<m):
                if (maps[x+dx][y+dy]==1)&(distance[x+dx][y+dy]==0):
                    q.append((x+dx,y+dy,dist+1))
                    maps[x+dx][y+dy]=-1
                    distance[x+dx][y+dy]=dist+1
                    
    if distance[n-1][m-1]:
        answer=distance[n-1][m-1]+1
    else:
        answer=-1
        
    return answer