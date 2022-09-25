import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    b = input()
    t = input()

    b_set = {'0', '1'}
    t_set = {'0', '1', '2'}

    b_10 = []
    for i in range(len(b)):
        lst = b_set - set(b[i])
        temp = list(b)
        for j in lst:
            temp[i] = j
            b_10.append(int('0b' + ''.join(temp), 2))

    t_10 = []
    for i in range(len(t)):
        lst = t_set - set(t[i])
        temp = list(t)
        for j in lst:
            temp[i] = j
            a = 0
            for k in range(len(temp)):
                a += 3**(len(temp)-1-k)*int(temp[k])
            t_10.append(a)

    for i in b_10:
        if i in t_10:
            ret = i
            break

    print(f'#{case} {ret}')