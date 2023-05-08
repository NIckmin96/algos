# 수 정렬하기 3 -> 메모리 제한
import sys
input = sys.stdin.readline

n = int(input())
dic = dict(zip(list(range(1,10001)), [0]*10000))

for _ in range(n):
    num = int(input())
    dic[num]+=1
    
for k,v in dic.items():
    for _ in range(v):
        print(k)