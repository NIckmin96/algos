def solution(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    for i in s:
        if i==' ':
            answer+=' '
            continue
        idx = alphabet.find(i.lower())
        print(idx)
        if i.islower():
            answer+=alphabet[(idx+n)%26]
        else:
            answer+=alphabet[(idx+n)%26].upper()
    return answer