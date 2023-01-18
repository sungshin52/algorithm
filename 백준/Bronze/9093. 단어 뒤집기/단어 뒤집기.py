T = int(input())

for t in range (1, T+1):
    string = list(map(list, input().split()))

    for word in string:
        print(''.join(word[::-1]), end = ' ')