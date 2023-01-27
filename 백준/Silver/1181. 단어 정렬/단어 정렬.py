import sys

word_list = []

N = int(sys.stdin.readline())

for _ in range (N):
    word = sys.stdin.readline().strip()
    if word not in word_list:
        word_list.append(word)

word_list.sort()
word_list.sort(key = len)

for w in word_list:
    print(w)