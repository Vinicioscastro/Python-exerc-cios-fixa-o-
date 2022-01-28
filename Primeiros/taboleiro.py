#nome = input("digite seu nome: ")
#idade = int(input("digite sua idade: "))

#print("Seja bem vindo {} de {} anos de idade".format(nome, idade))

#j= nome == idade
#print(j)

numero = int(21)

x = numero
sorte = int(input("Digite o numero: "))
while(sorte != x):
    #print(x)
    #x = x-1

    

    if numero == sorte:
        print("acertou")
    else:
        if numero < sorte:
            print("Seu numero foi depois")
        else:
            print('seu numero foi antes')
    sorte = int(input("Digite o numero: "))        
print('fim')
