# -*- coding: utf-8 -*-
"""
CALCULO SIMPLES

Created on Sat Feb 22 18:28:55 2020

@author: Geisa
"""

linha1 = input().split()
C1 = int(linha[0])
N1 = int(linha[1])
V1 = float(linha[2])

linha2 = input().split()
C2 = int(linha[0])
N2 = int(linha[1])
V2 = float(linha[2])

VT = (N1*V1) + (N2*V2)

print("VALOR A PAGAR: R$ {:.2f}".format(VT))

#ou

C1, N1, V1 = input().split()
C2, N2, V2 = input().split()
C1 = int(C1)
N1 = int(N1)
V1 = float(V1)
C2 = int(C2)
N2 = int(N2)
V2 = float(V2)

VT = (N1*V1) + (N2*V2)

print("VALOR A PAGAR: R$ {:.2f}".format(VT))