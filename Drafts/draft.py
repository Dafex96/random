equipos = ["Colo-Colo","Universidad de Chile","Universidad Catolica","Magallanes","Santiago Wanderers"]

equipos.append("Union Española")
####### Agrega al final de la lista

equipos.insert(1, "Huachipato")
####### Agrega en una poscicion especifica

equipos.remove("Universidad de Chile")
####### Elimina un elemento en especifico

equipos.reverse()
####### Invierte el orden de la lista

for i in equipos:
    print(i)