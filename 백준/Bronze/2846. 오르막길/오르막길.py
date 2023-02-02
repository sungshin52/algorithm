import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
height = []
h_tmp = 0

for i in range (N-1):
    if road[i] < road[i+1]:
        h_tmp += road[i+1] - road[i]

        if i == N-2:
            height.append(h_tmp)

    else:
        height.append(h_tmp)
        h_tmp = 0
    
print(max(height))