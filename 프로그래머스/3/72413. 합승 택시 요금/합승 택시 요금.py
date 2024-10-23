
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
def solution(n, s, a, b, fares):

    INF = 100001*n

    answer = INF

    graph = [[INF] * (n+1) for _ in range(n+1)]

    for start,end,f in fares:
        graph[start][end] = f
        graph[end][start] = f


    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    for x in range(1,n+1):
        graph[x][x] = 0

    #print(graph)

    for x in range(1,n+1):

        answer = min(graph[s][x]+graph[x][a]+graph[x][b],answer)

    return answer

# def floyd_warshall(n,fares):
#     inf=1e9
#     table = [[inf]*n for _ in range(n)]
#     # 기본 초기화
#     for i in range(n):
#         table[i][i]=0
#     for fare in fares:
#         a,b,f = fare
#         table[a-1][b-1]=f
#         table[b-1][a-1]=f
#     # 업데이트 실행
#     for i in range(n):
#         for j in range(n):
#             for m in range(n):
#                 if m in [i,j]:
#                     continue
#                 table[i][j]=min(table[i][j], table[i][m]+table[m][j])
#     return table    

# def solution(n, s, a, b, fares):
#     answer = 1e9
#     table = floyd_warshall(n,fares) # floyd_warshall 사용해서 노드간 최단 거리 계산
#     # print(table)
#     for i in range(n):
#         answer = min(answer, table[s-1][i-1]+table[i-1][a-1]+table[i-1][b-1])
    
#     return answer