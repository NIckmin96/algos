def solution(sequence, k):
    l,r = 0,0
    s = 0
    answer = []
    for i in range(len(sequence)):
        s+=sequence[i]
        if s==k:
            answer.append([l,r])
            s-=sequence[l]
            l+=1
        elif s>k:
            while s>k:
                s-=sequence[l]
                l+=1
                if s==k:
                    answer.append([l,r])
        r+=1
        
    return sorted(answer,key=lambda x:(x[1]-x[0],x[0]))[0]
            
            
        
    
    # 시간 초과
    # len_seq = 1
    # while len_seq<=len(sequence):
    #     for i in range(len(sequence)):
    #         if sum(sequence[i:i+len_seq])==k:
    #             return [i,i+len_seq-1]
    #     len_seq+=1
    
    