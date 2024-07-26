import sys
sys.stdin = open('input_16637.txt')
input = sys.stdin.readline

def calc(lst):
    stack = [lst[0]]
    for i in range(1, len(lst)):
        if i%2 == 0:
            operator = stack.pop()
            a = int(stack.pop())
            b = int(lst[i])

            if operator == '+':
                temp = a+b
            elif operator == '*':
                temp = a*b
            elif operator == '-':
                temp = a-b

            stack.append(str(temp))

        else:
            stack.append(lst[i])
    
    return int(stack[0])


def calcBlank(blank):
    temp_lst = []
    for j in range(0, len(blank), 2):
        temp_val = calc(lst[blank[j]:blank[j+1]+1])
        temp_lst.append(temp_val)

    new_lst = []
    i = 0
    j = 0
    while i < N:
        if blank[j] <= i < blank[j+1]:
            new_lst.append(temp_lst[j//2])
            i = blank[j+1]
            if j+2 < len(blank):
                j += 2
        else:
            new_lst.append(lst[i])

        i += 1

    return new_lst


def dfs(idx, cnt, blank):
    global ret

    if idx > N-1:
        new_lst = calcBlank(blank)

        temp = calc(new_lst)

        if temp > ret:
            ret = temp
        return

    for i in range(idx, N, 2):
        if cnt < M and i not in blank:
            blank.append(i)
            blank.append(i+2)
            dfs(i+2, cnt+1, blank)
            blank.pop()
            blank.pop()
        else:
            dfs(idx+2, cnt, blank)


N = int(input())
lst = list(input().strip())

if N == 1:
    print(lst[0])
else:
    M = N//4 + N%4//3

    ret = -(2**31)
    dfs(0, 0, [])

    print(ret)


# 문제조건을 잘못이해해서 구현이 꼬엿음 -> 괄호안에 연산자는 최대 한개만 포함 가능하다 조건