#Faça um programa que imprima na tela
# de 1 até um número digitado pelo usuário.
'''
num=int(input('Digite um número: '))  #receber número do usuário
x=1
while x<=num:
        print(x)
        x+=1
'''
#Range = Ela gera uma serie de números iniciando de 0
# a té o numero definido, ou de um numero inicial a um numero final
num=int(input('Digite um número: '))  #receber número do usuário
for valor in range(1,num+1):
    print(valor)

