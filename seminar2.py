# 1. Найти третью цифру числа или сообщить, что её нет
# 2. Программа проверяет пятизначное число на палиндромом
# 3. Дано число. Проверить кратно ли оно 7 и 23
# 4. Проверить истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y
# 5. Определить номер четверти плоскости, в которой находится точка с координатами Х и У, причем X ≠ 0 и Y ≠ 0
# 6. Дано число обозначающее день недели. Выяснить является номер дня недели выходным



# 1. Найти третью цифру числа или сообщить, что её нет
# Мое решение
# num = int(input('Введите число: '))
# while num >= 1000:
#     num = num//10
# if num < 100:
#     print ('Третьей цифры нет')
# else:
#     print (num % 10)

# Решение с учетом отрицательных и положительных чисел
# num = input('Введите число: ')
# if int(num) < 0:
#     num = str(int(num) * -1)
# if int(num) >= 0:
#     if len(num) < 3:
#         print ('Третьей цифры нет')
#     else:
#         print (num[2])



# 2. Программа проверяет пятизначное число на палиндромом
# 1 вариант решения:
# num = input('Введите пятизначное число: ')
# if int(num) < 0:
#     num = str(int(num) * -1)
# if num[0] == num[4] and num[1] == num[3]:
#     print(f'Число {num} является палиндромом')
# else:
#     print (f'Число {num} не является палиндромом')

# 2 вариант решения:
# num = input('Введите пятизначное число: ')
# reverse_num = ''
# for i in reversed(num): # перебирает каждый символ в обратном порядке
#     reverse_num += i
# if num == reverse_num:
#     print(f'Число {num} является палиндромом')
# else:
#     print (f'Число {num} не является палиндромом')

# 3 вариант решения:
# num = input('Введите пятизначное число: ')
# if num == num[::-1]: # берем срез, от крайнего левого до крайнего правого элемента ([:]) и идем по элементам в обратном порядке (:-1)
#     print(f'Число {num} является палиндромом')
# else:
#     print (f'Число {num} не является палиндромом')