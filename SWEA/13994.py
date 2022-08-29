import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for case in range(T):
    N = int(input())

    busstop = [0]*1001

    for _ in range(N):
        M, A, B= map(int, input().split())

        busstop[A] += 1
        busstop[B] += 1
        if M == 1:
            for i in range(A+1, B):
                busstop[i] += 1
        elif M == 2:
            busstop[A] -= 1
            for i in range(A, B, 2):
                busstop[i] += 1
        elif M == 3:
            for i in range(A+1, B):
                if A%2 == 1 and i%3 == 0 and i%10 != 0:
                    busstop[i] += 1
                elif A%2 == 0 and i%4 == 0:
                    busstop[i] += 1

    print(f'#{case+1} {max(busstop)}')