print("Si la expresion Ax^2+Bx+C=0")
A=float(input("Introdusca un valor numerico para A:"))
B=float(input("Introdusca un valor numerico para B:"))
C=float(input("Introdusca un valor numerico para C:"))
DIS=(B**2)-4*(A*C)
if DIS>=0:
    X1=((-B)+(DIS**0.5))/(2*A)
    X2=((-B)-(DIS**0.5))/(2*A)
    print(f"Las raices reales son {X1} y {X2}")
