#AREA DE UM TRIANGULO E UM TRAPEZIO
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if abs(b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    tria = (a + b + c)
    print("Perimetro =", tria)
else:
    print("Area = {:.1f}".format(((a + b) / 2) * c))