# 171번
# sol)
# price_list = [32100, 32150, 32000, 32500]
# for i in price_list:
#     print(i)

# 172번
# sol)
# price_list = [32100, 32150, 32000, 32500]
# j = 0
# for i in range(len(price_list)):
#     print('{} {}'.format(i, price_list[i]))

# 173번
# sol)
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print('{} {}'.format(3-i, price_list[i]))

# 174번
# sol)
# price_list = [32100, 32150, 32000, 32500]
# ll = [100, 110, 120]
# zz = list(zip(ll, price_list[1:]))
# for i in range(3):
#     print('{} {}'.format(*(zz[i])))

# 175번
# sol)
# my_list = ["가", "나", "다", "라"]
# for i in range(3):
#     print('{} {}'.format(my_list[i], my_list[i+1]))

# 176번
# sol)
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):
#     print('{} {} {}'.format(my_list[i],my_list[i+1],my_list[i+2]))

# 177번
# sol)
# my_list = ["가", "나", "다", "라"]
# for i in range(3,0,-1):
#     print('{} {}'.format(my_list[i], my_list[i-1]))

# 178번
# sol)
# my_list = [100, 200, 400, 800]
# for i in range(3):
#     print(my_list[i+1] - my_list[i])

# 179번
# sol)
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(my_list)-2):
#     ss = sum(my_list[i:i+3])
#     avg = ss / 3
#     print(avg)

# 180번
# sol)
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# cc = []
# for i in range(len(low_prices)):
#     cc.append(high_prices[i] - low_prices[i])
# print(cc)