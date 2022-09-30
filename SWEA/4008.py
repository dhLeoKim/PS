import sys
sys.stdin = open('sample_input.txt')

def calc(res):
    ret = lst[0]
    for i in range(N-1):
        if res[i] == '+':
            ret += lst[i+1]
        elif res[i] == '-':
            ret -= lst[i+1]
        elif res[i] == '*':
            ret *= lst[i+1]
        elif res[i] == '/':
            ret = int(ret/lst[i+1])
    return ret

def dfs(k):
    global max_v, min_v, cnt
    if k == N-1:
        cnt += 1
        temp = calc(res)
        if temp > max_v: max_v = temp
        if temp < min_v: min_v = temp
        return

    for idx in range(4):
        if oper[idx]:
            oper[idx] -= 1
            res.append(oper_lst[idx])
            dfs(k+1)
            res.pop()
            oper[idx] += 1

T = int(input())
for case in range(1, T+1):
    N = int(input())
    oper = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    oper_lst = ['+', '-', '*', '/']

    res = []
    cnt = 0
    max_v = -1e9
    min_v = 1e9

    dfs(0)

    print(f'#{case}', max_v - min_v)