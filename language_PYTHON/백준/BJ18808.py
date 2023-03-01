# 스티커 붙이기
# 복습 횟수:1, 00:30:00, 복습필요O
import sys
si = sys.stdin.readline
N, M , K = map(int, si().split())
graph = [[0 for _ in range(M)] for _ in range(N)]

def canAttach(sticker):
    n = len(sticker)
    m = len(sticker[0])

    for x in range(n):
        for y in range(m):
            if sticker[x][y] == 1 and graph[i+x][j+y] == 1:
                return False
    return True

def attach(sticker):
    n = len(sticker)
    m = len(sticker[0])

    for x in range(n):
        for y in range(m):
            if graph[i + x][j + y] == 0: # 스티커가 붙지 않은 경우에만 
                graph[i + x][j + y] = sticker[x][y]

def rotate90(sticker):
    n = len(sticker)
    m = len(sticker[0])
    new_sticker = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new_sticker[j][n-1-i] = sticker[i][j]

    return new_sticker


for i in range(K):
    n, m = map(int, si().split())
    sticker = [list(map(int, si().split())) for _ in range(n)]

    cnt = 0
    isTrue = False
    while cnt < 4:
        if isTrue:
            break

        for i in range(N - len(sticker) + 1):
            if isTrue:
                break
            for j in range(M - len(sticker[0]) + 1):
                if canAttach(sticker):
                    attach(sticker)
                    isTrue = True
                
                if isTrue:
                    break
        
        sticker = rotate90(sticker)
        cnt += 1


answer = 0 
for i in range(N):
    for j in range(M):
        answer += graph[i][j]
print(answer)