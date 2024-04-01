# 리모컨
import sys, heapq
input = sys.stdin.readline
n = int(input().strip())
m = int(input().strip())
broken = list(map(int, input().strip().split()))
if n==100:
    print(0)
else:
    if m==0: # 고장난 버튼 없는 경우
        if abs(n-100)>len(str(n)): 
            print(len(str(n)))
        else: # +/-누르는게 더 빠를 경우
            print(abs(n-100))
    elif m==10: # 전부 고장난 경우
        print(abs(n-100))
    else:
        lst = []
        for i in range(int(1e6)):
            nums = list(map(int,list(str(i))))
            if set(nums).intersection(set(broken)):
                continue
            else:
                # heapq.heappush(lst,(abs(n-i),i))
                lst.append((abs(n-i),i))
                
        lst.sort(key=lambda x:(x[0],len(str(x[1]))))
        if lst:
            dist, channel = lst[0]
        else:
            dist, channel = abs(n-100), 100
            
        if dist+len(str(channel))<abs(n-100):
            print(dist+len(str(channel)))
        else:
            print(abs(n-100))