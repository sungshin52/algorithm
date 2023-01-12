# 비밀번호 P와 주어지는 번호 K 입력
P, K = list(map(int, input().split()))

# P와 K 사이 차이로 몇 번 만에 맞출 수 있는지 구하기
tryout =  P - K + 1

print(tryout)