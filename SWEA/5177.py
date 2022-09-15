
import sys
sys.stdin = open('sample_input.txt')

####################
# 1. heapq 사용

from heapq import*

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    heap = []
    for i in lst:               # heappush(enq)
        heappush(heap, i)

    ret = 0
    i = len(lst)//2
    while i:                    # 끝 노드의 조상노드 합
        ret += heap[i-1]
        i //= 2

    print(f'#{case} {ret}')


####################
# 2. heap 구현

def enq(n):                     # heap enq(heappush)
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2

T = int(input())
for case in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    heap = [0]*(N+1)
    last = 0
    for i in lst:
        enq(i)
    
    i = (len(heap)-1) // 2
    ret = 0
    while i:                # 끝 노드의 조상노드 합
        ret += heap[i]
        i //= 2

    print(f'#{case} {ret}')