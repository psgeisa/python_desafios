"""
#If, else, elif
x, y = input().split()
x = float(x)
y = float(y)

if x == y == 0:
    print("Origem")

elif x > 0 and y > 0:
    print("Q1")
elif x < 0 and y > 0:
    print("Q2")

elif x < 0 and y < 0:
    print("Q3")
elif x > 0 and y < 0:
    print("Q4")

elif y == 0 and x > 0 or x <0:
    print("Eixo X")
elif x == 0 and y > 0 or y <0:
    print("Eixo Y")

#If & else
x, y = input().split()
x = float(x)
y = float(y)

if x > 0 and y > 0:
    print("Q1")
else:
    if x < 0 and y > 0:
        print("Q2")
    else:
        if x < 0 and y < 0:
            print("Q3")
        else:
            if x > 0 and y < 0:
                print("Q4")
            else:
                if y == 0 and x > 0 or x <0:
                    print("Eixo X")
                else:
                    if x == 0 and y > 0 or y <0:
                        print("Eixo Y")
                    else:
                        print("Origem")
"""