import sys
sys.stdin = open('sample_input.txt')

def backtracking(k, cnt):
    global ret
    if k >= N-1:
        ret = cnt
        return

    elif cnt >= ret:                    # prunning
        return

    for i in range(lst[k], 0, -1):      # 충전소 개수 만큼 for, 역순으로 탐색 줄이기
        backtracking(k+i, cnt+1)


T = int(input())
for case in range(1, T+1):
    N, *lst = map(int, input().split())

    ret = N
    backtracking(0, -1)

    print(f'#{case}', ret)