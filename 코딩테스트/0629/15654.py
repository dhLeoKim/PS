import sys
sys.stdin = open('input_15654.txt')
input = sys.stdin.readline

def dfs(k):
    if k == M:
        print(*arr)
        return
    
    for i in lst:
        if i not in arr:
            arr.append(i)
            dfs(k+1)
            arr.pop()


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = []
dfs(0)