# x의 부모 노드가, x일때 까지 재귀 호출 -> 처음 사용된 x의 부모노드 return됨
def find_parent(parent, x):
    if parent[x]!=x: 
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 노드가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a) # a의 root node
    b = find_parent(parent, b) # b의 root node
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
    
def solution(n, costs):
    answer = 0
    # 크루스칼 알고리즘
    parent = [0]*n
    # parent 초기화
    for i in range(n):
        parent[i]=i
    # cost작은 순서대로 오름차순 정렬
    costs = sorted(costs, key=lambda x:x[-1])
    # root노드 비교
    for a,b,c in costs:
        if find_parent(parent,a)!=find_parent(parent,b):
            union_parent(parent,a,b)
            answer+=c
    
    return answer