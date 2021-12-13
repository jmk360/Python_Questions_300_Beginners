# 221번
# sol)
# def print_reverse(st):
#     print(st[::-1])
# print_reverse('python')

# 222번
# sol)
# def print_score(_list):
#     print(sum(_list) / len(_list))

# print_score([1,2,3])

# 223번
# sol)
# def print_even(_list):
#     for i in [n for n in _list if n % 2 == 0]:
#         print(i)
# print_even([1,3,2,10,12,11,15])

# 224번
# sol)
# def print_keys(_dict):
#     for k in _dict:
#         print(k)
# print_keys({"이름":"김말똥", '나이':30, '성별':0})

# 225번
# sol)
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# def print_value_by_key(_dict, key):
#     print(_dict.get(key))
# print_value_by_key(my_dict, "10/26")

# 226번
# sol)
# def print_5xn(_string):
#     for i, s in enumerate(_string):
#         print(s, end='')
#         if (i+1) % 5 == 0:
#             print()

# print_5xn('아이엠어보이유알어걸')

# 227번
# sol)
# def print_mxn(_string, num):
#     for i, s in enumerate(_string):
#         print(s, end='')
#         if (i+1) % num == 0:
#             print()
# def print_mxn2(line, num):
#     chunk_num = int(len(line) / num)
#     for x in range(chunk_num + 1):
#         print(line[x*num:x*num+num])

# print_mxn2('아이엠어보이유알어걸', 3)

# 228번
# sol)
# def calc_monthly_salary(annual_salary):
#     print(int(annual_salary / 12))

# calc_monthly_salary(12000000)

# 229번
# sol)
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(a=100, b=200)

# 230번
# sol)
# def my_print (a, b) :
#     print("왼쪽:", a)
#     print("오른쪽:", b)

# my_print(b=100, a=200)