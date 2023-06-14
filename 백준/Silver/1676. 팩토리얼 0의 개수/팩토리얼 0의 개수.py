# 팩토리얼 0의 개수

n = int(input())

# memoization
lst = [0]*501
# Factorial
def factorial(n):
    if lst[n-1] != 0 : 
        return n*lst[n-1]
    else : 
        if n == 1: 
            lst[n] = 1
            return lst[n]
        elif n > 1:
            lst[n] = n*factorial(n-1)
            return lst[n]

# factorial 연산 진행
factorial(n)
num = lst[n]
# 0의 개수 count
def count_0(num) :
    num = str(num)
    cnt = 0 
    if num == '0' : 
        return cnt
    for i in num[::-1]:
        if i!='0':
            break
        else : 
            cnt+=1
    return cnt

print(count_0(num))