# 덩치
import sys
input = sys.stdin.readline
n = int(input().strip())
lst = [tuple(map(int,input().split())) for _ in range(n)]

for x,y in lst:
    cnt = 0
    for a,b in lst:
        if ((a>x) and (b>y)):
            cnt+=1
        # if ((a>x) and (b>y)) or ((a>x) and (y==b)) or ((a==x) and (b>y)):
        #     cnt+=1
        else:
            continue
    print(cnt+1, end=' ')