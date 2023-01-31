import sys
input = sys.stdin.readline

words_temp = []

for _ in range (5):
    words_temp.append(input().rstrip())

max_words = len(max(words_temp, key = len))
words = [[''] * 5 for _ in range (max_words)]

for i in range (5):
    for j in range (max_words):
        words[j][i] = words_temp[i][j:j+1:]

for i in range (max_words):
    for j in range(5):
        print(words[i][j], end = '')