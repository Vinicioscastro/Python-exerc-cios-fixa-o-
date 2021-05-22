#PROBLEMA DO CAIXEIRO VIAJANTE
auxiliar = 0
#APENAS 4 CIDADES
print(' ')
print('===== TODAS AS ROTAS POSSIVEIS ======')
print(' ')

rota1 = ["A", "B", "C", "D", "A"]
rota2 = ["A", "B", "D", "C", "A"]
rota3 = ["A", "C", "B", "D", "A"]
rota4 = ["A", "C", "D", "B", "A"]
rota5 = ["A", "D", "B", "C", "A"]
rota6 = ["A", "D", "C", "B", "A"]

opcoes = [rota1, rota2, rota3, rota4, rota5, rota6]

for n in [0,1,2,3,4,5]:
    print('ROTA {} {}'.format(n+1, opcoes[n]))

print(' ')
print('===== DISTANCIA EM CADA ROTA ======')
print(' ')
distanciaRota1 = 6+3+4+5
distanciaRota2 = 6+2+4+1
distanciaRota3 = 1+3+2+5
distanciaRota4 = 1+4+2+6
distanciaRota5 = 5+2+3+1
distanciaRota6 = 5+4+3+6

distancias = [distanciaRota1, distanciaRota2, distanciaRota3, distanciaRota4, distanciaRota5, distanciaRota6]

for n in [0,1,2,3,4,5]:
        print ('rota {} tem as distancia {}'.format(opcoes[n], distancias[n]) )

print(' ')

print('==== MELHOR ROTA PARA O CASO =======')

auxiliar = distancias[0]

for i in [0,1,2,3,4,5]:
   
    if auxiliar > distancias[i]:
        auxiliar = distancias[i]

print('melhor opcao e a rota com a distancia {}'.format(auxiliar))

 