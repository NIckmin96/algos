# 최대 힙
import sys, heapq
input = sys.stdin.readline
n = int(input().strip())
heap = []
for _ in range(n):
    num = int(input().strip())
    if num==0:
        if heap:
            _pop = heapq.heappop(heap)
            print(_pop[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, (-num,num))