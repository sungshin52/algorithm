import sys
input = sys.stdin.readline

train = []
people = 0

for _ in range (4):
    out_train, in_train = map(int, input().split())

    people += in_train - out_train
    train.append(people)

print(max(train))