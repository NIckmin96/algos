# 절댓값 힙
import sys, heapq
input = sys.stdin.readline
n = int(input().strip())
heap = []
for _ in range(n):
    num = int(input().strip())
    if num:
        heapq.heappush(heap, (abs(num),num))
    else:
        if heap:
            res = heapq.heappop(heap)
            print(res[-1])
        else:
            print(0)