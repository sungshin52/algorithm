N = int(input())
survey_list = []

for i in range (N):
    survey_list.append(int(input()))

count_one = survey_list.count(1)
count_zero = survey_list.count(0)

if (count_one < count_zero):
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')