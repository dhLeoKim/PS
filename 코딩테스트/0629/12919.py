import sys
sys.stdin = open('input_12919.txt')
input = sys.stdin.readline

def dfs(lst):
    global ret

    if len(lst) == L:
        if lst == S:
            ret = 1
            print(ret)
            exit()
        return

    if lst[-1] == 'A':
        dfs(lst[:-1])
    if lst[0] == 'B':
        dfs(lst[:0:-1])


S = list(input().strip())
T = list(input().strip())

L = len(S)
ret = 0
dfs(T)

print(ret)

# S에서 추가해가면서 T를 비교하면 시간초과!
# T에서 빼가면서 S로 비교!