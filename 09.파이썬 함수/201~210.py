# 201번
# sol)
# def print_coin():
#     print('비트코인')

# print_coin()

# 202번
# sol)
# print_coin()

# 203번
# sol)
# for i in range(100):
#     print_coin()

# 204번
# sol)
# def print_coin():
#     for i in range(100):
#         print('비트코인')
# print_coin()

# 205번
# sol)
# 함수가 정의되기 전에 호출되어서 에러가 발생한다.

# 206번
# sol)
# def message() :
#     print("A")
#     print("B")

# message()
# print("C")
# message()

# 207번
# sol)
# print("A")

# def message() :
#     print("B")

# print("C")
# message()

# 208번
# sol)
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()

# 209번
# sol)
# def message1():
#     print("A")

# def message2():
#     print("B")
#     message1()

# message2()

# 210번
# sol)
# def message1():
#     print("A")

# def message2():
#     print("B")

# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()

# message3()