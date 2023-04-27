# 좌표 정렬하기
import sys
input = sys.stdin.readline
n = int(input())
lst = [tuple(map(int,input().split())) for _ in range(n)]
lst.sort()
for i,j in lst:
    print(i,j)