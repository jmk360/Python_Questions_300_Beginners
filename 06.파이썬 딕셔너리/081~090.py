# 81번
# sol)
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# *valid_score, _, _ = scores
# print(valid_score)

# 82번
# sol)
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# _, _, *valid_score = scores
# print(valid_score, type(valid_score))

# 83번
# sol)
# scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
# _, *valid_score, _ = scores
# print(valid_score, type(valid_score))

# 84번
# sol)
# temp = {}

# 85번
# sol)
# myDict = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
# print(myDict)

# 86번
# sol)
# myDict = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
# myDict['죠스바'] = 1200
# myDict['월드콘'] = 1500
# print(myDict)


# 87번
# sol)
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# print(ice.get('메로나'))

# 88번
# sol)
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}
# ice['메로나'] = 1300
# print(ice)

# 89번
# sol)
# ice = {'메로나': 1000,
#        '폴로포': 1200,
#        '빵빠레': 1800,
#        '죠스바': 1200,
#        '월드콘': 1500}

# del ice['메로나']
# print(ice)

# 90번
# sol)
# icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# icecream['누가바']
# '누가바' 라는 키가 없기 때문에 에러가 난다.