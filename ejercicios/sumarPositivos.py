suma = 0

while True:    # while True: Bucle de manera infinita hasta que se ejecute el Break.
    numero = int(input("Introduzca un numero (negativo para terminar): "))
    if numero < 0:
        break  # Termina el while.
    suma += numero 

print(f"La suma de los numeros positivos es: {suma}")