#스타트와 링크
from operator import index
import sys


N = int(input())
soccer = []
sums = []
answer = []
index_list = []

for i in range(N):
    soccer.append(list(map(int, sys.stdin.readline().rstrip().split())))



def dfs(depth, x):
    if depth == N // 2:
        sum = 0
        for i in index_list:
            for j in index_list:
                if i < j:
                    sum += soccer[i-1][j-1] + soccer[j-1][i-1]
        sums.append(sum)
        return

    
    for i in range(x, N+1):
        if i not in index_list:
            index_list.append(i)
            dfs(depth+1, i)
            index_list.pop()



dfs(0, 1)
for i in range(len(sums) // 2):
    answer.append(abs(sums[i] - sums[len(sums) - i -1]))
    
print(min(answer))








# N = int(input())
# soccer = []
# sums = []
# answer = []
# index_list = []
# for i in range(N):
#     soccer.append(list(map(int,sys.stdin.readline().rstrip().split())))

# def dfs(idx,x):
#     if idx == N//2:
#         sum1 = 0
        
#         print(index_list)
#         for x in index_list:
#             for y in index_list:
#                 if(x < y):
#                     sum1 = sum1 + soccer[x-1][y-1] +soccer[y-1][x-1]
#                     print("S"+str(x)+str(y)+"S"+str(y)+str(x)+" = "+str(soccer[x-1][y-1] +soccer[y-1][x-1]))
#         print(sum1)
#         sums.append(sum1)
#         print("----------------")
#         return
    
#     for i in range(x,N+1):
#         if i not in index_list:
#             index_list.append(i)
#             dfs(idx+1,i)
#             index_list.pop()
        


# dfs(0,1)
# print(sums)

# for i in range(len(sums)//2):
#     answer.append(abs((sums[i]-sums[len(sums)-1-i])))

# print(answer)
# print(min(answer))