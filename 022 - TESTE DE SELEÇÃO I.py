# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:04:01 2020

@author: psgei


a, b, c, d = [int(x) for x in input().split()]

if (b<c):
    print("Valores nao aceitos1")
else:
    if (c<a):
        print("Valores nao aceitos2")
    else:
        if (c+d)<(a+b):
            print("Valores nao aceitos3")
        else:
            if (c and d<0):
                print("Valores nao aceitos4")
            else:
                if (a%2)!= 0:
                    print("Valores nao aceitos5")
                else:
                    print("Valores aceitos")

a, b, c, d = [int(x) for x in input().split()]

if (b<c) and (c<a):
    print("Valores nao aceitos")
else:
    if (c+d)<(a+b):
        print("Valores nao aceitos")
    else:
        if (c and d<0):
            print("Valores nao aceitos")
        else:
            if (a%2)!= 0:
                print("Valores nao aceitos")
            else:
                print("Valores aceitos")

a, b, c, d = [int(x) for x in input().split()]

if b > c and d > a and (c + d) > (a + b) and (c >= 0) and (d >= 0) and (a % 2) == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

"""

a, b, c, d = [int(x) for x in input().split()]

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')