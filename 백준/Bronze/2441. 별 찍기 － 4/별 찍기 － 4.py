import sys
input = sys.stdin.readline

N = int(input())

for n in range (N+1):
    print(' ' * n + '*' * (N-n))