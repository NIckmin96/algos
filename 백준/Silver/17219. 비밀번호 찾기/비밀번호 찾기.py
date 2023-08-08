# 비밀번호 찾기
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
dic = {}
for _ in range(n):
    a,b = input().split()
    dic[a] = b

for _ in range(m):
    k = input().strip()
    print(dic[k])