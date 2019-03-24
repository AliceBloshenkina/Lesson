
"""lst = [1, 'gt', 65, 87]

for index, item in enumerate(lst):
    # print(index, item)
    if isinstance(item, int):
        lst[index] = item ** 2
        # print('TEST OK!', item)

print(lst) """

'''lst = []

for i in range(100):
    lst.append(i**2)
print(lst)'''


# for i in range(2, 10):
#     print(i)


di = {}

'''for i in range(9, 100, 10):
    # di[i] = i ** 2
    test_value = {i: i ** 2}
    di.update(test_value)

print(di)'''

# for (var i; i <= 10; i++) {
#     ...
# }


p = 10
# for i in range(10):
#     print(i)

'''i = 1
b = True

while b:
    print(i)
    i += 1

    if i == 10:
        b = False'''
#
# for item in range(1000):
#     try:
#         if item < 990:
#             continue
#         elif item.sfefsdf ** '997':
#             break
#         else:
#             print(item)
#     except Exception:
#         print('qsd')
#         break
    # except AttributeError as e:
    #     print(item, 'Jib,rf')
    #     continue
    # except TypeError as aa:
    #     print(item, 'Jhftygf')
    #     continue
    #
    # print(e, aa)


# def add(x, y):
#     return x ** 2 + y ** 2
#
#
# print(add(10, 13))
#
#
# def check_result(x):
#     if x % 2 == 0:
#         print(x)
#
#
# print(range(1000))
#
# for i in range(1000):
#     check_result(i)

# import time
#
#
# print(time.ctime())
#
# time.sleep(5)
# print('Ytllo')

# x = 5


# def tmt(x):
#     for i in x:
#         print(time.ctime)
#         time.sleep(5)

# for i in range(100):
#     Tmt(x)

'''
    TODO:
    1 - Импортировать библиотека time
    2 - Функция, которая отдает время 
    3 - Цикл, выполняемый пять раз 
    4 - Ждем пять секунд после каждого элемента цикла
'''

# import time
#
#
# def tmt(i):
#     while i <= 5:
#         print(time.ctime())
#         time.sleep(5)
#         i += 1
#
# tmt(1)

k = 2
def er(i):
     m = 2
     while m <= i:
         k = 2
         count = 0
         while k <= m-1:
             if m % k == 0:
                 count += 1
         k += 1
         if count == 0:
             print(m)
     m += 1

er(30)
















