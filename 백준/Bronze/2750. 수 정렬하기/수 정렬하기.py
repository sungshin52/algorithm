N = int(input())
n_list = []

for n in range (N):
    n_list.append(int(input()))

n_list.sort()

for n in range (N):
    print(n_list[n])