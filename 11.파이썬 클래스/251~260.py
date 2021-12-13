# 251번
# sol)
# 클래스 : 객체를 찍어 내는 틀
# 객체 : 클래스로부터 나온 것
# 인스턴스 : 객체와 같음

# 252번
# sol)
# class Human:
#     pass

# 253번
# sol)
# class Human:
#     pass
# areum = Human()

# 254번
# sol)
# class Human:
#     def __init__(self):
#         print('응애응애')
# areum = Human()

# 255번
# sol)
# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# areum = Human("아름", 25, '여')
# print(areum.name)

# 256번
# sol)
# class Human:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
# areum = Human("조아름", 25, '여자')
# print(f"이름 : {areum.name}, 나이 : {areum.age}, 성별 : {areum.gender}")

# 257번
# sol)
# class Human:
#     def __init__(self, name, age ,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def who(self):
#         print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}")

# areum = Human('조아름', 25, '여자')
# areum.who()

# 258번
# sol)
# class Human:
#     def __init__(self, name, age ,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def who(self):
#         print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}")

#     def setInfo(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

# areum = Human('모름', 0, '모름')
# areum.who()
# areum.setInfo('아름', 25, '여자')
# areum.who()

# 259번
# sol)
# class Human:
#     def __init__(self, name, age ,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
    
#     def who(self):
#         print(f"이름 : {self.name}, 나이 : {self.age}, 성별 : {self.gender}")

#     def setInfo(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender

#     def __del__(self):
#         print('나의 죽음을 알리지 말라')

# areum = Human('모름', 0, '모름')
# areum.who()
# areum.setInfo('아름', 25, '여자')
# areum.who()
# del areum

# 260번
# sol)
# class OMG : 
#     def print() :
#         print("Oh my god")

# myStock = OMG()
# OMG.print()
# 클래스 변수는 인스턴스를 통해서 접근이 불가능하고, 오직 클래스명을 통해서만 사용가능하다.