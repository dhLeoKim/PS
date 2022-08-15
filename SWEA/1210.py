T = 10
for case in range(T):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(len(arr)):
        if arr[-1][i] == 2:
            e = [99, i]

    e = [e[0]-1, e[1]]
    cmd = 'U'
    while e[0] > 0:
        if cmd == 'U':
            if 0 < e[1] and arr[e[0]][e[1]-1] == 1:
                e = [e[0], e[1]-1]
                cmd = 'L'
            elif e[1] < 99 and arr[e[0]][e[1]+1] == 1:
                e = [e[0], e[1]+1]
                cmd = 'R'
            else:
                e = [e[0] - 1, e[1]]
                cmd = 'U'

        elif cmd == 'L':
            if 0 < e[1] and arr[e[0]][e[1] - 1] == 1:
                e = [e[0], e[1]-1]
                cmd = 'L'
            else:
                e = [e[0]-1, e[1]]
                cmd = 'U'

        elif cmd == 'R':
            if e[1] < 99 and arr[e[0]][e[1]+1] == 1:
                e = [e[0], e[1]+1]
                cmd = 'R'
            else:
                e = [e[0]-1, e[1]]
                cmd = 'U'

    print(f'#{case+1} {e[1]}')

# pseudo code
'''
while e[0] > 0:
    if cmd == 'U':
        if checkL():
            moveL()
            cmd = 'L'
        elif checkR():
            moveR()
            cmd = 'R'
        else:
            moveUp()
            cmd = 'U'

    elif cmd == 'L':
        if checkL():
            moveL()
            cmd = 'L'
        else:
            moveUp()
            cmd = 'U'

    elif cmd == 'R':
        if checkR():
            moveR()
            cmd = 'R'
        else:
            moveUp()
            cmd = 'U'
'''