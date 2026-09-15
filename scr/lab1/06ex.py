n = int(input())
k0 = 0

for i in range(n):
    s = input() # вывод строк
    s0 = s.split(' ') # разделение по пробелам

    if s0[-1] == 'True': # проверяем последний элемент(очно.заочно)
        k0 +=1


print('out: ', k0, n-k0)