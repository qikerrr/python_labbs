def format_record(s):

    if type(s) != tuple: return 'TypeError = не тот тип данных'
    if len(s) != 3: return 'ValueError = введены не все данные'
    if s[0] == '' or s[1] == '': return 'ValueError = пустые данные'
    if type(s[2]) != float: return 'TypeError = неверный тип GPA'

    fio1 = s[0]
    group = s[1]
    gpa = s[2]
    res =''
    if not(0.0 <= gpa <= 5.0): return 'ValueError = неверный gpa'

    fio2 = fio1.split(" ")
    fio = ''
    for i in range(len(fio2)):

        if len(fio) == 0 and fio2[i] != "":
            clovo1 = fio2[i]
            fio = fio +  (clovo1[0]).upper() + clovo1[1:] + ' '
            continue

        if fio2[i] != "":
            clovo = fio2[i]
            fio = fio + (clovo[0]).upper() + '.'
            
    res = '"' + fio  + ',' + ' ' + 'гр.' + ' ' + group + ',' + ' ' +'GPA' + ' ' + f'{gpa:.2f}' + '"'
    return res

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
    