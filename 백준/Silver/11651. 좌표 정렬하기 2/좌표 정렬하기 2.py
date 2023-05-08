# 좌표 정렬하기 2
import sys
input = sys.stdin.readline
k = int(input())
lst = []
for _ in range(k):
    lst.append(list(map(int, input().split())))
    
lst.sort(key = lambda x:(x[1], x[0])) # 정렬 기준 여러개 설정방법

for x,y in lst:
    print(x,y)