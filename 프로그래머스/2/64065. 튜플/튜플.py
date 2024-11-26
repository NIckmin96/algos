def solution(s):
    answer = []
    s = s[1:-1]
    lst = s.split('},') # 1e6
    lst = list(map(lambda x:x.lstrip("{").rstrip("}"), lst)) #1e6
    lst = list(map(lambda x:list(map(int, x.split(','))), lst)) #1e6
    lst = sorted(lst, key=lambda x:len(x)) #1e6
    for s in lst: # 1e6
        for x in s: # 1 ~ 1e6
            if x not in answer:
                answer.append(x)
    # print(answer)
    return answer