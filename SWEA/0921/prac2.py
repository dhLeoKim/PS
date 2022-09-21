import sys
sys.stdin = open('input.txt')

def checkBabygin(k):
    if k == N:
        arr11 = arr1[:3]
        arr12 = arr1[3:]
        res11 = res12 = 0

        if (arr11[2] - arr11[1] == 1 and arr11[1] - arr11[0] == 1) or len(set(arr11)) == 1:
            res11 = 1

        if (arr12[2] - arr12[1] == 1 and arr12[1] - arr12[0] == 1) or len(set(arr12)) == 1:
            res12 = 1

        if res11 + res12 == 2:
            ret.append(arr1)

        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr1.append(lst[i])
            checkBabygin(k+1)
            visited[i] = False
            arr1.pop()

T = int(input())
for case in range(1, T+1):
    lst = list(map(int, input()))
    N = len(lst)

    ret = []
    arr1 = []
    visited = [False]*N

    checkBabygin(0)

    print('True' if ret else 'False')