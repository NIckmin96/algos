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
    
    # # 1. permutations
    # from itertools import permutations
    # for i in range(1,len(numbers)+1):
    #     s = set(list(map(lambda x:int(''.join(x)), permutations(numbers,i))))
    #     for num in s:
    #         if is_prime(num):
    #             answer.add(num)
                
    # 2. 재귀
    def permutation(numbers,k,res=''):
        if len(res)==k:
            if is_prime(int(res)):
                answer.add(int(res))
                return
        for _ in range(len(numbers)):
            num = numbers.pop(0)
            permutation(numbers,k,res+num)
            numbers.append(num)
    
    for i in range(1,len(numbers)+1):
        permutation(numbers,i)
        
                            
    return len(answer)