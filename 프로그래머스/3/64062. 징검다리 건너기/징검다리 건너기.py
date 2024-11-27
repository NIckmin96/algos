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
        # print(heap)
        # print(answer)
        # max_table.append(-heap[0][0])
        
    # print(max_table)
            
    return answer
            
    # for i in range(l-k+1):
    #     m = min(m,max(stones[i:i+k]))
    
    # return m
            
        
    