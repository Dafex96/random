print("--Clasificacion de numeros--")

for i in range(1, 21):
    
    if i % 3 == 0 and i % 5 == 0:     # El % es para obtener el resto de una division entre 2 numeros.
        
        print(f"{i} es multiplo de 3 y 5")
        
    elif i % 3 == 0:
        
        print(f"{i} es multiplo de 3")
        
    elif i % 5 == 0:
        
        print(f"{i} es multiplo de 5")
        
    else:
        
        print (f"{i} no es multiplo de 3 ni de 5")