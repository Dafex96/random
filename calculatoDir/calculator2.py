from test import menu,calcular

menu()

opcion = int(input("Ingrese una opcion: "))

while opcion > 0 and opcion < 6:
    
    num1 = int(input("Ingrese el primero numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    
    resultado = calcular(num1,num2,opcion)
    
    print(f"El resultado es: {resultado}")
    
    menu()
    
    opcion = int(input("Ingrese una opcion: "))
    
print("Gracias, hasta luego")