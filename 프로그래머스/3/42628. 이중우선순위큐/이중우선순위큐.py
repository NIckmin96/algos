def solution(operations):
    answer = []
    import heapq
    min_heap = []
    max_heap = []
    # lst = []
    for op in operations:
        a,b = op.split()
        if a=='I':
            # lst.append(int(b))
            heapq.heappush(max_heap, -int(b))
            heapq.heappush(min_heap, int(b))
        else:
            if (max_heap!=[])&(min_heap!=[]):
                if b=='1':
                    # lst = sorted(lst, key=lambda x:-x)[1:]
                    heapq.heappop(max_heap)
                    min_heap = list(map(lambda x:-x, max_heap))
                    heapq.heapify(min_heap)
                else:
                    # lst = sorted(lst)[1:]
                    heapq.heappop(min_heap)
                    max_heap = list(map(lambda x:-x, min_heap))
                    heapq.heapify(max_heap)
        # print(max_heap, min_heap)
    
    if (min_heap!=[])&(max_heap!=[]):
        answer = [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        answer = [0,0]
                    
    # if lst:
        # answer.append(max(lst))
        # answer.append(min(lst))
    # else:
        # answer = [0,0]
        
    return answer