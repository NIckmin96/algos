def solution(scoville, K):
    answer = 0
    import heapq
    heapq.heapify(scoville)
    while scoville and scoville[0]<K:
        if len(scoville)<2:
            answer=-1
            break
        answer+=1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+2*b)
    return answer