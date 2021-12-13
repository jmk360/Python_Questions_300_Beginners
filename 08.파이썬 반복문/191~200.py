# 191번
# sol)
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for row in data:
#     for j in row:
#         print(j*(1+0.00014))

# 192번
# sol)
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for row in data:
#     for j in row:
#         print(j*(1+0.00014))
#     print('-'*4)

# 193번
# sol)
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []

# for row in data:
#     for j in row:
#         result.append(j*(1+0.00014))
# print(result)

# 194번
# sol)
# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for row in data:
#     re1 = []
#     for j in row:
#         re1.append(j*(1+0.00014))
#     result.append(re1)
# print(result)

# 195번
# sol)
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:4]:
#     print(i[3])

# 196번
# sol)
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#     if i[3] > 150:
#         print(i[3])

# 197번
# sol)
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#     if i[0] <= i[3]:
#         print(i[3])

# 198번
# sol)
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility = []
# for i in ohlc[1:]:
#     volatility.append(i[1] - i[2])
# print(volatility)

# 199번
# sol)
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in ohlc[1:]:
#     if i[0] < i[3]:
#         print(i[1] - i[2])

# 200번
# sol)
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# sum = 0
# for i in ohlc[1:]:
#     sum += i[3] - i[0]
# print(sum)