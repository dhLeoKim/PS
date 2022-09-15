import sys
sys.stdin = open('sample_input.txt')

def inorder(N):                     # 중위 순회
    global num
    if N:
        inorder(ch1[N])
        node[N] = num
        num += 1
        inorder(ch2[N])

T = int(input())
for case in range(1, T+1):
    N = int(input())

    node = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)

    for i in range(1, N//2+1):      # tree 저장
        ch1[i] = i*2
        if i*2 + 1 > N: continue
        ch2[i] = i*2 + 1

    num = 1
    inorder(1)
    print(f'#{case} {node[1]} {node[N//2]}')