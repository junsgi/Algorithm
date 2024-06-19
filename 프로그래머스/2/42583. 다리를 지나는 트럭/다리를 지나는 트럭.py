from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    cnt = len(truck_weights)
    wait = deque()
    bridge = deque()
    while truck_weights: wait.appendleft(truck_weights.pop())
    
    while cnt:
        answer += 1
        
        if bridge and answer - bridge[0][0] == bridge_length:
            t, w = bridge.popleft()
            weight += w
            cnt -= 1


        if wait and wait[0] <= weight:
            weight -= wait[0]
            bridge.append((answer, wait.popleft()))
            
    return answer