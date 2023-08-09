# 1로 만들기
import sys
sys.setrecursionlimit(10000000)
n = int(input())
lst = [0]*(10**7)
   
def a(x):
    if x*3>n:
        return 0
    if lst[x*3]==0:
        lst[x*3] = lst[x]+1
    a(x*3)
        
def b(x):
    if x*2>n:
        return 0
    if lst[x*2]==0:
        lst[x*2] = lst[x]+1
    b(x*2)
        
def c(x):
    if x+1>n:
        return 0
    if lst[x+1]==0:
        lst[x+1] = lst[x]+1
    c(x+1)      
# a(1)
# b(1)
# c(1)

# min 함수
for i in range(2,n+1):
    if (i%2==0) and (i%3==0):
        lst[i] = min([lst[i//2], lst[i//3], lst[i-1]])+1
    elif (i%2==0) and (i%3!=0):
        lst[i] = min([lst[i//2], lst[i-1]])+1
    elif (i%3==0) and (i%2!=0):
        lst[i] = min([lst[i//3], lst[i-1]])+1
    else:
        # print(i)
        lst[i] = lst[i-1]+1
        

# print(lst[:n+1])
print(lst[n])