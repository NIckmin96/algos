# 케빈 베이컨의 6단계 법칙
import sys, copy
input = sys.stdin.readline
n,m = map(int, input().strip().split())
# 최단거리 그래프
graph = [[1e9]*n for _ in range(n)]
for i in range(n):
    graph[i][i]=0
for _ in range(m):
    i,j = map(int, input().strip().split())
    graph[i-1][j-1]=1
    graph[j-1][i-1]=1
# print(graph)
# 플로이드 워셜 알고리즘
# 중간에 거치는 노드를 하나씩 순회하면서, 최단거리 업데이트
# 한번이상 거치는 경우를 고려하기 위해, while문으로 변화가 없을때까지 반복
graph_new = copy.deepcopy(graph)
while True:
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])
    if graph_new == graph:
        break
    else:
        graph_new=copy.deepcopy(graph)

_sum = list(map(sum, graph))
for i,v in enumerate(_sum):
    if v==min(_sum):
        print(i+1)
        break