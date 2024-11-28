def solution(board):
    from collections import deque
    d = ''
    n = len(board)
    answer = []
    board[0][0] = {'':0}
    q = deque([(0,0,d)])
    while q:
        x,y,d = q.popleft()
        for nx,ny in [(x-1,y),(x,y+1),(x+1,y),(x,y-1)]:
            if not (nx==0 and ny==0) and (0<=nx<n and 0<=ny<n) and board[nx][ny]!=1:
                if (d=='h' and x!=nx) or (d=='v' and y!=ny): # corner
                    nd = 'h' if d=='v' else 'v'
                    if board[nx][ny]==0:
                        board[nx][ny] = dict()
                        board[nx][ny][nd] = board[x][y][d]+600
                        q.append((nx,ny,nd))
                    else:
                        if not board[nx][ny].get(nd):
                            board[nx][ny][nd] = board[x][y][d]+600
                            q.append((nx,ny,nd))
                        elif board[nx][ny][nd]>board[x][y][d]+600:
                            board[nx][ny][nd]=board[x][y][d]+600
                            q.append((nx,ny,nd))
                    
                            
                else: # straight
                    nd = 'h' if ny!=y else 'v'
                    if board[nx][ny]==0:
                        board[nx][ny] = dict()
                        board[nx][ny][nd] = board[x][y][d]+100
                        q.append((nx,ny,nd))
                    else:
                        if not board[nx][ny].get(nd):
                            board[nx][ny][nd] = board[x][y][d]+100
                            q.append((nx,ny,nd))
                        elif board[nx][ny][nd]>board[x][y][d]+100:
                            board[nx][ny][nd]=board[x][y][d]+100
                            q.append((nx,ny,nd))
                        
                        
    # print(board)
    answer = min(board[n-1][n-1].values())
                
    return answer