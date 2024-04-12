def solution(operations):
    answer = []
    import heapq
    # min_heap = []
    # max_heap = []
    lst = []
    for op in operations:
        a,b = op.split()
        if a=='I':
            lst.append(int(b))
        #     heapq.heappush((-int(b),int(b)), max_heap)
        #     heapq.heappush((int(b),int(b)), min_heap)
        else:
            if lst:
                if b=='1':
                    lst = sorted(lst, key=lambda x:-x)[1:]
                    # heapq.heappop(max_heap)
                else:
                    lst = sorted(lst)[1:]
        # print(lst)
                    
    if lst:
        answer.append(max(lst))
        answer.append(min(lst))
    else:
        answer = [0,0]
        
    return answer