'''
Program: Flip the array
Date: 08.04.19
'''
a = [1, 2, 3, 4, 5, 6, 7]
b = [99, 99, 99, 99, 99, 99, 99]

for i in range(7): #Это ввод пользователем
    a[i] = input()

#for i in range(7): #Это он берет по умолчанию
#    print(a[i])

print('\n')

for i in range(7):
    if i == 0:
        b[i] = a[-1]
    else:
        b[i] = a[-(i + 1)]

for i in range(7):
    print(b[i])

#for i in range(7):  #Это он заменяет перевернутый массив в исходном
#    a[i] = b[i]
#for i in range(7):
#    print(a[i])