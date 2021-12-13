# 291번
# sol)
# with open(r'C:\Users\jmk360\Desktop\매수종목1.txt', 'w') as f:
#     f.write('005930\n')
#     f.write('005380\n')
#     f.write('035420\n')

# 292번
# sol)
# with open(r"C:\Users\jmk360\Desktop\매수종목2.txt", 'w') as f:
#     f.write("005930 삼성전자\n")
#     f.write("005380 현대차\n")
#     f.write("035420 NAVER\n")

# 293번
# sol)
# import csv

# with open(r"C:\Users\jmk360\Desktop\매수종목.csv", 'w', encoding='cp949', newline='') as f:
#     writer = csv.writer(f)
#     writer.writerow(["종목명", "종목코드", "PER"])
#     writer.writerow(["삼성전자", "005930", 15.59])
#     writer.writerow(["NAVER", "035420", 55.82]) 

# 294번
# sol)
# myList = []
# with open(r"C:\Users\jmk360\Desktop\매수종목1.txt", 'r') as f:
#     for line in f:
#         myList.append(line.strip())
# print(myList)

# 295번
# sol)
# myDict = {}
# with open(r"C:\Users\jmk360\Desktop\매수종목2.txt", 'r') as f:
#     for line in f:
#         code, name = line.strip().split()
#         myDict[code] = name
# for k, v in myDict.items():
#     print(k, v)

# 296번
# sol)
# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print(0)

# 297번
# sol)
# per = ["10.31", "", "8.00"]
# myList = []
# for i in per:
#     try:
#         myList.append(float(i))
#     except:
#         myList.append(0)
# print(myList)

# 298번
# sol)
# try:
#     a = 5 / 0
# except ZeroDivisionError:
#     print('ZeroDivisionError')

# 299번
# sol)
# data = [1, 2, 3]

# for i in range(5):
#     try:
#         print(data[i])
#     except IndexError as e:
#         print(e)

# 300번
# sol)
# from os import error

# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print('except occured!!')
#     else:
#         print('else occured!!')
#     finally:
#         print('finally occured!!')