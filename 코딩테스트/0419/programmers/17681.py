def solution(n, arr1, arr2):
    
    temp = [bin(x|y) for x, y in zip(arr1, arr2)]
    
    result = []
    for i in temp:
        i = i[2:]
        if len(i) < n:
            i = '0'*(n-len(i)) + i
        i = i.replace('1', '#')
        i = i.replace('0', ' ')
        result.append(i)

    return result

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))