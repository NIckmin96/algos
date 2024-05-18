def solution(n, arr1, arr2):
    answer = []
    def binary(num):
        res = ''
        while num:
            num,mod = divmod(num,2)
            res += str(mod)
        return res[::-1].zfill(n)
    
    map1 = [list(binary(num)) for num in arr1]
    map2 = [list(binary(num)) for num in arr2]
    answer = map1.copy()
    for i in range(n):
        for j in range(n):
            if map1[i][j]=='1' or map2[i][j]=='1':
                answer[i][j]='#'
            else:
                answer[i][j]=' '
                
    answer = list(map(('').join, answer))
        
    return answer