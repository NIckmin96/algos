# 집합

import sys
input = sys.stdin.readline

m = int(input().strip())
S = set()

def add(x):
    global S
    S = S|set([x])

def remove(x):
    global S
    S -= set([x])

def check(x):
    global S
    if x in S:
        return 1
    else:
        return 0

def toggle(x):
    global S
    if x in S:
        S-=set([x])
    else:
        S = S | set([x])

def all():
    global S
    S = set(list(range(1,21)))

def empty():
    global S
    S = set()
    
for _ in range(m):
    tmp = input().strip()
    if ' ' in tmp:
        func, x = tmp.split()
    else:
        func = tmp
    if func == "add":
        add(int(x))
    elif func == "remove":
        remove(int(x))
    elif func == "check":
        print(check(int(x)))
    elif func == "toggle":
        toggle(int(x))
    elif func == "all":
        all()
    elif func == "empty":
        empty()