def solution(files):
    answer = []
    from collections import deque
    for i,file in enumerate(files):
        head = ''
        number = ''
        tail = ''
        file_name = deque(list(file))
        # head
        while file_name:
            if file_name[0].isdigit():
                break
            else:
                head += file_name.popleft()
        # number
        while file_name:
            if file_name[0].isdigit():
                number+=file_name.popleft()
            else:
                break
        # tail
        tail = ('').join(file_name)
        head = head
        number = number
        tail = tail
        answer.append((head,number,tail,i))
        
    answer.sort(key=lambda x:(x[0].lower(),int(x[1]),i))
    answer = list(map(lambda x:('').join(x[:-1]),answer))
        
    return answer