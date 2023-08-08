# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n,m = map(int, input().strip().split())
dic_name = {input().strip():i+1 for i in range(n)}
dic_index = {v:k for k,v in dic_name.items()}

for _ in range(m):
    q = input().strip()
    # print(q)
    if q.isdigit():
        q = int(q)
        print(dic_index[q])
    else:
        print(dic_name[q])