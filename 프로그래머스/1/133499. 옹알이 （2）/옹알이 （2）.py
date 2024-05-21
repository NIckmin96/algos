def solution(babbling):
    import re
    answer = 0
    sounds = ['aya','ye','woo','ma']
    for babble in babbling:
        if all(sound*2 not in babble for sound in sounds):
            if re.sub('|'.join(sounds), '', babble)=='':
                answer+=1
        
    return answer