import sys
sys.stdin = open('input_p3.txt')

T = int(input())
for case in range(T):
    lst = input()

    num = ''
    for i in lst:
        temp = bin(int(i, 16))
        num += '0'*(6 - len(temp)) + temp[2:]

    pattern = {
        '001101': 0,
        '010011': 1,
        '111011': 2,
        '110001': 3,
        '100011': 4,
        '110111': 5,
        '001011': 6,
        '111101': 7,
        '011001': 8,
        '101111': 9,
    }

    bit = num[:6]
    k = 0
    while bit not in pattern.keys():
        bit = bit[1:] + num[k+6]
        k += 1

    num = num[k:len(num)-k]

    for i in range(len(num)//6):
        temp = num[6*i:6*(i+1)]
        print(pattern[temp], end=' ')
    
    print()