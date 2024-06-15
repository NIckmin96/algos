def solution(bridge_length, weight, truck_weights):
    answer = 0
    from collections import deque
    truck_weights = deque(truck_weights)
    bridge = deque([0]*bridge_length)
    bridge_weight = 0
    while True:
        if not truck_weights and bridge_weight==0:
            break
        answer+=1
        if truck_weights and weight>=bridge_weight-bridge[-1]+truck_weights[0]:
            truck = truck_weights.popleft()
            bridge_weight+=truck
            bridge.appendleft(truck)
            bridge_weight-=bridge.pop()
            
        else:
            bridge.appendleft(0)
            bridge_weight-=bridge.pop()
            
        
    return answer