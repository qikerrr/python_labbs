s = input()
res = ''
ch = '0123456789'
k = 0
ind1 = 0
ind2 = 0

for i in range(len(s)):
    if s[i].isupper() == True:
        res += s[i]
        ind1 = i
        break

for j in range(ind1, len(s)-1):
    k += 1
    if s[j] in ch:
        res += s[j+1]
        ind2 = j+1
        break

for e in range(ind2, len(s)-2):
    while s[e] != 0:
        res += s[i+2]

print(res)



