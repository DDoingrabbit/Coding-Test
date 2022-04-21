# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import defaultdict
def solution(tickets):
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])

    for key in routes.keys():
        routes[key].sort(reverse=True)
    
    answer = []
    visit = []
    visit.append('ICN')
    while visit:
        tmp = visit[-1]
        if not routes[tmp]:
            answer.append(visit.pop())
        else:
            visit.append(routes[tmp].pop())
    answer.reverse()
    return answer