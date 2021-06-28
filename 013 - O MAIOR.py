# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:49:57 2020

O MAIOR

7 14 106
217 14 6
@author: psgei

Maior = (a + b + abs(a-b))/2
"""
a, b, c = [int(x) for x in input().split()]

Maior = max(a, b, c)

print(int(Maior), "eh o maior")