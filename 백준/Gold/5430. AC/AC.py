# AC
import sys
from collections import deque
input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    func = input().strip()
    len_lst = int(input().strip())
    tmp = input().strip().strip('[]')
    if tmp=='':
        lst = []
    else:
        lst = list(map(int,tmp.split(',')))
    rev_lst = deque(lst[::-1])
    lst = deque(lst)
    target = lst
    res=True
    for f in func:
        if f=='R':
            if target==lst:
                target=rev_lst
            else:
                target=lst
        elif f=='D':
            if target:
                if target==lst:
                    lst.popleft()
                    rev_lst.pop()
                    target = lst
                else:
                    rev_lst.popleft()
                    lst.pop()
                    target=rev_lst
                
            else:
                print('error')
                res=False
                break
        # print(lst, rev_lst, target)
    if res:
        print('[', end='')
        for i,v in enumerate(target):
            if i<len(target)-1:
                print(str(v), end='')
                print(',',end='')
            else:
                print(str(v), end='')
        print(']')