dial_alph = {2: ['A', 'B', 'C'], 3: ['D', 'E', 'F'], 4: ['G', 'H', 'I'],
            5: ['J', 'K', 'L'], 6: ['M', 'N', 'O'], 7: ['P', 'Q', 'R', 'S'],
            8: ['T', 'U', 'V'], 9: ['W', 'X', 'Y', 'Z']}
sec = 0

word = input()

for alph in word:
    for key in dial_alph:
        if alph in dial_alph[key]:
            sec += key + 1

print(sec)