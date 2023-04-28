def solution(name, yearning, photo):
    answer = []
    score = dict(zip(name,yearning))

    for p in photo:
        res = 0
        for person in p:
            if person in score.keys():
                res += score[person]
        answer.append(res)
    
    return answer