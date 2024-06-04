def solution(board, h, w):
    answer = 0
    height = len(board)
    width = len(board[0])
    color = board[h][w]
    for dh,dw in [(-1,0),(1,0),(0,-1),(0,1)]:
        if 0<=h+dh<height and 0<=w+dw<width and board[h+dh][w+dw]==color:
            answer+=1
    return answer