price = float(input('price = '))
discount = float(input('discount ='))
vat = float(input('vat = '))

base = price * (1 - discount/100)
vat_amount = base* (vat/100)
total = base + vat_amount

print('База после скидки:', f'{base:.2f}', '₽')
print('НДС:', f'{vat_amount:.2f}', '₽')
print('Итого к оплате:', f'{total:.2f}', '₽')
#используем f-строки, чтобы вывести 2 знака после запятой