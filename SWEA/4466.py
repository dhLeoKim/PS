import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(T):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    lst.sort(reverse= True)

    print(f'#{case+1}', sum(lst[:K]))