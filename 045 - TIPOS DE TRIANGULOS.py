,#multiplos
a, b, c = input().split()
list = [a, b, c]
if a < b:
    var = a
    a = b
    b = var

if a < c:
    var = a
    a = c
    c = var

if b < c:
    var = b
    b = c
    c = var
print(a, b, c)

    if a >= b + c:
        print("NAO FORMA TRIANGULO")
    elif a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
        print("TRIANGULO ISOSCELES")
    elif a == b == c:
        print("TRIANGULO EQUILATERO")
    else:
        print("TRIANGULO ISOSCELES")

"""
if a >= b + c:
    print("NAO FORMA TRIANGULO")
elif a**2 == b**2 + c**2:
    print("TRIANGULO RETANGULO")
elif a**2 > b**2 + c**2:
    print("TRIANGULO OBTUSANGULO")
elif a**2 < b**2 + c**2:
    print("TRIANGULO ACUTANGULO")
    print("TRIANGULO ISOSCELES")
elif a == b == c:
    print("TRIANGULO EQUILATERO")
else:
    print("TRIANGULO ISOSCELES")
"""
