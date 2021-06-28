# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:46:40 2020
3.0 4.0 5.2
12.7 10.4 15.2
@author: psgei

a, b, c = [float(x) for x in input().split()]

ou
"""
A, B, C = input().split()
A = float(A) 
B = float(B)
C = float(C)

pi = 3.14159

print("TRIANGULO: {:.3f}".format((A * C)/2))
print("CIRCULO: {:.3f}".format(pi * (C * C)))
print("TRAPEZIO: {:.3f}".format(((A+B)*C)/2))
print("QUADRADO: {:.3f}".format(B ** 2))
print("RETANGULO: {:.3f}".format(A * B))
