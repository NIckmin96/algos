def solution(people, limit):
    people.sort()
    answer = 0
    light_idx, heavy_idx = 0,len(people)-1
    while light_idx<heavy_idx:
        if people[light_idx]+people[heavy_idx]<=limit:
            light_idx+=1
            answer+=1
        heavy_idx-=1
        
    return len(people)-answer