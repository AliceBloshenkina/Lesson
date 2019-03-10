
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

for i in range(9, 100, 10):
    # di[i] = i ** 2
    test_value = {i: i ** 2}
    di.update(test_value)

print(di)









