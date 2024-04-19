from itertools import combinations
n,m = map(int, input().split())
combs = sorted(list(combinations(list(range(1,n+1)),m)))
for comb in combs:
    for i in comb:
        print(i,end=' ')
    print('')