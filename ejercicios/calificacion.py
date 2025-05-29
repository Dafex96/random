print("--Calificaciones de estudiantes--")

nota = int(input("Introduzca la puntuacion del estudiante: "))

if nota >= 90:
    print("Calificacion: A")
elif nota >= 80:
    print("Calificacion: B")
elif nota >= 70:
    print("Calificacion: C")
elif nota >= 60:
    print("Calificacion: D")
else:
    print("Calificacion: F")
    print("¡REPOBASTE!")