# DSLR
import sys
from collections import deque
input = sys.stdin.readline

def D(n):
    return n*2 if n*2<10000 else (n*2)%10000

def S(n):
    return n-1 if n-1>=0 else 9999

def L(n):
    n = str(n).zfill(4)
    return int(n[1:]+n[0])

def R(n):
    n = str(n).zfill(4)
    return int(n[-1]+n[:-1])
        
def bfs(n,target):
    q = deque([(n,'')])
    while q: 
        n,answer = q.popleft()
        for func in funcs:
            # res = globals()[f'{func}'](n)
            if func=='D':
                res = n*2 if n*2<10000 else (n*2)%10000
            elif func=='S':
                res = n-1 if n-1>=0 else 9999
            elif func=='L':
                n = str(n).zfill(4)
                res = int(n[1:]+n[0])
            else:
                n = str(n).zfill(4)
                res = int(n[-1]+n[:-1])
                
            if res==target:
                return answer+func
            else:
                if not visited[res]:
                    visited[res]=True
                    q.append((res,answer+func))
                       
funcs = ['D','S','L','R']
t = int(input().strip())
for _ in range(t):
    visited = [False]*10000
    a,b = map(int, input().strip().split())
    answer = bfs(a,b)
    print(answer)