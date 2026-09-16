m = int(input('Минуты: '))
mine = m//60
sek = m - (m//60)*60
if sek >= 10:
    print(mine,':',sek, sep = '')
else:
    print(mine,':','0', sek, sep = '')
# используем sep, чтобы вывести без пробелов 