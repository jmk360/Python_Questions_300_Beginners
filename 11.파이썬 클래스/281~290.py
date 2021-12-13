# 281번
# sol)
# class Car:
#     def __init__(self, wheelNum, price):
#         self.wheelNum = wheelNum
#         self.price = price

# car = Car(2, 1000)
# print(car.wheelNum)
# print(car.price)

# 282번
# sol)
# class Car:
#     def __init__(self, wheelNum, price):
#         self.wheelNum = wheelNum
#         self.price = price

# def Bicycle(Car):
#     pass

# 283번
# sol)
# class Car:
#     def __init__(self, wheelNum, price):
#         self.wheelNum = wheelNum
#         self.price = price

# class Bicycle(Car):
#     def __init__(self, wheelNum, price):
#         super().__init__(wheelNum, price)

# bicycle = Bicycle(2, 100)
# print(bicycle.price)

# 284번
# sol)
# class Car:
#     def __init__(self, wheelNum, price):
#         self.wheelNum = wheelNum
#         self.price = price

# class Bicycle(Car):
#     def __init__(self, wheelNum, price, driving_system):
#         super().__init__(wheelNum, price)
#         self.driving_system = driving_system

# bicycle = Bicycle(2, 100, '시마노')
# print(bicycle.driving_system)

# 285번
# sol)
# class Car:
#     def __init__(self, wheelNum, price):
#         self.wheelNum = wheelNum
#         self.price = price
#     def dispaly_info(self):
#         print('바퀴수', self.wheelNum)
#         print('가격', self.price)

# class Bicycle(Car):
#     def __init__(self, wheelNum, price, driving_system):
#         super().__init__(wheelNum, price)
#         self.driving_system = driving_system

# class Car2(Car):
#     def __init__(self, wheelNum, price):
#         super().__init__(wheelNum, price)
    

# car = Car2(4, 1000)
# car.dispaly_info()

# 286번
# sol)
# class Car:
#     def __init__(self, wheelNum, price):
#         self.wheelNum = wheelNum
#         self.price = price
#     def display_info(self):
#         print('바퀴수', self.wheelNum)
#         print('가격', self.price)

# class Bicycle(Car):
#     def __init__(self, wheelNum, price, driving_system):
#         super().__init__(wheelNum, price)
#         self.driving_system = driving_system

# class Car2(Car):
#     def __init__(self, wheelNum, price):
#         super().__init__(wheelNum, price)
    

# bicycle = Bicycle(2, 100, '시마노')
# bicycle.display_info()

# 287번
# sol)
# class Car:
#     def __init__(self, wheelNum, price):
#         self.wheelNum = wheelNum
#         self.price = price
#     def display_info(self):
#         print('바퀴수', self.wheelNum)
#         print('가격', self.price)

# class Bicycle(Car):
#     def __init__(self, wheelNum, price, driving_system):
#         super().__init__(wheelNum, price)
#         self.driving_system = driving_system
#     def display_info(self):
#         print('바퀴수', self.wheelNum)
#         print('가격', self.price)
#         print('구동계', self.driving_system)

# class Car2(Car):
#     def __init__(self, wheelNum, price):
#         super().__init__(wheelNum, price)
    

# bicycle = Bicycle(2, 100, '시마노')
# bicycle.display_info()

# 288번
# sol)
# class 부모:
#   def 호출(self):
#     print("부모호출")

# class 자식(부모):
#   def 호출(self):
#     print("자식호출")
# 나 = 자식()
# 나.호출()

# 289번
# sol)
# class 부모:
#   def __init__(self):
#     print("부모생성")

# class 자식(부모):
#   def __init__(self):
#     print("자식생성")

# 나 = 자식()

# 290번
# sol)
# class 부모:
#   def __init__(self):
#     print("부모생성")

# class 자식(부모):
#   def __init__(self):
#     print("자식생성")
#     super().__init__()

# 나 = 자식()