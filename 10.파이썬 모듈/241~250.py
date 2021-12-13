# 241번
# sol)
# import datetime
# print(datetime.datetime.now())

# 242번
# sol)
# import datetime
# now = datetime.datetime.now()
# print(now, type(now))

# 243번
# sol)
# import datetime

# now = datetime.datetime.now()

# for day in range(5,0,-1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)

# 244번
# sol)
# import datetime
# now = datetime.datetime.now()
# a = now.strftime(r"%Y-%m-%d %H:%M:%S")
# print(a, type(a))

# 245번
# sol)
# import datetime
# date = datetime.datetime.strptime("2020-05-04",r"%Y-%m-%d")
# print(date, type(date))

# 246번
# sol)
# import time
# import datetime

# while True:
#     print(datetime.datetime.now())
#     time.sleep(1)

# 247번
# sol)
# import 모듈, from 패키지 import 모듈, from 모듈 import *, from 패키지.모듈 import *

# 248번
# import os
# ret = os.getcwd()
# print(ret, type(ret))

# 249번
# sol)
# import os
# os.rename(r"C:/Users/jmk360/Desktop/before.txt", r"C:/Users/jmk360/Desktop/after.txt")

# 250번
# sol)
# import numpy as np
# np_data = np.arange(0, 5.1, 0.1)
# print(np_data)