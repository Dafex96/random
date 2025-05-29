

def calcular(num1,num2,opcion):
    if opcion == 1:
        return num1+num2
    elif opcion == 2:
        return num1-num2
    elif opcion == 3:
        return num1*num2    
    elif opcion == 4:
        while num2 == 0:
            print("!!!No se puede dividir por cero")
            num2=int(input("Vuelva a ingresa el divisor: "))
        resultado = num1 / num2
        resultado_redondeado = round(resultado,2)
        return resultado_redondeado
    elif opcion == 5:
        return num1**num2
    
def menu():
    print("Calculadora")

    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Salir")
