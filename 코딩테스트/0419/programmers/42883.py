def solution(number, k):
    stack = []

    for num in number:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

number = "4177252841"
k = 4
print(solution(number, k))