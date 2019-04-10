'''
TODO:
      1.Open file
      2.Copy informaion to another file
      3.Close file
'''

a = ['ju', 'fd', 'df', 'sf', 'safro', 'se', 'sdv', 'f', 'efI', 'WER', 'U']

file_1 = open('File1.txt', 'r')
file_2 = open('File2.txt', 'a')

for i in range(10):
    a[i] = str(file_1.read())

for i in range(10):
    file_2.write(a[i])

file_1.close()
file_2.close()