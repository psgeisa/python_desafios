# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:27:48 2020

TEMPO EM MINUTOS, HORAS E SEGUNDOS

556
1
140153

@author: psgei

"""
Evento = int(input())

T_segundos = [3600, 60, 1]
Resultado = []

for second in T_segundos:
    qtd = int(Evento / second) #second calculado aos valores da lista T_s
    Resultado.append(str(qtd)) #adcionando na lista Resultado
    Evento -= qtd * second #Descontando segundos usados em horas
    
print(":".join(Resultado))