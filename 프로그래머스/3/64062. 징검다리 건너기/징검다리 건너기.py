def solution(stones, k):
    import heapq
    answer = 1e9
    l = len(stones)
    # max heap
    heap = []
    for i in range(k-1):
        heapq.heappush(heap, (-stones[i],i))
    for i in range(k-1,l):
        heapq.heappush(heap, (-stones[i],i))
        while heap[0][1]<=i-k:
            heapq.heappop(heap)
        answer = min(answer, -heap[0][0])
            
    return answer
            
        
    