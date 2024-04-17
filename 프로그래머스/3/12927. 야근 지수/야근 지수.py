def solution(n, works):
    answer = 0
    import heapq
    heap = []
    # 최대힙
    for work in works:
        heapq.heappush(heap, -work)
    while n:
        work = heapq.heappop(heap)
        if work<0:
            heapq.heappush(heap, work+1)
        else:
            heapq.heappush(heap,work)
        n-=1
        
    for work in heap:
        answer+=(work**2)
    return answer