def solution(sticker):
    answer = 0
    # 완전탐색-재귀 함수(시간 초과 의심됨)
    available = [True]*len(sticker)
    
    def func(idx, available, _sum=0, tmp=[]):
        nonlocal answer
        # 사용 처리
        for i in range(-1,2):
            new_idx = idx+i if idx+i<len(sticker) else idx+i-len(sticker)
            available[new_idx]=False
        
        if sum(available)==0:
            print(tmp, _sum)
            answer = max(answer, _sum)
            return 
        
        for i,v in enumerate(available):
            if v:
                func(i,available,_sum+sticker[idx], tmp+[sticker[idx]])
                
        for i in range(-1,2):
            new_idx = idx+i if idx+i<len(sticker) else idx+i-len(sticker)
            available[new_idx]=True
                
    # main
    for i in range(len(sticker)):
        func(i, available)
        
    return answer