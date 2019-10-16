ENF=int(input("Ingrese el tipo de enfermedad del paciente:"))
EDAD=int(input("Ingrese la edad del paciente:"))
DIAS=int(input("Ingrese los dias que el paciente estuvo hospitalizado:"))
if ENF==1:
    COSTOT= DIAS*25
elif ENF==2:
    COSTOT=DIAS*16
elif ENF==3:
    COSTOT=DIAS*20
elif ENF==4:
    COSTOT=DIAS*32

if EDAD>=14:
    if EDAD<=22:
        COSTOT=COSTOT*1.1
print(f"El costo de la intenacion del paciente es de: {COSTOT}")
