import sys
sys.stdin = open('input_15655.txt')
input = sys.stdin.readline

def dfs(k, s):
    if k == M:
        print(*arr)
        return

    for i in range(s, N):
        if lst[i] not in arr:
            arr.append(lst[i])
            dfs(k+1, i)
            arr.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = []
dfs(0, 0)