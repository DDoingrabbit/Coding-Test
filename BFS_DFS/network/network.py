#https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def solution(n, computers):
    graph = [[] for _ in range(n+1)]
    for i in range(len(computers)):
        for j in range(len(computers)):
            if i != j and computers[i][j]==1:
                graph[(i+1)].append(j+1)
    visited = [False]*(n+1)
    count = 0
    for i in range(1, len(visited)):
        if visited[i] == False:
            bfs(graph,i,visited)
            count +=1
        elif visited[i] == True:
            continue
    return count