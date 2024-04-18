import sys
sys.stdin = open('input_1094.txt')
input = sys.stdin.readline

X = int(input())
rod = [64]

while sum(rod) > X:
    temp = rod.pop()
    half = temp//2
    rod.append(half)
    
    if sum(rod) < X:
        rod.append(half)
    elif sum(rod) == X:
        break

    rod.sort(reverse=True)

print(len(rod))