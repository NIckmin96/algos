# hashing
l = int(input())
dic = dict(zip('abcdefghijklmnopqrstuvwxyz', list(range(1,27))))

res = 0
for i,v in enumerate(input().strip()):
    hash = dic[v]
    res += hash*(31**i)
    
res = res%1234567891
print(res)