m = int(input('Минуты: '))
mine = m//60
sek = m - (m//60)*60
print(f'{mine}.{sek:02d}')
