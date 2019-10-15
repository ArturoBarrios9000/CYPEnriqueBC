CLA=int(input("Ingrese la clave de la zona geografica a la que se llamo:"))
NUMIN=int(input("Ingrese la duracion de la llamada (en minutos sin segundos):"))
if CLA == 12:
    COST=NUMIN*2
    print(f"El costo total de la llamada es {COST}")
elif CLA == 15:
    COST=NUMIN*2.2
    print(f"El costo total de la llamada es {COST}")
elif CLA == 18:
    COST=NUMIN*4.5
    print(f"El costo total de la llamada es {COST}")
elif CLA == 19:
    COST=NUMIN*3.5
    print(f"El costo total de la llamada es {COST}")
elif CLA == 23:
    COST=NUMIN*6
    print(f"El costo total de la llamada es {COST}")
elif CLA == 25:
    COST=NUMIN*6
    print(f"El costo total de la llamada es {COST}")
elif CLA == 29:
    COST=NUMIN*5
    print(f"El costo total de la llamada es {COST}")
else:
    print("Ingrese el numero correcto de la clave geografica")
print("FIN")
