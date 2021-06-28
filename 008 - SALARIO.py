# -*- coding: utf-8 -*-
"""
SALÁRIO
Created on Sat Feb 22 18:28:55 2020

@author: Geisa
"""

FUNCION = int(input())
HORAST = int(input())
VALORH = float(input())

SALARY = HORAST * VALORH

print("NUMBER =", FUNCION,"\nSALARY = U$ {:.2f}".format(SALARY))

#ou

FUNCION = int(input())
HORAST = int(input())
VALORH = float(input())

SALARY = HORAST * VALORH

print("NUMBER =", FUNCION)
print("SALARY = U$ {:.2f}".format(SALARY))