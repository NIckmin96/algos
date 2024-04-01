# 가장 가까운 세 사람의 심리적 거리
import sys
from itertools import combinations
input = sys.stdin.readline
t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    lst = input().strip().split()
    res = []
    # 비둘기집 원리
    if len(lst)>32: # 중복되는 MBTI 3개 이상되는 경우
        print(0)
    else: # 그렇지 않은 경우, Brute Force(모든 경우의 수 구하기) : 최대 32C
        for i in combinations(lst,3):
            a,b,c = i
            diff = 0
            diff+=len(set(list(a))-set(list(b)))
            diff+=len(set(list(b))-set(list(c)))
            diff+=len(set(list(a))-set(list(c)))
            res.append(diff)
        print(min(res))