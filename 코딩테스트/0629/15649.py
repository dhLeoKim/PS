import sys
sys.stdin = open('input_15649.txt')
input = sys.stdin.readline

def dfs(k):
    if k == M:
        print(*lst)
        return

    for i in range(1, N+1):
        if i not in lst:
            lst.append(i)
            dfs(k+1)
            lst.pop()


N, M = map(int, input().split())

lst = []
dfs(0)