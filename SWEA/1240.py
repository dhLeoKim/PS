import sys
sys.stdin = open('input.txt')

T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    lst = [input() for _ in range(N)]

    pattern = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }
    
    for row in lst:
        if '1' in row:
            break

    k = 0
    num = []
    while k < len(row):
        bit = row[k:k+7]
        if bit not in pattern.keys():
            k += 1
        else:
            num.append(pattern[bit])
            k += 7
    
    temp = 0
    for i in range(len(num)):
        if i%2:
            temp += num[i]
        else:
            temp += num[i]*3

    ret = 0 if temp%10 else sum(num)

    print(f'#{case} {ret}')