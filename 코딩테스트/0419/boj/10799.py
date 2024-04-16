import sys
sys.stdin = open('input_10799.txt')
input = sys.stdin.readline

lst = list(input().strip())
stack = []
temp = ')'
ret = 0
for char in lst:
    if char == ')':
        if temp == '(':
            stack.pop()
            ret += len(stack)
        elif temp == ')':
            stack.pop()
            ret += 1
    elif char == '(':
        stack.append(char)
    
    temp = char

print(ret)