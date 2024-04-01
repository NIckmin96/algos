def solution(arr1, arr2):
    answer = []
    new_arr2 = []
    for i in range(len(arr2[0])):
        tmp = []
        for j in range(len(arr2)):
            tmp.append(arr2[j][i])
        new_arr2.append(tmp)
    
    for row in arr1:
        tmp = []
        for col in new_arr2:
            res = 0
            for i in range(len(col)):
                res+=row[i]*col[i]
            tmp.append(res)
        answer.append(tmp)
    
    return answer