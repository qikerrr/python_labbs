n = int(input('in_1:'))
k0 = 0

for i in range(n):
    s = input(f'in_{i+2}: ') # вывод строк
    s0 = s.split(' ') # разделение по пробелам

    if s0[-1] == 'True': # проверяем последний элемент(очно.заочно)
        k0 +=1
    i += 1


print('out: ', k0, n-k0)