duck = []

start = input()

while 1:
    prob = input()

    if prob == '고무오리 디버깅 끝':
        break

    else:
        if prob == '문제':
            duck.append(1)
            
        elif prob == '고무오리':
            if duck.count(1) == 0:
                [duck.append(1) for _ in range (2)]
            else:
                duck.pop()
 
if duck:
    print('힝구')
else:
    print('고무오리야 사랑해')