def find(booked,num):
    if booked.get(num,0):
        booked[num] = find(booked,booked[num]+1)
    else:    
        booked[num] = num
        
    return booked[num]

def solution(k, room_number):
    import sys
    sys.setrecursionlimit(1000000)
    answer = []
    booked = dict()
    for num in room_number:
        room = find(booked,num)
        answer.append(room)
            
    return answer