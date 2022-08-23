import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(T):
    lst = list(input().split())

    # 숫자와 연산자 수를 세서 가능한 연산식인지 판단
    cnt = 0
    for i in lst:
        if cnt < 0: break
        if i.isdigit(): cnt += 1
        elif i == '.': break
        else: cnt -= 1

		# 불가능하다면 error 처리
    if cnt != 1:
        print(f'#{case+1} error')
        continue

    stack = []
    for i in lst:
        if i.isdigit():
            stack.append(i)
        else:
            if i == '+':
                B = int(stack.pop())
                A = int(stack.pop())
                stack.append(str(A+B))
            elif i == '-':
                B = int(stack.pop())
                A = int(stack.pop())
                stack.append(str(A-B))
            elif i == '*':
                B = int(stack.pop())
                A = int(stack.pop())
                stack.append(str(A*B))
            elif i == '/':
                B = int(stack.pop())
                A = int(stack.pop())
                stack.append(str(int(A/B)))
                # stack.append(str(A//B))       # // 연산도 가능
            elif i == '.':
                print(f'#{case+1} {int(*stack)}')
                break