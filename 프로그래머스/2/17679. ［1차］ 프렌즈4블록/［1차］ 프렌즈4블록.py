def solution(m, n, board):
    board = [list(row) for row in board]
    answer = 0
    def check(x,y):
        if x+1<m and y+1<n and (0!=board[x][y]==board[x][y+1]==board[x+1][y]==board[x+1][y+1]):
            return True
        else:
            return False
    
    while True:
        check_all = False
        lst = []
        # 2x2 찾기
        for i in range(m):
            for j in range(n):
                if check(i,j):
                    check_all=True
                    for dx,dy in [(i,j),(i,j+1),(i+1,j),(i+1,j+1)]:
                        if (dx,dy) not in lst:
                            lst.append((dx,dy))
        # 2x2 제거
        for x,y in lst:
            # print(x,y)
            board[x][y]=0
            while x>0:
                board[x][y], board[x-1][y] = board[x-1][y], board[x][y]
                x-=1
            answer+=1

        if not check_all:
            break
    
        # print(board)
        
    return answer