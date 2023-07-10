#11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

a = int(input('Digite o valor de um número inteiro:'))
b = int(input('Digite o valor de um número inteiro:'))
c = int(input('Digite o valor de um número real:'))

produto = ((2*a)*(0.5*b))
soma = ((3*a) + c)
cubo = (c*c*c)

print('O valor do produto:', produto )
print('O valor da soma:', soma )
print('O valor do terceiro elevado ao cubo:', cubo )