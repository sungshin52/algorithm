# 테스트 케이스 입력
T = int(input())

month_31 = ['01', '03', '05', '07', '08', '10', '12']
month_30 = ['04', '06', '09', '11']

# 테스트 케이스별 날짜 입력 (str type)
for t in range (1, T+1):
    date = input()

    # 0월일 때 처리
    if (date[4:6] == '00'):
        print(f'#{t} -1')
    
    # 1, 3, 5, 7, 8, 10, 12월 31일까지 처리
    elif (date[4:6] in month_31):
        if(int(date[6:]) == 0 or int(date[6:]) > 31):
            print(f'#{t} -1')
        
        else:
            real_date = date[:4] + '/' + date[4:6] + '/' + date[6:]
            print(f'#{t} {real_date}')

    # 2월 28일까지 처리
    elif (date[4:6] == '02'):
        if(int(date[6:]) == 0 or int(date[6:]) > 28):
            print(f'#{t} -1')

        else:
            real_date = date[:4] + '/' + date[4:6] + '/' + date[6:]
            print(f'#{t} {real_date}')

    # 4, 6, 9, 11월 30일까지 처리
    elif (date[4:6] in month_30):
        if(int(date[6:]) == 0 or int(date[6:]) > 30):
            print(f'#{t} -1')

        else:
            real_date = date[:4] + '/' + date[4:6] + '/' + date[6:]
            print(f'#{t} {real_date}')