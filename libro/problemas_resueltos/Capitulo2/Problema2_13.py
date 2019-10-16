MAT=int(input("Ingrese la matricula del alumno:"))
CARR=int(input("Ingrese la carrera del alumno ( 1 Economia, 2 Computacion, 3 Administracion, 4 Contabilidad):"))
SEM=int(input("Ingrese el semestre aprobado del alumno:"))
PRO=float(input("Ingrese el promedio del almno:"))
if CARR == 1:
    if SEM>=6:
        if PRO>=8.8:
            print(f"El alumno con matricula {MAT} esta aceptado")
elif CARR ==2:
    if SEM>=5:
        if PRO>=8.5:
            print(f"El alumno con matricula {MAT} esta aceptado")
elif CARR== 3:
    if SEM>=5:
        if PRO>=8.5:
            print(f"El alumno con matricula {MAT} esta aceptado")
elif CARR== 4:
    if SEM>=5:
        if PRO >=8.5:
            print(f"El alumno con matricula {MAT} esta aceptado")
print("FIN")
