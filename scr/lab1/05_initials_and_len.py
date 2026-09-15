login = input('ФИО: ')
l2 = login.split(' ')

print(l2)


s = 0
ini = ''

for i in range(len(l2)):
    if len(l2[i]) != 0:
        s += len(l2[i])
        clovo = l2[i]
        ini += clovo[0]


print('ФИО: ', ' '.join(l2))
print('Инициалы: ', ini.upper())
print('Длина (символов):', s+2)