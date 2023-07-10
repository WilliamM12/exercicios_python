#6) Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math #Declaração da biblioteca
math.pi # Valor do número Pi, acessado pela biblioteca

r = float(input('Digite o valor do raio do círculo:'))

a = (math.pi * r *r)

print('O valor da área do círculo é :', a )