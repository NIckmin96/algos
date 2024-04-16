def solution(n, t, m, p):
    answer = ''
    dic = dict(zip(list(range(0,16)), list('0123456789ABCDEF')))
    def convert(num, base_num):
        new_num = ''
        while True:
            num, remainder = num//base_num, num%base_num
            new_num+=dic[remainder]
            if num<base_num:
                if num!=0:
                    new_num+=dic[num]
                break
        return new_num[::-1]
                
    num=0
    cnt=1
    # 나머지 맞추기
    if m==p:
        p=0
    while len(answer)<t:
        # 1. 진수 변환
        new_num = convert(num,n)
        # 2. 진수 한자리씩 끊어서 출력+내가 말하는 차례인지 확인
        for i in new_num:
            if cnt%m==p:
                answer+=i
                if len(answer)==t:
                    break
            cnt+=1
        num+=1
            
    
    return answer