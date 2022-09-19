import sys
sys.stdin = open('input_p2.txt')

from collections import deque

T = int(input())
for case in range(T):
    lst = list(input())

    num = ''
    for i in lst:
        temp = bin(int(i, 16))
        num += '0'*(6 - len(temp)) + temp[2:]
    
    a, b = divmod(len(num), 7)

    for k in range(a):
        temp = '0b' + num[7*k:7*(k+1)]
        print(int(temp, 2), end=' ')

    k += 1
    temp = '0b' + num[7*k:7*k+b]
    print(int(temp, 2))