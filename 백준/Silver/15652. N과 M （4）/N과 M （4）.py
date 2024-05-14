# N과 M(4)
n,m = map(int, input().split())
answer = []
def dp(_min,lst=[]):
    if len(lst)==m:
        answer.append(lst)
        return 
    else:
        for i in range(_min,n+1):
            dp(i,lst+[str(i)])

for i in range(1,n+1):
    dp(i,[str(i)])

for i in answer:
    print((' ').join(i))