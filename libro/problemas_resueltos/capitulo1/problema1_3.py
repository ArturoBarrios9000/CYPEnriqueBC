NOM = str(input("Nombre del dinosaurio:"))
PES = float(input("Ingrese el peso del dinosaurio en toneladas:"))
LON = float(input("Ingrese la longuitud del dinosaurio en pies:"))
PESKIL = PES * 1000
LONMET = 0.3047 * LON
print(f"El dinosaurio {NOM} pesa {PESKIL}kg y mide {LONMET}m.")
