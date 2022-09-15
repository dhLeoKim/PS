import sys
sys.stdin = open('input.txt')

def postorder(n):                       # 후위 순회
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        if not tree[n].isdigit():       # 연산자인 경우, 연산 진행
            if tree[n] == '+':
                tree[n] = float(tree[ch1[n]]) + float(tree[ch2[n]])
            elif tree[n] == '-':
                tree[n] = float(tree[ch1[n]]) - float(tree[ch2[n]])
            elif tree[n] == '*':
                tree[n] = float(tree[ch1[n]]) * float(tree[ch2[n]])
            elif tree[n] == '/':
                tree[n] = float(tree[ch1[n]]) / float(tree[ch2[n]])

T = 10
for case in range(1, T+1):
    N = int(input())
    tree = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)

    for i in range(N):                  # tree 저장
        temp = list(input().split())
        tree[i+1] = temp[1]
        if len(temp) > 2:
            ch1[i+1] = int(temp[2])
            ch2[i+1] = int(temp[3])

    postorder(1)

    print(f'#{case} {int(tree[1])}')