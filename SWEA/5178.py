import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    N, M, L = map(int, input().split())
    node = [0]*(N+1)
    for _ in range(M):              # 노드 정보 저장
        key, val = map(int, input().split())
        node[key] = val

    tree = [0]*(N+1)                # 이진 트리
    for i in range(1, N+1):
        tree[i] = i//2

    for i in range(N, 0, -1):       # 자식 노드 합
        node[tree[i]] += node[i]

    print(f'#{case} {node[L]}')