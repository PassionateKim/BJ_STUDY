import math

def solution(k, d):
    answer = 0

    for x in range(0, d + 1, k):
        
        answer += (math.floor(math.sqrt(d**2 - x**2)) // k) + 1

    return answer

solution(2, 4)