# 덱
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
q = deque()

for _ in range(n):
    inputs = input().split()
    if len(inputs)>1:
        cmd, num = inputs
    else:
        cmd = inputs[0]
        
    if cmd == 'push_front':
        q.appendleft(num)
    elif cmd == 'push_back':
        q.append(num)
    elif cmd == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(q))
    elif cmd == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)