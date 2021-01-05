

# untuk mengetahui bilangan genap dan ganjil di list angka

print('\n')
list = [1,2,3,4,5,6,7,8,9,10]   # list

print('list : 1,2,3,4,5,6,7,8,9,10\n')

print('bilangan genap : ', end='')   # bilangan genap
for i in list:
    if i % 2 == 0 :
        print(i,'', end='')

print("\n")
print('bilangan ganjil : ', end='')   # bilangan ganjil
for x in list:
    if x % 2 == 1 :
        print(x,'', end='')

print('\n')