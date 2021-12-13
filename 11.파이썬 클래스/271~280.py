# 271번
# sol)
# from random import randint

# class Account:
#     def __init__(self, name, balance):
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance

# kim = Account("김민수", 100)
# print(kim.name)
# print(kim.balance)
# print(kim.bank)
# print(kim.account_number)

# 272번
# sol)
# from random import randint

# class Account:
#     account_count = 0
#     def __init__(self, name, balance):
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance
#         Account.account_count += 1

# kim = Account("김민수", 100)
# print(Account.account_count)
# lee = Account("이민수", 100)
# print(Account.account_count)

# 273번
# sol)
# from random import randint

# class Account:
#     account_count = 0
#     def __init__(self, name, balance):
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance
#         Account.account_count += 1
#     @classmethod
#     def get_account_num(cls):
#         print('개설된 계좌 수 :',cls.account_count)

# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# Account.get_account_num()

# 274번
# sol)
# from random import randint

# class Account:
#     account_count = 0
#     def __init__(self, name, balance):
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance
#         Account.account_count += 1

#     def deposit(self, money):
#         if money >= 1:
#             self.balance += money

#     @classmethod
#     def get_account_num(cls):
#         print('개설된 계좌 수 :',cls.account_count)

# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# kim.deposit(300)
# print(kim.balance)

# 275번
# sol)
# from random import randint

# class Account:
#     account_count = 0
#     def __init__(self, name, balance):
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance
#         Account.account_count += 1

#     def deposit(self, money):
#         if money >= 1:
#             self.balance += money

#     def withdraw(self, money):
#         if self.balance > money:
#             self.balance -= money

#     @classmethod
#     def get_account_num(cls):
#         print('개설된 계좌 수 :',cls.account_count)

# k = Account('kim', 100)
# k.deposit(100)
# k.withdraw(90)
# print(k.balance)

# 276번
# sol)
# from random import randint

# class Account:
#     account_count = 0
#     def __init__(self, name, balance):
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance
#         Account.account_count += 1

#     def deposit(self, money):
#         if money >= 1:
#             self.balance += money

#     def withdraw(self, money):
#         if self.balance > money:
#             self.balance -= money
    
#     def display_info(self):
#         print('은행이름:', self.bank)
#         print('예금주:', self.name)
#         print('계좌번호:', self.account_number)
#         balanceStr = str(self.balance)[::-1]
#         myList = []
#         for i in range(0, len(balanceStr), 3):
#             myList.append(balanceStr[i:i+3])
#         balanceStr = ','.join(myList)[::-1]
#         print('잔고: {}'.format(balanceStr))

#     @classmethod
#     def get_account_num(cls):
#         print('개설된 계좌 수 :',cls.account_count)

# p = Account('파이썬', 10000000000)
# p.display_info()

# 277번
# sol)
# from random import randint

# class Account:
#     account_count = 0
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance
#         Account.account_count += 1

#     def deposit(self, money):
#         if money >= 1:
#             self.balance += money
#         self.deposit_count += 1
#         if self.deposit_count % 5 == 0:
#             self.balance = int(self.balance * (1+0.01))

#     def withdraw(self, money):
#         if self.balance > money:
#             self.balance -= money
    
#     def display_info(self):
#         print('은행이름:', self.bank)
#         print('예금주:', self.name)
#         print('계좌번호:', self.account_number)
#         balanceStr = str(self.balance)[::-1]
#         myList = []
#         for i in range(0, len(balanceStr), 3):
#             myList.append(balanceStr[i:i+3])
#         balanceStr = ','.join(myList)[::-1]
#         print('잔고: {}원'.format(balanceStr))

#     @classmethod
#     def get_account_num(cls):
#         print('개설된 계좌 수 :',cls.account_count)

# p = Account('파이썬', 10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(5000)
# p.deposit(5000) # 50,500원
# p.display_info()

# 278번
# sol)
# from random import randint

# class Account:
#     account_count = 0
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance
#         Account.account_count += 1

#     def deposit(self, money):
#         if money >= 1:
#             self.balance += money
#         self.deposit_count += 1
#         if self.deposit_count % 5 == 0:
#             self.balance = int(self.balance * (1+0.01))

