# 숨바꼭질 (풀이 봄)
import sys
from collections import deque
input = sys.stdin.readline
n,k = map(int, input().strip().split())
max = 10**5
q = deque()
q.append(n)
dist = [0]*(max+1) # 거리 초기화
while q:
    x = q.popleft()
    if x==k:
        print(dist[x])
        break
    for nx in [x-1, x+1, 2*x]:
        if 0<=nx<=max and not dist[nx]:
            dist[nx] = dist[x]+1
            q.append(nx)