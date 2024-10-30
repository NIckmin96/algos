def dijkstra(n, road):
    import heapq
    inf = 1e9
    distance = [[inf]*(n+1) for _ in range(n+1)]
    # 전체 distance map 초기화
    for r in road: # O(2000)
        a,b,d = r
        distance[a][b]=min(d, distance[a][b])
        distance[b][a]=min(d, distance[b][a])
    for i in range(1,n+1): # O(50)
        distance[i][i]=0
    # min heap
    heap = list(zip(distance[1][2:], range(2,n+1))); heapq.heapify(heap)
    # visited
    visited = [False]*(n+1)
    # update
    while sum(visited)<(n-1):
        dist,node = heapq.heappop(heap)
        if not visited[node]:
            visited[node] = True
            for i in range(2,n+1):
                distance[1][i] = min(distance[1][i], distance[1][node]+distance[node][i])
        else:
            continue
        heap = list(zip(distance[1][2:], range(2,n+1))); heapq.heapify(heap)
        # print(heap)
            
    return distance[1]
            
        

def solution(N, road, K):
    answer = 0
    distance = dijkstra(N, road)
    # print(distance)
    answer = len([i for i in distance if i<=K])

    return answer