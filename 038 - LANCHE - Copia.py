# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 20:44:31 2020

@author: psgei
"""
Cod, Qtd = input().split()
Cod, Qtd = float(Cod), float(Qtd)
valor = 0

if Cod == 1:
    valor = 4.0 * Qtd
elif Cod == 2:
    valor = 4.5 * Qtd
elif Cod == 3:
    valor = 5.0 * Qtd
elif Cod == 4:
    valor = 2.0 * Qtd
elif Cod == 5:
    valor = 1.5 * Qtd

print("Total: R$ %.2f" %valor)