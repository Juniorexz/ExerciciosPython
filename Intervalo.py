#Escreva um programa que peça ao usuário 
#números entre 0-10. Se o usuário inserir
#um número fora desse intervalo o programa
#deverá finalizar com uma mensagem personalizada.

while True:
    num=int(input('Insira um número inteiro entre 0-10: '))
    if num<0 or num>10:
        print('Fim do programa.')
        break
