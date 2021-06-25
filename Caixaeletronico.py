'''Faça um Programa para um caixa eletrônico.
 O programa deverá perguntar ao usuário a valor do saque 
 e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 
'''


def menu_inicial():
    print('Programa Caixa Eletrônico ')

#print('Qual valor deseja sacar')
valorconta = float(input("Digite o valor que possui de saldo na conta :"))
variavel= int(input("Digite o valor que deseja sacar [10-1000] : "))
#valorquersacar = variavel - 
conta = variavel - valorconta


duzentos = int(variavel / 200)
variavel = variavel - (duzentos*200)
 
cem = int(variavel / 100)
variavel = variavel - (cem*100)
    
cinquenta = int(variavel/50)
variavel = variavel - (variavel*50)

vinte = int(variavel/20)
variavel = variavel - (vinte*20)

dez = int(variavel/10)
variavel = variavel - (dez*10)

cinco = int(variavel/5)
variavel = variavel - (cinco*5)

dois = int(variavel/2)
variavel = variavel - (dois*2)

#dois = variavel
print('Notas R$200,00 = ',duzentos)
print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$20,00 = ',vinte)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  2,00 = ',dois)

print('Saldo atual = ', conta)



