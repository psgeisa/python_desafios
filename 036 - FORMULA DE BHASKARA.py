"""
por: Geisa Souza
"""

#Fórmula de Bhaskara x = (-b) + or -
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

if a == 0:
    print("Impossivel calcular")
else:
    num = (b**2) - 4 * a * c
    if num <0:
        print("Impossivel calcular")
    else:
        x1 = (-b + num ** (1/2))/(2*a)
        x2 = (-b - num ** (1/2))/(2*a)
        print("R1 = %.5f" %x1)
        print("R2 = %.5f" %x2)
