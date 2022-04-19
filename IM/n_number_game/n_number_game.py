def number(n,num):
    numbers = '0123456789ABCDEF'
    r = ''
    if num == 0:
        return '0'
    while num>0:
        r = numbers[num%n]+r
        num = num // n
    return r 

def solution(n, t, m, p):
    answer = ''
    for i in range(t*m):
        answer += number(n, i)
                
    new_answer = ''
    for j in range(p-1,t*m, m):
        new_answer += answer[j]

    return new_answer