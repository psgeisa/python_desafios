# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 00:37:28 2020
NOTAS E MOEDAS
@author: psgei
"""
    
"""
#1 tentativa
Valor = float(input())

cedulas = [100,50,20,10,5,2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for cedula in cedulas:
    qtd_cedulas = int(Valor / cedula)
    print("{} nota(s) de R$ {:.2f}".format(qtd_cedulas, cedula))
    Valor -= qtd_cedulas * cedula
    
print('MOEDAS:')
for moeda in moedas:
    qtd_moedas = int(Valor / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas, moeda))
    Valor -= qtd_moedas * moeda

#2 tentativa
valor = float(input())

Reais100 = int(valor//100)
Sobra = valor%100

Reais050 = int(Sobra//50)
Sobra = Sobra%50

Reais020 = int(Sobra//20)
Sobra = Sobra%20

Reais010 = int(Sobra//10)
Sobra = Sobra%10

Reais005 = int(Sobra//5)
Sobra = Sobra%5

Reais002 = int(Sobra//2)
Sobra = Sobra%2

M100 = int(Sobra//1)
Sobra = Sobra%1

M050 = int(Sobra//0.50)
Sobra = Sobra%0.50

M025 = int(Sobra//0.25)
Sobra = Sobra%0.25

M010 = int(Sobra//0.10)
Sobra = Sobra%0.10

M005 = int(Sobra//0.05)
Sobra = Sobra%0.05

M001 = int(Sobra//0.01)
Sobra = Sobra%0.01

print("NOTAS:")
print(Reais100,"nota(s) de R$ 100.00")
print(Reais050,"nota(s) de R$ 50.00")
print(Reais020,"nota(s) de R$ 20.00")
print(Reais010,"nota(s) de R$ 10.00")
print(Reais005,"nota(s) de R$ 5.00")
print(Reais002,"nota(s) de R$ 1.00")
print("MOEDAS:")
print(M100,"moeda(s) de R$ 1.00")
print(M050,"moeda(s) de R$ 0.50")
print(M025,"moeda(s) de R$ 0.25")
print(M010,"moeda(s) de R$ 0.10")
print(M005,"moeda(s) de R$ 0.05")
print(M001,"moeda(s) de R$ 0.01")


#Python 2 Goya
l1 = [100, 50, 20, 10, 5, 2]
l2 = [50, 25, 10, 5, 1]
ls = []
s  = input()
ls = s.split(".", 2)
re = int(ls[0])
ce = int(ls[1])

print "NOTAS:"
for i in l1:
n  = re / i
re = re % i
print "%d nota(s) de R$ %d.00" % (n, i)

print "MOEDAS:"
print "%d moeda(s) de R$ 1.00" % (re)

for i in l2:
n  = ce / i
ce = ce % i
print "%d moeda(s) de R$ %.2f" % (n, float(i)/100.0)


#3 tentativa
Valor = float(input())

cedulas = [100,50,20,10,5,2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for cedula in cedulas:
    qtd_cedulas = int(round(Valor,2) / cedula)
    print("{} nota(s) de R$ {:.2f}".format(qtd_cedulas, cedula))
    Valor -= qtd_cedulas * cedula
    
print('MOEDAS:')
for moeda in moedas:
    qtd_moedas = int(Valor / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas, moeda))
    Valor -= qtd_moedas * moeda


#4 tentativa

valor = input().split()
reais = int(linha[0])
moedas = int(linha[1])

print("VALOR A PAGAR: R$ {:.2f}".format(VT))

Reais, Moedas = (input())

cedulas = [100,50,20,10,5,2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for cedula in cedulas:
    qtd_cedulas = int(Reais, Moedas / cedula)
    print("{} nota(s) de R$ {:.2f}".format(qtd_cedulas, cedula))
    Valor -= qtd_cedulas * cedula
    
print('MOEDAS:')
for moeda in moedas:
    qtd_moedas = int(Valor / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moedas, moeda))
    Valor -= qtd_moedas * moeda

#Operando com a lista completa
valores = float(input())
lista = [100.00,50.00,20.00,10.00,5.00,2.00,1.00,0.5,0.25,0.1,0.05,0.01]
qtd = [0]*12
for RS in range(0,12): 
  while valores >= lista[RS]:
    qtd[RS] = qtd[RS] + 1
    valores = round(valores,2) - lista[RS]
    
#Saída - primeira parte da lista
print('NOTAS:') 
for RS in range(0,6):
    valores = int()
    print('{} nota(s) de R$ {:.2f}'.format(qtd[RS],lista[RS]))

#Saída - segunda parte da lista
print('MOEDAS:')
for RS in range(6,12):
    valores = int()
    print('{} moeda(s) de R$ {:.2f}'.format(qtd[RS],lista[RS]))
    
####    
n = float(input())

n100 = n // 100
n = n - n100*100

n50 = n // 50
n = n - n50*50

n20 = n // 20
n = n - n20*20

n10 = n // 10
n = n - n10*10

n5 = n // 5
n = n - n5*5

n2 = n // 2
n = n - n2*2

n1 = n // 1
n = n - n1*1
n1=float('%.2f'% n1)
n=float('%.2f'% n)

m50 = n // 0.5
n = n - m50*0.5
m50=float('%.2f'% m50)
n=float('%.2f'% n)

m25 = n // 0.25
n = n - m25*0.25
m25=float('%.2f'% m25)
n=float('%.2f'% n)

m10 = n // 0.10
n = n - m10*0.10
m10=float('%.2f'% m10)
n=float('%.2f'% n)

m5 = n // 0.05
n = n - m5*0.05
m5=float('%.2f'% m5)
n=float('%.2f'% n)

m1 = n * 100
m1=float('%.2f'% m1)
n=float('%.2f'% n)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(n100)))
print('{} nota(s) de R$ 50.00'.format(int(n50)))
print('{} nota(s) de R$ 20.00'.format(int(n20)))
print('{} nota(s) de R$ 10.00'.format(int(n10)))
print('{} nota(s) de R$ 5.00'.format(int(n5)))
print('{} nota(s) de R$ 2.00'.format(int(n2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(n1)))
print('{} moeda(s) de R$ 0.50'.format(int(m50)))
print('{} moeda(s) de R$ 0.25'.format(int(m25)))
print('{} moeda(s) de R$ 0.10'.format(int(m10)))
print('{} moeda(s) de R$ 0.05'.format(int(m5)))
print('{} moeda(s) de R$ 0.01'.format(int(m1)))

valor = float(input())

Reais100 = (valor//100)
valor = valor - Reais100*100

Reais050 = (valor//50)
valor = valor - Reais050*50

Reais020 = (valor//20)
valor = valor - Reais020*20

Reais010 = (valor//10)
valor = valor - Reais010*10

Reais005 = (valor//5)
valor = valor - Reais005*5

Reais002 = (valor//2)
valor = valor - Reais100*2

M100 = (valor//1)
valor = valor - M100*1
M100('%.2f M100)
valor = float'%.2f' valor)

M050 = (valor//1)
valor = valor - M050*0.5
M050('%.2f M050)
valor = float'%.2f' valor)

M025 = (valor//1)
valor = valor - M025*0.25
M025('%.2f M025)
valor = float'%.2f' valor)

M010 = (valor//1)
valor = valor - M010*0.10
M010('%.2f M010)
valor = float'%.2f' valor)

M005 = (valor//1)
valor = valor - M050*0.05
M050('%.2f M050)
valor = float'%.2f' valor)

M001 = valor * 100
M001 = float('%.2f'% M001)
valor = float('%.2f'% valor)

print("NOTAS:")
print("{} nota(s) de R$ 100.00").format(int(R100)))
print("{} nota(s) de R$ 50.00").format(int(R050)))
print("{} nota(s) de R$ 20.00").format(int(R020)))
print("{} nota(s) de R$ 10.00").format(int(R010)))
print("{} nota(s) de R$ 5.00").format(int(R005)))
print("{} nota(s) de R$ 1.00").format(int(R1)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00").format(int(M100)))
print("{} moeda(s) de R$ 0.50").format(int(M050)))
print("{} moeda(s) de R$ 0.25").format(int(M025)))
print("{} moeda(s) de R$ 0.10").format(int(M010)))
print("{} moeda(s) de R$ 0.05").format(int(M005)))
print("{} moeda(s) de R$ 0.01").format(int(M001)))
"""
valor = float(input())

n100 = valor//100
valor = valor - n100*100

n50 = valor//50
valor = valor - n50*50

n20 = valor//20
valor = valor - n20*20

n10 = valor//10
valor = valor - n10*10

n5 = valor//5
valor = valor - n5*5

n2 = valor//2
valor = valor - n2*2

m1 = valor//1
valor = valor - m1*1
m1 = float('%.2f'% m1)
valor = float('%.2f'% valor)

m50 = valor//0.5
valor= valor- m50*0.5
m50=float('%.2f'% m50)
valor=float('%.2f'% valor)

m25 = valor//0.25
valor = valor - m25*0.25
m25 = float('%.2f'% m25)
valor = float('%.2f'% valor)

m10 = valor//0.10
valor = valor - m10*0.10
m10 = float('%.2f'% m10)
valor = float('%.2f'% valor)

m5 = valor//0.05
valor = valor - m5*0.05
m5 = float('%.2f'% m5)
valor = float('%.2f'% valor)

m01 = valor*100
m01 = float('%.2f'% m01)
valor = float('%.2f'% valor)

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(n100)))
print('{} nota(s) de R$ 50.00'.format(int(n50)))
print('{} nota(s) de R$ 20.00'.format(int(n20)))
print('{} nota(s) de R$ 10.00'.format(int(n10)))
print('{} nota(s) de R$ 5.00'.format(int(n5)))
print('{} nota(s) de R$ 2.00'.format(int(n2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(m1)))
print('{} moeda(s) de R$ 0.50'.format(int(m50)))
print('{} moeda(s) de R$ 0.25'.format(int(m25)))
print('{} moeda(s) de R$ 0.10'.format(int(m10)))
print('{} moeda(s) de R$ 0.05'.format(int(m5)))
print('{} moeda(s) de R$ 0.01'.format(int(m01)))
