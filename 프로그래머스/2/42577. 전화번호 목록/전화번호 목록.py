def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        a = phone_book[i]
        b = phone_book[i+1]
        if b[:len(a)]==a:
            answer=False
            break
    return answer