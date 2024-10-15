def solution(a, b):
    if a%b==0:
        return 1
    
    def is_prime(num):
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    
    def decomposition(num):
        lst = []
        while num>=2:
            for i in range(2,num+1):
                if is_prime(i) and num%i==0:
                    lst.append(i)
                    num//=i
                    break
                
        return lst
                
    
    answer = 0
    # 1. 기약분수 만들기
    # 1-1. a 소인수분해
    lst_a = decomposition(a)
    lst_b = decomposition(b)
    copy_a = lst_a.copy()
    copy_b = lst_b.copy()
    for elem in lst_a:
        if elem in copy_b:
            copy_b.remove(elem)
    for elem in lst_b:
        if elem in copy_a:
            copy_a.remove(elem)        
    # 2. 분모 소인수분해
    if set(copy_b)=={2} or set(copy_b)=={5} or set(copy_b)=={2,5}:
        return 1
    else:
        return 2
    
    return answer