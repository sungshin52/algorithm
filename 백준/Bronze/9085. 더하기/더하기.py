T = int(input())

for t in range (1, T+1):
    N = int(input())
    n_list = list(map(int, input().split()))
    
    print(sum(n_list))