#Faça um Programa que peça o raio de um círculo,
#  calcule e mostre sua área. 
# r**2 = quadrado
#

'''
    from math import pi
    raio=float(input('Digite o valor do raio da circunferência: '))
    print(f'Área da circunferência: {pi*raio**2:.2f}')



'''
import math


pi = math.pi
pi = 3.14
r = int(input("Digite o raio:  "))
a = pi*(r*r)
print(a)