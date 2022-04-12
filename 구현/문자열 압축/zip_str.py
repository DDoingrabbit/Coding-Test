def solution(a):
    ans = len(a)
    for i in range(1, len(a)//2+1):
        com = ''
        count =1
        first = a[0:i]
        for j in range(1,len(a)//i):
            if first == a[j*i:(j+1)*i]:
                count +=1
            else:
                com += (str(count) + first) if count >=2 else first
                first = a[j*i:(j+1)*i]
                count = 1
        com += (str(count) + first) if count >=2 else first
        if len(a)%i ==0:
            com = com
        else:
            com += a[-(len(a)%i):]
        ans = min(ans, len(com))

    return ans