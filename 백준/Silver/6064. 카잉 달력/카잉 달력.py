# 카잉 달력
t = int(input())
for _ in range(t):
    m,n,x,y = map(int, input().split())
    # 최대공약수(gcd)
    def find_gcd(a,b):
        dividend=max(a,b)
        divisor=min(a,b)
        res = dividend%divisor
        while res!=0:
            dividend=divisor
            divisor=res
            res = dividend%divisor
        return divisor
    gcd=find_gcd(m,n)
    # 최소공배수(lcm)
    lcm=gcd*int(m/gcd)*int(n/gcd)
    lst_x, lst_y = [],[]
    res=-1
    while x<=lcm:
        if (x-y)%n==0:
            res=x
            break
        else:
            x+=m
    print(res)
    #     lst_x.append(x)
    #     lst_y.append(y)
    #     x+=m
    #     y+=n
    
    # res = list(set(lst_x).intersection(set(lst_y)))
    # if res:
    #     print(sorted(res)[0])
    # else:
    #     print(-1)