alph_list = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

words = input()

for word in words:
    if word in alph_list:
        words = words.replace(word, '')

print(words)