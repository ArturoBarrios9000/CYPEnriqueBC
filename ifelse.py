EDAD = int(input("Dame tu edad;"))
INE = bool(int (input("Tienes INE (0 No / 1 Si)?:")))

if EDAD>= 18 and INE == True:
    print("ES mayor de edad")
    print("Puede entrar al Bar")
else:
    print("Eres menor de edad")
    print("Puedes jugar League of Draven")
print("Fin del programa")
