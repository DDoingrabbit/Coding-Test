from itertools import combinations
n,m = map(int, input().split())
chicken = []
house = []

count = 0
for _ in range(n):
    k = list(map(int, input().split()))
    for i in range(len(k)):
        if k[i] == 1:
            house.append([count, i])
        elif k[i] == 2:
            chicken.append([count, i])
    count +=1
    
candi = list(combinations(chicken,m))

def get_sum(candidate):
    result = 0
    for k in house:
        temp = 1e9
        for x in candidate:
            temp = min(temp, abs(k[0]-x[0])+abs(k[1]-x[1]))
        result += temp
    return result

result = 1e9
for candidate in candi:
    result = min(result, get_sum(candidate))
    
print(result)