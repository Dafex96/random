print("--Tabla--")

numero = int(input("Ingrese un numero para ver su tabla: "))

for i in range(1, 11):     # La "i" es para darle el nombre a la variable.
    
    print(f"{numero} X {i} = {numero * i}")