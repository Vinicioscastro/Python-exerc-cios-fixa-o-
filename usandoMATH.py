import math
num = int(input("digite o angolo: "))
num = math.radians(num)

print('O seno: {} \n o cosseno: {} \n a tangente: {} '.format(math.sin(num), math.cos(num), math.tan(num)))

catop = int(input("Digite o Catop: "))
catad = int(input("digite o catad: "))

#catop = math.radians(catop)
#catad = math.radians(catad)

print("A hipotenusa e: {} ".format(math.hypot(catop,catad)))