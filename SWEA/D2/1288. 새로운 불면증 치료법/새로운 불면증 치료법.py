
# 테스트 케이스 입력
T = int(input())
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for t in range (1, T+1):
    N = int(input())
    i = 1
    num_sheep = []

    while True:
        sheep = str(i * N)

        for j in range (len(sheep)):
            if (sheep[j] not in num_sheep):
                num_sheep.append(sheep[j])
        num_sheep.sort()

        if (num_sheep == num_list):
            break

        i += 1

    print(f'#{t} {sheep}')