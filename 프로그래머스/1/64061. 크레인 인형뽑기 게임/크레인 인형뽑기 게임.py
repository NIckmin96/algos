def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
    for move in moves:
        for i in range(n):
            doll = board[i][move-1]
            if doll:
                if basket:
                    if basket[-1]==doll:
                        basket.pop()
                        answer+=2
                    else:
                        basket.append(doll)
                else:
                    basket.append(doll)
                board[i][move-1]=0
                break
                
    return answer