# 121번
# sol)
# a = input('>> ')
# if a.islower():
#     print(a.upper())
# else:
#     print(a.lower())

# 122번
# sol)
# score = int(input('>> score: '))
# if 81 <= score <= 100:
#     grade = 'A'
# elif 61 <= score <= 80:
#     grade = 'B'
# elif 41 <= score <= 60:
#     grade = 'C'
# elif 21 <= score <= 40:
#     grade = 'D'
# else:
#     grade = 'E'
# print('grade is', grade)

# 123번
# sol)
# a = input('>> 입력: ')
# n, nn = a.split()
# if nn == '달러':
#     print(float(n)*1167,'원')
# elif nn == '엔':
#     print(float(n)*1.096,'원')
# elif nn == '유로':
#     print(float(n)*1268,'원')
# elif nn == '위안':
#     print(float(n)*171,'원')

# 124번
# sol)
# a = int(input('>> input number1: '))
# b = int(input('>> input number2: '))
# c = int(input('>> input number3: '))
# if a > b and a > c:
#     max = a
# elif b > a and b > c:
#     max = b
# else:
#     max = c
# print(max)

# 125번
# sol)
# myDict = {'011':'SKT', '016': 'KT', '019': 'LGU', '010':'알수없음'}
# number = input('>> 휴대전화 번호 입력: ')
# print('당신은 {} 사용자입니다.'.format(myDict.get(number[:3])))

# 126번
# sol)
# myDict = {'010':'강북구', '011':'강북구', '012':'강북구', '013':'도봉구', '014':'도봉구','015':'도봉구', '016':'노원구', '017':'노원구',
#             '018':'노원구', '019':'노원구'}
# a = input('>> 우편번호: ')
# print(myDict.get(a[:3]))

# 127번
# sol)
# number = input('>> 주민등록번호: ')
# if int(number[7]) % 2 == 0:
#     print('여자')
# else:
#     print('남자')

# 128번
# sol)
# number = input('>> 주민등록번호: ')
# if number[-6:-4] in ['00', '01', '02', '03', '04', '05', '06', '07', '08']:
#     print('서울입니다.')
# else:
#     print('서울이 아닙니다.')

# 129번
# sol)
# num = input('>> 주민등록번호: ')
# bb = int(num[-1])
# aa = (2,3,4,5,6,7,8,9,2,3,4,5)
# num = num.replace('-', '')
# sum = 0
# for i, n in enumerate(num[:-1]):
#     sum += int(n) * aa[i]
# result = 11 - sum % 11
# if bb == result:
#     print('유효한 주민등록번호입니다.')
# else:
#     print('유효하지 않은 주민등록번호입니다.')

# 130번
# sol)
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# print(btc)
# cc = int(btc.get('max_price')) - int(btc.get('min_price'))
# rr = int(btc.get('opening_price')) + cc

# if rr > int(btc.get('max_price')):
#     print('상승장')
# else:
#     print('하락장') 