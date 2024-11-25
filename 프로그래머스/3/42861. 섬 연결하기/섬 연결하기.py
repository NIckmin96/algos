# kruskal
def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    if parent[a]<=parent[b]:
        parent[b] = a
    else:
        parent[a] = b

def solution(n, costs):
    answer = 0
    # 0. parent(root 노드) 초기화
    parent = {i:i for i in range(n)}
    # 1. cost별로 정렬
    costs = sorted(costs, key=lambda x:x[-1])
    # 2. 순차적으로 탐색하면서, cycle이 생성 안되는 경우에만 추가
    for a,b,c in costs:
        a = find_parent(parent,a)
        b = find_parent(parent,b)
        if a!=b:
            union(parent, a, b)
            answer+=c
    
    return answer