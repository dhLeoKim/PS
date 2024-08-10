import sys
sys.stdin = open('input_15655.txt')
input = sys.stdin.readline

def backtracking(k, s):
    if k == M:
        print(*arr)
        return

    for i in range(s, N):
        if lst[i] not in arr:
            arr.append(lst[i])
            backtracking(k+1, i)
            arr.pop()

N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

arr = []
backtracking(0, 0)