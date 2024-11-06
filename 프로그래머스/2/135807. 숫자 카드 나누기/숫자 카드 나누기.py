def gcd(a,b):
    g,l = max(a,b), min(a,b)
    if g%l==0:
        return l
    else:
        return gcd(l, g%l)
    
def get_divisor(num):
    lst = set()
    for i in range(1,int(num**0.5)+1):
        if num%i==0:
            lst.add(i)
            lst.add(num//i)
    return list(lst)

def solution(arrayA, arrayB):
    from functools import reduce
    answer = 0
    # gcd
    gcd_a = reduce(lambda x,y:gcd(x,y), arrayA)
    gcd_b = reduce(lambda x,y:gcd(x,y), arrayB)
    codiv_a = get_divisor(gcd_a)
    codiv_b = get_divisor(gcd_b)
    # condition 1 : a의 공약수중에서, B를 전부 나눌 수 없는 수
    for num in codiv_a:
        # print(num)
        res = sum(map(lambda x:1 if x%num==0 else 0, arrayB))
        if res==0:
            answer = max(answer,num)
        # print(answer)
    # condition 2 : b의 공약수중에서, A를 전부 나눌 수 없는 수
    for num in codiv_b:
        # print(num)
        res = sum(map(lambda x:1 if x%num==0 else 0, arrayA))
        if res==0:
            answer = max(answer,num)
        # print(answer)
    return answer