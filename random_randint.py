from random import randint
#                  randint= genera un numero aleatorio dentro de una serie de numeros (n1, n2)
#    random = modulo dentro de python con funciones relacionadas con numeros aleatoros

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))

num = randint(n1,n2)

print(f"El numero random es: {num}")

if num % 2 == 0:
    print(f"{num} es par")
else:
    print(f"{num} no es par")