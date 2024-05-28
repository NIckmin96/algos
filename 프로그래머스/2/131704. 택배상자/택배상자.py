def solution(order):
    # import time
    from collections import deque
    # start = time.time()
    n = len(order)
    order = deque(order)
    first = order.popleft()
    main = deque(range(first+1,n+1))
    secondary = list(range(1,first))
    answer=1
    
    # for i in order:
    #     if i in main:
    #         while main:
    #             box = main.popleft()
    #             if i==box:
    #                 answer+=1
    #                 break
    #             else:
    #                 secondary.append(box)
    #     elif secondary and secondary[-1]==i:
    #         secondary.pop()
    #         answer+=1
    #     else:
    #         break
            
    for i in order:
        if secondary and i==secondary[-1]:
            secondary.pop()
            answer+=1
        elif not secondary or i>secondary[-1]: # main
            while True:
                box = main.popleft()
                if i==box:
                    answer+=1
                    break
                else:
                    secondary.append(box)
        else: # secondary
            break
            
    # print(time.time()-start)
            
    return answer