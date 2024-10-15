def solution(board):
    answer = 0
    n = len(board)
    
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                for dx,dy in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                        board[nx][ny]=-1
    for i in range(n):
        for j in range(n):
            if board[i][j]==0:
                answer+=1
                
    return answer