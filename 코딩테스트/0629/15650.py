import sys
sys.stdin = open('input_15650.txt')
input = sys.stdin.readline

def dfs(k):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(k, N+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()


N, M = map(int, input().split())

arr = []
dfs(1)