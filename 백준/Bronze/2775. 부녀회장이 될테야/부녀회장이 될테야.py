# 부녀회장이 될테야

graph = [[0]*14 for _ in range(15)] # 15x14
# 0층 초기화
for i in range(len(graph[0])):
    graph[14][i] = i+1

# 거주인 계산
for i in range(14,0,-1): # floor
    for j in range(14): # room
        graph[i-1][j] = sum(graph[i][:j+1])
        
# print(graph)

t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    print(graph[14-k][n-1])