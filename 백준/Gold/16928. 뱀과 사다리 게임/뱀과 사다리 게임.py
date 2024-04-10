# 뱀과 사다리 게임
import sys
from collections import deque
input = sys.stdin.readline
board = [[j+i*10 for j in range(1,11)] for i in range(10)]
distance = [[0]*10 for _ in range(10)]
n,m = map(int, input().strip().split())
ladder, snake = dict(), dict()
for _ in range(n):
    a,b = map(int, input().strip().split())
    ladder[a] = b
for _ in range(m):
    a,b = map(int, input().strip().split())
    snake[a] = b
# bfs
start = (0,0)
q = deque()
q.append(start)
dist=1
distance[0][0]=-1
def bfs():
    new_q = deque()
    num_q = deque()
    while q:
        x,y = q.popleft()
        # snake, ladder의 시작점인 경우 -> 1~6까지의 경우 고려할 수 없음
        # if board[x][y] in snake.keys():
        #     r = (snake[board[x][y]]-1)//10
        #     c = snake[board[x][y]]%10-1
        #     if distance[r][c]==0:
        #         distance[r][c]=dist
        #         new_q.append((r,c))
        #     continue
        # elif board[x][y] in ladder.keys():
        #     r = (ladder[board[x][y]]-1)//10
        #     c = ladder[board[x][y]]%10-1
        #     if distance[r][c]==0:
        #         distance[r][c]=dist
        #         new_q.append((r,c))
        #     continue
        
        for i in range(7):
            if (y+i)<=9:
                if distance[x][y+i]==0:
                    distance[x][y+i]=dist
                    if board[x][y+i] in ladder.keys():
                        r = (ladder[board[x][y+i]]-1)//10
                        c = (ladder[board[x][y+i]]-1)%10
                        if distance[r][c]==0:
                            distance[r][c]=dist
                            new_q.append((r,c))
                            num_q.append(board[r][c])
                    elif board[x][y+i] in snake.keys():
                        r = (snake[board[x][y+i]]-1)//10
                        c = (snake[board[x][y+i]]-1)%10
                        if distance[r][c]==0:
                            distance[r][c]=dist
                            new_q.append((r,c))
                            num_q.append(board[r][c])
                    else:
                        new_q.append((x,y+i))
                        num_q.append(board[x][y+i])

            else:
                if x<9:
                    new_x = x+1
                    new_y = y+i-10
                else:
                    if y+i>9:
                        break
                if distance[new_x][new_y]==0:
                    distance[new_x][new_y]=dist
                    if board[new_x][new_y] in ladder.keys():
                        r = (ladder[board[new_x][new_y]]-1)//10
                        c = (ladder[board[new_x][new_y]]-1)%10
                        if distance[r][c]==0:
                            distance[r][c]=dist
                            new_q.append((r,c))
                            num_q.append(board[r][c])
                    elif board[new_x][new_y] in snake.keys():
                        r = (snake[board[new_x][new_y]]-1)//10
                        c = (snake[board[new_x][new_y]]-1)%10
                        if distance[r][c]==0:
                            distance[r][c]=dist
                            new_q.append((r,c))
                            num_q.append(board[r][c])
                    else:
                        new_q.append((new_x,new_y))
                        num_q.append(board[new_x][new_y])

    # # print(new_q)
    # print(num_q)
    return new_q
while q:
    q = bfs()
    dist+=1
# print(distance)
print(distance[9][9])    