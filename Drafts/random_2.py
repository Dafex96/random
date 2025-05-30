from random import randint

while True:
    n1 = int(input("Ingrese un numero: "))
    if n1 == 0:
        break
    n2 = int(input("Ingrese un numero: "))
    if n2 == 0:
        break
    
    num = randint(n1,n2)
    #Elije un numero aleatorio entre el n1 y n2.
    
    print(f"El numero aleatorio es: {num}")
    
    if num % 2 == 0:
        print(f"{num} es par")
    else:
        print(f"{num} es impar")

#####--El segundo numero no puede ser menor al primero--#####


# n1 = int(input("Ingrese un numero: "))
# n2 = int(input("Ingrese un numero: "))

# num = randint(n1,n2)

# print(f"El numero random es: {num}")

