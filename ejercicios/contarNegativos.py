print("--Contador de numeros negativos--")

#[int(num) for num in ... Convierte cada subcadena en un número entero usando una list comprehension.

numeros = [int(num) for num in input("Introduzca una lista de numeros negativos separados por un espacio: ").split()]

#.split(): Divide la cadena ingresada por el usuario en una lista de subcadenas usando el espacio como delimitador.

contador = 0

for numero in numeros:
    if numero < 0:
        contador += 1


print(f"Hay {contador} numeros negativos en la lista.")