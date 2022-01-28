numero = int(input('Digite um numero: '))
print('O antecessor e: {} e seu sucessor: {} '.format(numero-1, numero+1))
print('Dobro e: {} o triplo {} e sua raiiz: {} '.format(numero*2, numero*3, numero**(1/2)))

n = int(0)
# while n < 11:
   # print('Multiplicação: {} '.format(numero*n))
   # n = n+1

altura = float(input("Digite a altura: "))
largura = float(input("Digite a largura² "))
tinta = float((altura*largura))
if tinta%2==0:
     print("Serão necessaarias {} latas de tintas".format(tinta/2))
else:
       print("Serão necessaarias {} latas de tintas".format((tinta//2)+1))  