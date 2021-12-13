# 231번
# sol)
# def n_plus_1 (n) :
#     result = n + 1

# n_plus_1(3)
# print (result)

# 232번
# sol)
# def make_url(domain):
#     return 'www.'+domain+'.com'
# print(make_url('naver')) 

# 233번
# sol)
# def make_list(_str):
#     return list(_str)
# print(make_list('abcd'))

# 234번
# sol)
# def pickup_even(_list):
#     return [n for n in _list if n % 2 == 0]
# print(pickup_even([3,4,5,6,7,8]))

# 235번
# sol)
# def convert_int(_str):
#     return int(_str.replace(',',''))
# print(convert_int('1,234,567'))

# 236번
# sol)
# def 함수(num) :
#     return num + 4

# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)

# 237번
# sol)
# def 함수(num) :
#     return num + 4

# c = 함수(함수(함수(10)))
# print(c)

# 238번
# sol)
# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     return num * 10

# a = 함수1(10)
# c = 함수2(a)
# print(c)

# 239번
# sol)
# def 함수1(num) :
#     return num + 4

# def 함수2(num) :
#     num = num + 2
#     return 함수1(num)

# c = 함수2(10)
# print(c)

# 240번
# sol)
# def 함수0(num) :
#     return num * 2

# def 함수1(num) :
#     return 함수0(num + 2)

# def 함수2(num) :
#     num = num + 10
#     return 함수1(num)

# c = 함수2(2)
# print(c)