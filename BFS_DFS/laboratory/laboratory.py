import copy
from itertools import combinations
import sys

input = sys.stdin.readline

n,m = map(int, input().split())

data = []
temp = [[0]*m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))
    
dx = [-1,0,1,0]
dy = [0,1,0,-1]

result = 0

def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx <n and ny >=0 and ny <m:
            if temp[nx][ny] == 0:
                temp[nx][ny] =2
                virus(nx, ny)
                
def get_score(temp):
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] ==0:
                score +=1
    return score

com = []
for i in range(n):
    for j in range(m):
        if data[i][j] ==0:
            com.append([i,j])

combin = list(combinations(com, 3))

for i in range(len(combin)):
    temp = copy.deepcopy(data)
    for a,b in combin[i]:
        temp[a][b] = 1
    for c in range(n):
        for d in range(m):
            if temp[c][d]==2:
                virus(c,d)
    result = max(result, get_score(temp))

print(result)