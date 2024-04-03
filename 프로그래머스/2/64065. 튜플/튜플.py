def solution(s):
    answer = []
    s = s.replace('{{','{')
    s = s.replace('}}','}')
    lst = []
    tmp = []
    num = ''
    # print(s)
    for i in s:
        if i=='{':
            tmp = []
        elif i=='}':
            tmp.append(int(num))
            num=''
            lst.append(tmp)
        elif i==',':
            if num=='':
                continue
            else:
                tmp.append(int(num))
                num=''
        elif i.isdigit():
            num+=i
    
    # print(lst)
    for i,v in enumerate(sorted(lst, key=lambda x:len(x))):
        if i==0:
            answer.append(v[0])
        else:
            tmp = list(set(v)-set(answer))
            if tmp:
                answer.append(tmp[0])
            else:
                break
        
    return answer