# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

ist = [ [0,0,0],
        [0,0,1],
        [0,1,1],
        [1,0,0],
        [1,1,0],
        [1,0,1],
        [1,0,1],
        [1,1,1]]

for i in ist:
    if (not (i[0] or i[1] or i[2])) == ((not i[0]) and (not i[1]) and (not i[2])):
        print('Истина')
    else:
        print('Ложь')