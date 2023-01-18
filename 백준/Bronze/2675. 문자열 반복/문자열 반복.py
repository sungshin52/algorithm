T = int(input())

for t in range (1, T+1):
    R, S = input().split()
    R = int(R)
    P = ''

    for i in range (len(S)):
        P += S[i: i+1] * R
    
    print(P)