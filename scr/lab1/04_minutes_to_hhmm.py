m = int(input('Минуты: '))
mine = m//60
sek = m - (m//60)*60
print(mine,':',sek, sep = '')