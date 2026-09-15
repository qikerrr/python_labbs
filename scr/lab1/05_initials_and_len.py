login = input('ФИО: ')
l2 = login.split(' ')

s = 0
ini = ''
res = []

for i in range(len(l2)):
    if len(l2[i]) > 1:
        s += len(l2[i])
        clovo = l2[i]
        ini += clovo[0]


print('Инициалы: ', ini.upper())
print('Длина (символов):', s+2)