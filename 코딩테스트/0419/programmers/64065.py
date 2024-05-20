def solution(s):

    lst = []
    string = s[2:len(s)-2]
    for subset in string.split('},{'):
        lst.append(list(map(int, subset.split(','))))

    lst.sort(key=lambda x:len(x))

    chk = [0]*(100001)
    t = []
    for subset in lst:
        for num in subset:
            if chk[num] == 0:
                chk[num] += 1
                t.append(num)
    
    return t