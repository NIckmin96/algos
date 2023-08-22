# 패션왕 신해빈
import sys
from itertools import combinations
input = sys.stdin.readline
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    dic = {}
    for _ in range(n):
        v,k = input().split()
        if k not in dic.keys():
            dic[k] = []
        if v not in dic[k]:
            dic[k].append(v)
    # res=0
    # for k,v in dic.items():
    #     res+=len(v)
    # for i in range(2,len(dic.keys())+1):
    #     for j in combinations(dic.keys(), i):
    #         tmp = 1
    #         for n in j:
    #             tmp *= len(dic[n])
    #         res+=tmp
    res=1
    for k,v in dic.items():
        res*=len(v)+1
    res-=1
    print(res)