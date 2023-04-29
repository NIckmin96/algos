# 나무 자르기
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
trees = list(map(int, input().split()))
## 이진 탐색
#################### SOLUTION ####################
start,end = 1,max(trees)
while start<=end:
    mid = (start+end)//2
    res = [tree-mid if tree>=mid else 0 for tree in trees]
    if sum(res) >= m:
        start = mid+1
    else:
        end = mid-1
print(end)
    

#################### FAIL ####################
# start,end = min(trees),max(trees)
# mid = (start+end)//2
# res = [tree-mid if tree>=mid else 0 for tree in trees]
# h = mid

# while sum(res) != m:
#     if sum(res) > m: # 잘랐을 때, 목표값보다 큰 경우
#         start = mid+1
#         # 값을 하나 올려서 잘랐을 때, 목표값보다 작아거나 같아지는 경우 -> 하나 올린 값이 최대값
#         if sum([tree-start if tree>=start else 0 for tree in trees]) <= m:
#             h = start
#             break
#     elif sum(res) < m: # 잘랐을 때, 목표값보다 작은 경우
#         end = mid-1
#         # 값을 하나 내려서 잘랐을 때, 목표값보다 크거나 같아지는 경우 -> 하나 내린 값이 최대값
#         if sum([tree-end if tree>=end else 0 for tree in trees]) >= m:
#             h = end
#             break
#     mid = (start+end)//2
#     res = [tree-mid if tree>=mid else 0 for tree in trees]
#     h = mid
# print(h)

