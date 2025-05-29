from test import menu

menu()


option = 0
valor_1 = 0
valor_2 = 0
answer = 0 


while option < 5:
    
    if option == 1:
        print("Esta sumando")
        valor_1 = int(input("Ingrese el primer valor: "))
        valor_2 = int(input("Ingrese el segundo valor: "))
        answer = valor_1 + valor_2
        print(f"El resultado es: {answer}")
        menu()
        option = int(input("Ingrese una opcion"))
        
    elif option == 2:
        print("Esta restando")
        valor_1 = int(input("Ingrese el primer valor: "))
        valor_2 = int(input("Ingrese el segundo valor: "))
        answer = valor_1 - valor_2
        print(f"El resultado es: {answer}")
        menu()
        option = int(input("Ingrese una opcion"))
        
    elif option == 3:
        print("Esta multiplicando")
        valor_1 = int(input("Ingrese el primer valor: "))
        valor_2 = int(input("Ingrese el segundo valor: "))
        answer = valor_1 * valor_2
        print(f"El resultado es: {answer}")
        menu()
        opcion = int(input("Ingrese una opcion"))
        
    elif option == 4:
        print("Esta dividiendo")
        valor_1 = int(input("Ingrese el primer valor: "))
        valor_2 = int(input("Ingrese el segundo valor: "))
        answer = valor_1 / valor_2
        print(f"El resultado es: {answer}")
        menu()
        option = int(input("Ingrese una opcion"))
        
    else:
        
        print("Opcion ingresada no valida")
        
    option = int(input("Ingrese la opcion: "))