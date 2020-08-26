# Ordem de precedência 
# ()
# **
# * / // %
# + -

n1 = int(input('digite um nomer0: '))
n2 = int(input('digite um nomer0: '))

s= n1+n2
m = n1*n2
di = n1//n2
rd = n1%n2
p = n1**n2

print('a soma e: {} a multiplicação: {} a divisão inteira: {}'.format(s,m,di), end=' >> ')
print('O resto da divisão: {} e a potencia: {} '.format(rd, p))