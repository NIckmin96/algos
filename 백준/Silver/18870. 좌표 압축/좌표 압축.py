# 좌표 압축
import sys
input = sys.stdin.readline
n = int(input().strip())
lst = list(map(int, input().strip().split()))
# 시간, 메모리 효율적 알고리즘 필요
sorted_lst = sorted(set(lst))
# 메모이제이션
dic = {}
for i,num in enumerate(sorted_lst):
    dic[num] = i
for num in lst:
    print(dic[num], end=' ')