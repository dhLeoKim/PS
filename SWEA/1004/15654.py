import sys
input = sys.stdin.readline

def backtracking(k):
    if k == M:
        print(*arr)
        return
    
    for i in lst:
        if i not in arr:
            arr.append(i)
            backtracking(k+1)
            arr.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = []
backtracking(0)