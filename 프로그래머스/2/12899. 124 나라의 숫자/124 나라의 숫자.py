def solution(n):

    def base_124(num):
        num_dic = dict(zip(range(1,4),['1','2','4']))
        new_num = ''
        while num:
            num, mod = divmod(num, 3)
            if mod==0:
                num-=1
                new_num+=num_dic[3]
            else:
                new_num+=num_dic[mod]
            
            
        return new_num[::-1]
            
    answer = base_124(n)
    
    
    return answer