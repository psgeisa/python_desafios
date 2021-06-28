# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:55:11 2020
GASTO EM COMBUSTIVEL

@author: psgei


TG = int(input()) #tempo gasto
VM = int(input()) #velocidade média

KM = TG * VM  #Kilometragem

LT = (KM / 12) #Litros

print(round(LT,3))

"""

TG = int(input()) #tempo gasto
VM = int(input()) #velocidade média

KM = TG * VM  #Kilometragem

LT = (KM / 12) #Litros

print('{:.3f}'.format(LT))
