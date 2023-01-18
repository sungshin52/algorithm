word = input()
alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in alph:
    word = word.replace(i, '1')

print(len(word))