# 2×n 타일링 2
import sys
input = sys.stdin.readline
n = int(input().strip())

def combination(a,b):
    top,bottom = 1,1
    for i in range(b):
        top*=(a-i)
        bottom*=(b-i)
    return top//bottom

b=1
res=0
while True:
        a=n-b
        if b>a:
            break
        res+=combination(a,b)*(2**b)
        b+=1
print((res+1)%10007)