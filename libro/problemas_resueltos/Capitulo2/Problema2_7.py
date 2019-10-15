A=int(input("Ingrese un numero entero para A:"))
B=int(input("Ingrese un numero entero para B:"))
C=int(input("Ingrese un numero entero para C:"))
if A<B:
    if B<C:
        print("Los numeros estan en orden creciente")
    else:
        print("Los numeros no estan en orden creciente")
else:
    print("Los numeros no estan en orden creciente")
print("FIN")
