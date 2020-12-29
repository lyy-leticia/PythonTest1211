# a = set('abracadabra')#set（）建集合
# b = set('abrfghhrra')
# print(a)
# t=a ^ b  # 在 a 或 b 中的字母，但不同时在 a 和 b 中
# print(t)   

# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

# b=dict(sape=4139, guido=4127, jack=4098)
# print(b)

# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k,v in knights.items():
#     print(k,v)

# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print(q,a)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):#转元祖，排序，for循环遍历打印
    print(f)