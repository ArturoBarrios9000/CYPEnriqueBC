MAT=int(input("Introduzca numero de matricula del alumno:"))
CAL1=float(input("Introduzca la primera calificacion:"))
CAL2=float(input("Introduzca la segunda calificacion:"))
CAL3=float(input("Introduzca la tercera calificacion:"))
CAL4=float(input("Introduzca la cuarta calificacion:"))
CAL5=float(input("Introduzca la quinta calificacion:"))
PRO=(CAL5+CAL4+CAL3+CAL2+CAL1)/5
if PRO>=6:
    print(f"El alumno con matricula {MAT} tiene un promedio de {PRO}, por lo tanto esta aprobado")
else:
    print(f"El alumno con matricula {MAT} tiene un promedio de {PRO}, por lo tanto esta reprobado")
