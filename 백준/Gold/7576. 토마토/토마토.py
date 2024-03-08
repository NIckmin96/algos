# 토마토
import sys
input = sys.stdin.readline
m,n = map(int, input().strip().split())
box = [list(map(int, input().strip().split())) for _ in range(n)]
# 1. 1(익은 토마토)의 위치 찾기
idx = []
for i,row in enumerate(box):
    for j,elem in enumerate(row):
        if elem==1:
            idx.append((i,j))
def func(idx):
    global box
    # 2. 익은 토마토의 인접 index 찾기
    close_idx = []
    new_tomato = []
    for i,j in idx:
        if i==0:
            if j==0:
                if box[i+1][j]==0:
                    box[i+1][j]=1
                    new_tomato.append((i+1,j)) # 아래
                if box[i][j+1]==0:
                    box[i][j+1]=1
                    new_tomato.append((i,j+1)) # 오
            elif j==m-1:
                if box[i+1][j]==0:
                    box[i+1][j]=1
                    new_tomato.append((i+1,j)) # 아래
                if box[i][j-1]==0:
                    box[i][j-1]=1
                    new_tomato.append((i,j-1)) # 왼
            else:
                if box[i][j-1]==0:
                    box[i][j-1]=1
                    new_tomato.append((i,j-1)) # 왼
                if box[i][j+1]==0:
                    box[i][j+1]=1
                    new_tomato.append((i,j+1)) # 오
                if box[i+1][j]==0:
                    box[i+1][j]=1
                    new_tomato.append((i+1,j)) # 아래
        elif i==n-1:
            if j==0:
                if box[i-1][j]==0:
                    box[i-1][j]=1
                    new_tomato.append((i-1,j)) # 위
                if box[i][j+1]==0:
                    box[i][j+1]=1
                    new_tomato.append((i,j+1)) # 오
            elif j==m-1:
                if box[i-1][j]==0:
                    box[i-1][j]=1
                    new_tomato.append((i-1,j)) # 위
                if box[i][j-1]==0:
                    box[i][j-1]=1
                    new_tomato.append((i,j-1)) # 왼
            else:
                if box[i-1][j]==0: # 위
                    box[i-1][j]=1
                    new_tomato.append((i-1,j))
                if box[i][j-1]==0: # 왼
                    box[i][j-1]=1
                    new_tomato.append((i,j-1))
                if box[i][j+1]==0: # 오
                    box[i][j+1]=1
                    new_tomato.append((i,j+1))
        else:
            if j==0: # 왼쪽 1열
                if box[i-1][j]==0:
                    box[i-1][j]=1
                    new_tomato.append((i-1,j)) # 위
                if box[i+1][j]==0:
                    box[i+1][j]=1
                    new_tomato.append((i+1,j)) # 아래
                if box[i][j+1]==0:
                    box[i][j+1]=1
                    new_tomato.append((i,j+1)) # 오
            elif j==m-1: # 오른쪽 1열
                if box[i-1][j]==0:
                    box[i-1][j]=1
                    new_tomato.append((i-1,j)) # 위
                if box[i+1][j]==0:
                    box[i+1][j]=1
                    new_tomato.append((i+1,j)) # 아래
                if box[i][j-1]==0:
                    box[i][j-1]=1
                    new_tomato.append((i,j-1)) # 왼
            else:
                if box[i-1][j]==0:
                    box[i-1][j]=1
                    new_tomato.append((i-1,j))# 위
                if box[i+1][j]==0:
                    box[i+1][j]=1
                    new_tomato.append((i+1,j))# 아래
                if box[i][j-1]==0:
                    box[i][j-1]=1
                    new_tomato.append((i,j-1))# 왼
                if box[i][j+1]==0:
                    box[i][j+1]=1
                    new_tomato.append((i,j+1))# 오
    return box, new_tomato
    
# print(idx)
# print(box)
cnt = 0
while True:
    new_box, idx = func(idx)
    if idx:
        cnt+=1
    else:
        break
    # print(idx)
# print(new_box)
# 다 채워지지 않는 경우
for r in new_box:
    for elem in r:
        if elem==0:
            cnt = -1
            break
        
print(cnt)
    

