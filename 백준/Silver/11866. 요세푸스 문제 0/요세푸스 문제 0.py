# 요세푸스 문제 0
from collections import deque
n,k = map(int,input().split())
q = deque(range(1,n+1))

cnt = 1
print("<",end='')
while q:
    if (cnt%k==0) and (len(q)==1):
        print(q.popleft(), end='')
    elif cnt%k==0:
        print(q.popleft(), end=", ")
    else:
        q.append(q.popleft())
    cnt+=1
print(">")