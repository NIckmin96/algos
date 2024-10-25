def solution(book_time):
    from collections import deque
    answer = 0
    book_time = list(map(lambda x:[''.join(x[0].split(':')), ''.join(x[1].split(':'))],book_time))
    book_time.sort()
    book_time = deque(book_time)
    room_dic = dict()
    while book_time:
        book = book_time.popleft()
        _in, _out = book
        len_room = len(room_dic)
        if len_room==0:
            room_dic[len_room] = [book]
        else:
            new_room=True
            for room, booking in room_dic.items():
                if booking:
                    _, before_out = booking[-1]
                    h,m = int(before_out[:2]), int(before_out[2:])
                    if m+10>=60:
                        m-=50; h+=1
                    else:
                        m+=10
                    before_out = ''.join([str(h).zfill(2), str(m).zfill(2)])
                    if int(before_out)<=int(_in):
                        room_dic[room].append(book)
                        new_room=False
                        break
            if new_room:
                room_dic[len_room] = [book]
    
    # print(room_dic)
    answer = len(room_dic)
            
            
    return answer