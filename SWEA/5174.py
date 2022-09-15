import sys
sys.stdin = open('sample_input.txt')

##########################
# 1. ch1, ch2 배열 두개로 저장

def preorder(N):            # 전위 순회
    global cnt
    if N:
        cnt += 1
        preorder(ch1[N])
        preorder(ch2[N])

T = int(input())

for case in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    ch1 = [0]*(E+2)
    ch2 = [0]*(E+2)

    for i in range(E):      # tree 저장
        p, c = lst[i*2], lst[i*2 + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    cnt = 0
    preorder(N)

    print(f'#{case} {cnt}')

##########################
# 2. 인접 리스트로 저장

def preorder(N):        # 전위 순회
    global cnt
    if tree[N]:
        for nxt in tree[N]:
            cnt += 1
            preorder(nxt)

T = int(input())

for case in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    tree = [[] for _ in range(E+2)]

    for i in range(E):      # tree 저장
        tree[lst[2*i]].append(lst[2*i + 1])

    cnt = 1
    preorder(N)

    print(f'#{case} {cnt}')

##########################
# 3. 인접 배열로 저장

def preorder(N):            # 전위 순회
    global cnt
    for nxt in range(E+2):
        if tree[N][nxt]:
            cnt += 1
            preorder(nxt)

T = int(input())

for case in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))

    tree = [[0]*(E+2) for _ in range(E+2)]

    for i in range(E):      # tree 저장
        tree[lst[2*i]][lst[2*i + 1]] = 1

    cnt = 1
    preorder(N)

    print(f'#{case} {cnt}')