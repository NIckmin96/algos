# 스택
import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    inputs = input().split()
    if len(inputs)>1:
        cmd, num = inputs
    else:
        cmd = inputs[0]
        
    if cmd == 'push':
        stack.append(num)
    elif cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)