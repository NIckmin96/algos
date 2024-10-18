def solution(maps):
    from collections import deque
    maps = list(map(lambda x:list(x), maps))
    n,m = len(maps), len(maps[0])
    answer = []
    for i in range(n):
        for j in range(m):
            if maps[i][j].isdigit():
                q = deque([(i,j)])
                food = int(maps[i][j])
                maps[i][j]='O'
                while q:
                    x,y = q.popleft()
                    for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
                        nx, ny = x+dx, y+dy
                        if 0<=nx<n and 0<=ny<m and maps[nx][ny].isdigit():
                            q.append([nx,ny])
                            food+=int(maps[nx][ny])
                            maps[nx][ny] = 'O'
                            
                answer.append(food)
                
    if len(answer)==0: 
        return [-1]
    else:
        return sorted(answer)
    
    return answer