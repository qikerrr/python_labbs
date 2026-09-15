s = input()
res = ''
ch = '0123456789' # список для проверки является элементом числом или нет
k = 0
ind1 = 0
ind2 = 0

for i in range(len(s)): # цикл для нахождения первой заглавной буквы и добавления ее в список результата
    if s[i].isupper() == True:
        res += s[i]
        ind1 = i
        break

for j in range(ind1, len(s)-1): # цикл, чтобы найти вторую буквы и узнать шаг, чтобы собрать сообщение до конца
    k += 1
    if s[j] in ch:
        res += s[j+1]
        ind2 = j+1
        shag = abs(ind1 - ind2)
        break

for e in range(ind2, len(s)-shag, shag): #цикл, чтобы закончить сообщение. начинаем со второго элемента и дальше с известным шагом
    res += s[e+shag]

print(res)



