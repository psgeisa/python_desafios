# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 16:14:24 2020

@author: psgei
"""

RS = int(input())

cedulas = [100,50,20,10,5,2,1]

print(RS)
for cedula in cedulas:
    qtd_cedulas = int(RS / cedula)
    print("{:.0f} nota(s) de R$ {},00".format(qtd_cedulas, cedula))
    RS -= qtd_cedulas * cedula
    