#     def withdraw(self, money):
#         if self.balance > money:
#             self.balance -= money
    
#     def display_info(self):
#         print('은행이름:', self.bank)
#         print('예금주:', self.name)
#         print('계좌번호:', self.account_number)
#         balanceStr = str(self.balance)[::-1]
#         myList = []
#         for i in range(0, len(balanceStr), 3):
#             myList.append(balanceStr[i:i+3])
#         balanceStr = ','.join(myList)[::-1]
#         print('잔고: {}원'.format(balanceStr))

#     @classmethod
#     def get_account_num(cls):
#         print('개설된 계좌 수 :',cls.account_count)

# myList = []
# myList.append(Account('홍길동', 100))
# myList.append(Account('황인국', 500))
# myList.append(Account('박기태', 1000))
# print(myList)

# 279번
# sol)
# from random import randint

# class Account:
#     account_count = 0
#     def __init__(self, name, balance):
#         self.deposit_count = 0
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance
#         Account.account_count += 1

#     def deposit(self, money):
#         if money >= 1:
#             self.balance += money
#         self.deposit_count += 1
#         if self.deposit_count % 5 == 0:
#             self.balance = int(self.balance * (1+0.01))

#     def withdraw(self, money):
#         if self.balance > money:
#             self.balance -= money
    
#     def display_info(self):
#         print('은행이름:', self.bank)
#         print('예금주:', self.name)
#         print('계좌번호:', self.account_number)
#         balanceStr = str(self.balance)[::-1]
#         myList = []
#         for i in range(0, len(balanceStr), 3):
#             myList.append(balanceStr[i:i+3])
#         balanceStr = ','.join(myList)[::-1]
#         print('잔고: {}원'.format(balanceStr))

#     @classmethod
#     def get_account_num(cls):
#         print('개설된 계좌 수 :',cls.account_count)

# myList = []
# myList.append(Account('홍길동', 10000000))
# myList.append(Account('황인국', 10000))
# myList.append(Account('박기태', 10000))
# for _obj in myList:
#     if _obj.balance >= 1000000:
#         _obj.display_info()

# 280번
# sol)
# from random import randint

# class Account:
#     account_count = 0
#     def __init__(self, name, balance):
#         self.deposit_log = [balance]
#         self.withdraw_log = []
#         self.deposit_count = 0
#         self.bank = "SC은행"
#         a1 = str(randint(100,999))
#         a2 = str(randint(10,99))
#         a3 = str(randint(100000,999999))
#         self.account_number =  a1 + '-' + a2 + '-' + a3
#         self.name = name
#         self.balance = balance
#         Account.account_count += 1

#     def deposit(self, money):
#         if money >= 1:
#             self.balance += money
#             self.deposit_count += 1
#             self.deposit_log.append(money)   
#             if self.deposit_count % 5 == 0:
#                 self.balance = int(self.balance * (1+0.01))
        
#     def withdraw(self, money):
#         if self.balance > money:
#             self.balance -= money
#             self.withdraw_log.append(money) 

#     def deposit_history(self):
#         print("<입금내역>")
#         print('='*10)
#         for v in self.deposit_log:
#             print("{}".format(v))
#         print('='*10)

#     def withdraw_history(self):
#         print("<출금내역>")
#         print('='*10)
#         for v in self.withdraw_log:
#             print("{}".format(v))
#         print('='*10)
    
#     def display_info(self):
#         print('은행이름:', self.bank)
#         print('예금주:', self.name)
#         print('계좌번호:', self.account_number)
#         balanceStr = str(self.balance)[::-1]
#         myList = []
#         for i in range(0, len(balanceStr), 3):
#             myList.append(balanceStr[i:i+3])
#         balanceStr = ','.join(myList)[::-1]
#         print('잔고: {}원'.format(balanceStr))

#     @classmethod
#     def get_account_num(cls):
#         print('개설된 계좌 수 :',cls.account_count)

# k = Account('kim', 1000)
# k.deposit(100)
# k.deposit(200)
# k.deposit(300)
# k.deposit_history()

# k.withdraw(100)
# k.withdraw(200)
# k.withdraw_history()

# k.display_info()