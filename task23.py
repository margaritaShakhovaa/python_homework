# 23. Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

list = [2,3,4,5,6]
mult = 0

print (f'[{list[0]*list[4]}, {list[1]*list[3]}, {list[2]**2}]')
# for i in range(len(list)): # чтобы i принимала значение индексов
#     mult = list[i] * list [i - 1]
#     print (mult)