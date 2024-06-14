def solution(numbers):
    answer = set()
    numbers = list(numbers)
    def is_prime(num):
        if num<2:
            return False
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True
    
    # 1. permutations
    from itertools import permutations
    for i in range(1,len(numbers)+1):
        s = set(list(map(lambda x:int(''.join(x)), permutations(numbers,i))))
        for num in s:
            if is_prime(num):
                answer.add(num)
    
        
                            
    return len(answer)