# 제로
import sys
input = sys.stdin.readline

k = int(input())
lst = []
for _ in range(k):
    num = int(input())
    if num==0:
        lst.pop()
    else:
        lst.append(num)
        
print(sum(lst))