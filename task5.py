# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

print ('Введите любое целое число:')
a = int(input())

b = 5
c = 10
d = 15
e = 30

if a % b == 0 and a % c == 0:
    print (f'Число {a} кратно 5 и 10')
elif a % d == 0:
    print (f'Число {a} кратно 15')
if a % e != 0:
    print (f'Число {a} не кратно 30')