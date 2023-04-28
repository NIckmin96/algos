# 벌집

n = int(input())

div = []
# 수열 만들기
num = 0
i = 1
while (n > num*6+1):
    div.append(num*6+1)
    num+=i
    i+=1

print(len(div)+1)