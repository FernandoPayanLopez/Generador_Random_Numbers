import random

print("Bienvenido al Generador de numeros")
print("Seleccione el modo de uso")
print("1.- Manual")
print("2.- Aleatorio")
NUM = int(input("Ingrese su opción: ")) #Selcción del Modo
if(NUM==1):
    N = int(input("Ingrese la cantidad de numeros a generar: "))
    i = int(0)
    while i < N:
        print(i+1 , ".-" , random.random())
        i += 1
elif (NUM==2):
     M = int(random.randint(1, 1000))
     print("Numero generado aleatoriamente: " , M)
     i = int(0)
     while i < M:
        print(i+1 , ".-" , random.random())
        i += 1
else:
    print("Numero invalido")