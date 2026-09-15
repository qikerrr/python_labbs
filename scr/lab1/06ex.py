n = int(input())
k0 = 0

for i in range(n):
    s = input()
    s0 = s.split(' ')

    if s0[-1] == 'True':
        k0 +=1


print('out: ', k0, n-k0)