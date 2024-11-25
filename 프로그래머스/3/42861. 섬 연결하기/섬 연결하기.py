# prim
def solution(n,costs):
    answer = 0
    import heapq
    # 연결 정보 초기화
    connect_dic = dict()
    for a,b,c in costs:
        tmp = {b:c}
        if a in connect_dic.keys():
            connect_dic[a].update(tmp)
        else:
            connect_dic[a] = tmp
        tmp = {a:c}
        if b in connect_dic.keys():
            connect_dic[b].update(tmp)
        else:
            connect_dic[b] = tmp
    # prim
    visited = [False]*n
    h = [(0,0)]
    while h:
        if all(visited):
            break
        c,v = heapq.heappop(h)
        if visited[v]:
            continue
        # print(v,c,answer)
        visited[v] = True
        answer+=c
        for nv,nc in connect_dic[v].items():
            if not visited[nv]:
                heapq.heappush(h,(nc,nv))
                
    return answer
            

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

def solution2(n, costs):
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