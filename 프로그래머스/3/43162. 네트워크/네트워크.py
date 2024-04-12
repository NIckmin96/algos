def solution(n, computers):
    answer = 0
    # dfs
    for i in range(n):
        stack = []
        for j in range(n):
            if computers[i][j]==1:
                stack.append((i,j))
                computers[i][j]=-1
                computers[j][i]=-1
                while stack:
                    x,y = stack.pop()
                    for k in range(n):
                        if computers[y][k]==1:
                            stack.append((y,k))
                            computers[y][k]=-1
                            computers[k][y]=-1
                answer+=1
    return answer