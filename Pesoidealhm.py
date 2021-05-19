#Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#  Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 

def menu_inicial():
    print('Programa peso ideal')
    print('1. Peso ideal para homens')
    print('2. Peso ideal para mulheres')

def pesohomem():
    altura = float(input('Entre com a altura: '))
    pesohomem = 72.7*altura - 58 
    print('Peso ideal para homens: {:.2f} Kg'.format(pesohomem))

def pesomulher():
    altura = float(input('Entre com a altura: '))
    pesomulher = 62.1*altura - 44.7
    print('Peso ideal para mulheres: {:.2f} Kg'.format(pesomulher))

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de operação que deseja realizar: ')

    if escolha == '1':
        pesohomem()

    if escolha == '2':
        pesomulher()

