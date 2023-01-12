# 정수 입력
N = int(input())

# 약수 찾기
for i in range(1, N//2 + 1):
    if (N % i == 0):
        print(i, end = ' ')
print(N)