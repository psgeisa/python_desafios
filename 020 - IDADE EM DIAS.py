# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:44:29 2020

@author: psgei

IDADE EM DIAS, MES E ANO

"""

Seus_dias = int(input())

Sua_idade = Seus_dias//365
Sobra = Seus_dias%365

Seus_meses = Sobra//30
Dias = Sobra%30

print(Sua_idade,"ano(s)")
print(Seus_meses,"mes(es)")
print(Dias,"dia(s)")
