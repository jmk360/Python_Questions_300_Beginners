# 261번
# sol)
# class Stock:
#     pass

# 262번
# sol)
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code

# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)

# 263번
# sol)
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#     def set_name(self, name):
#         self.name = name

# 삼성 = Stock(None, None)
# print(삼성.name)
# print(삼성.code)
# 삼성.set_name("삼성전자")
# print(삼성.name)
# print(삼성.code)

# 264번
# sol)
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#     def set_name(self, name):
#         self.name = name
#     def set_code(self, code):
#         self.code = code

# 삼성 = Stock(None, None)
# print(삼성.name)
# print(삼성.code)
# 삼성.set_name("삼성전자")
# 삼성.set_code('005930')
# print(삼성.name)
# print(삼성.code)

# 265번
# sol)
# class Stock:
#     def __init__(self, name, code):
#         self.name = name
#         self.code = code
#     def set_name(self, name):
#         self.name = name
#     def set_code(self, code):
#         self.code = code
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code

# 삼성 = Stock("삼성전자", "005930")
# print(삼성.name)
# print(삼성.code)
# print(삼성.get_name())
# print(삼성.get_code())

# 266번
# sol)
# class Stock:
#     def __init__(self, name, code, per, pbr, div_yield):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.div_yield = div_yield
#     def set_name(self, name):
#         self.name = name
#     def set_code(self, code):
#         self.code = code
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code

# 267번
# sol)
# class Stock:
#     def __init__(self, name, code, per, pbr, div_yield):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.div_yield = div_yield
#     def set_name(self, name):
#         self.name = name
#     def set_code(self, code):
#         self.code = code
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code

# samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)

# 268번
# sol)
# class Stock:
#     def __init__(self, name, code, per, pbr, dividend):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.dividend = dividend
#     def set_name(self, name):
#         self.name = name
#     def set_code(self, code):
#         self.code = code
#     def set_per(self, per):
#         self.per = per
#     def set_pbr(self, pbr):
#         self.pbr = pbr
#     def set_dividend(self, dividend):
#         self.dividend = dividend
               
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code

# samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)

# 269번
# sol)
# class Stock:
#     def __init__(self, name, code, per, pbr, dividend):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.dividend = dividend
#     def set_name(self, name):
#         self.name = name
#     def set_code(self, code):
#         self.code = code
#     def set_per(self, per):
#         self.per = per
#     def set_pbr(self, pbr):
#         self.pbr = pbr
#     def set_dividend(self, dividend):
#         self.dividend = dividend
               
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code

# samsung = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
# print(samsung.per)
# samsung.set_per(12.75)
# print(samsung.per)

# 270번
# sol)
# class Stock:
#     def __init__(self, name, code, per, pbr, dividend):
#         self.name = name
#         self.code = code
#         self.per = per
#         self.pbr = pbr
#         self.dividend = dividend
#     def set_name(self, name):
#         self.name = name
#     def set_code(self, code):
#         self.code = code
#     def set_per(self, per):
#         self.per = per
#     def set_pbr(self, pbr):
#         self.pbr = pbr
#     def set_dividend(self, dividend):
#         self.dividend = dividend
               
#     def get_name(self):
#         return self.name
#     def get_code(self):
#         return self.code

# stock_list = [Stock('삼성전자', '005930', 15.79, 1.33, 2.83), Stock('현대차', '005380', 8.70, 0.35, 4.27),
#                 Stock('LG전자', '066570', 317.34, 0.69, 1.37)]

# for stock in stock_list:
#     print(stock.code, stock.per)