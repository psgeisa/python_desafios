# -*- coding: utf-8 -*-
"""
SALÁRIO COM BONUS
Created on Sat Feb 22 18:28:55 2020

@author: Geisa
"""

NomeV = (input())
SalaF = float(input())
VendT = float(input())

SALARY = (VendT * 0.15) + SalaF

print("TOTAL = R$ {:.2f}".format(SALARY))