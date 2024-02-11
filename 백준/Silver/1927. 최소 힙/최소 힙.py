# 최소 힙
import sys, heapq
input = sys.stdin.readline
n = int(input().strip())
heap = []
for _ in range(n):
    x = int(input().strip())
    if (0<x) and (type(x)==int):
        heapq.heappush(heap, x)
    elif (x==0) and heap:
        print(heapq.heappop(heap))
    elif (x==0) and not heap:
        print(0)