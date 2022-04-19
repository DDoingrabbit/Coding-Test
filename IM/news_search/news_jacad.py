import math
def solution(str1, str2):
    str1 = str1.lower()
    str_list1 = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            str_list1.append(str1[i:i+2])
    str2 = str2.lower()
    str_list2 = []
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            str_list2.append(str2[i:i+2])
            
    if len(str_list1) == 0 and len(str_list2)==0:
        return 65536
    else:
        str_dict1 = {}
        for j in str_list1:
            count = str_list1.count(j)
            str_dict1[j] = count
        str_dict2 = {}
        for j in str_list2:
            count = str_list2.count(j)
            str_dict2[j] = count

        str_set1 = set(str_dict1.keys())
        str_set2 = set(str_dict2.keys())
        inter = str_set1 & str_set2
        inter_total = 0
        for k in inter:
            count = min(str_dict1[k], str_dict2[k])
            inter_total += count

        uni = str_set1 | str_set2
        uni_total = 0
        for k in uni:
            if k in str_dict1.keys() and k not in str_dict2.keys():
                uni_total += str_dict1[k]
            elif k not in str_dict1.keys() and k in str_dict2.keys():
                uni_total += str_dict2[k]
            elif k not in str_dict1.keys() and k not in str_dict2.keys():
                continue
            else:
                count = max(str_dict1[k], str_dict2[k])
                uni_total += count
        if uni_total ==0:
            return 65536
        else : 
            answer = math.trunc(inter_total/uni_total*65536)
    return answer