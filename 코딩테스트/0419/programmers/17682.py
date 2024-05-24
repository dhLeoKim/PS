def solution(dartResult):
    flag = False
    stack = []
    for i in dartResult:
        if i.isdigit():
            if flag:
                stack.append(int(str(stack.pop())+i))
                flag = True
            else:
                stack.append(int(i))
                flag = True
        else:
            if i == 'S':
                stack.append(stack.pop()**1)
            elif i == 'D':
                stack.append(stack.pop()**2)
            elif i == 'T':
                stack.append(stack.pop()**3)
            elif i == '#':
                stack.append(stack.pop()*(-1))
            elif i == '*':
                temp = stack.pop()*2
                if stack:
                    stack.append(stack.pop()*2)
                stack.append(temp)
            flag = False

    return sum(stack)


dartResult = "1S2D*3T"

print(solution(dartResult))