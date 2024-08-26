import sys
input = sys.stdin.readline

N = int(input())
prime_number = []
prime_bool = [True]*(N+1)


for i in range(2, N+1):
    if prime_bool[i]:
        prime_number.append(i)
        for j in range(2*i, N+1, i):
            prime_bool[j] = False

ret = 0
start = 0
end = 0
temp = 0

for start in range(len(prime_number)):
    while temp < N and end < len(prime_number):
        temp += prime_number[end]
        end += 1
    
    if temp == N:
        ret += 1

    temp -= prime_number[start]
    
print(ret)