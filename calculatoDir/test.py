def menu():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divide")
    print("5. Quit")

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