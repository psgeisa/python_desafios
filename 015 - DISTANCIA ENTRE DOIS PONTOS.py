# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:29:11 2020
DISTANCIA ENTRE DOIS PONTOS

1.0 7.0
5.0 9.0

@author: psgei
"""

pt1 = input().split()
X1 = float(pt1[0]) 
Y1 = float(pt1[1])

pt2 = input().split()
X2 = float(pt2[0]) 
Y2 = float(pt2[1])

pd =((X2 - X1)**(2) + (Y2 -Y1)**(2))**(0.5)

print('{:.4f}'.format(pd))