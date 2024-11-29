def solution(bandage, health, attacks):
    max_health = health
    end = attacks[-1][0]
    attacks = {k:v for k,v in attacks}
    cnt = 0
    for i in range(1,end+1):
        if attacks.get(i):
            health-=attacks[i]
            cnt=0
        else:
            health = min(max_health,health+bandage[1])
            cnt+=1
        if cnt==bandage[0]:
            health = min(max_health,health+bandage[2])
            cnt=0
        # print(health)
        if health<=0:
                return -1
            
    return health