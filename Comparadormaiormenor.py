
def menu_inicial():
    print('Programa Comparador')
    print('1. Exibir o maior valor: ')
    print('2. Exibir o menor valor: ')

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))


def maior():
    if valor1 > valor2 and valor1 > valor3 :
        print("O primeiro número digitado é o maior: ", valor1)
    elif valor2 > valor3 and valor2 > valor1 :
        print("O segundo número digitado é o maior: ", valor2)
    elif valor3 > valor1 and valor3 > valor2:
        print("O terceiro número digitado é o maior: ", valor3)



def menor():
    if valor1 < valor2 and valor3:
        print("O primeiro número digitado é o menor: ", valor1)
    elif valor2 < valor1 and valor3:
        print("O segundo número digitado é o menor: ", valor2)
    elif valor3 < valor1 and valor2:
        print("O terceiro número digitado é o menor: ", valor3)


    elif valor1 < valor2 and valor1 < valor3:
        print (valor1,'é','o menor!!')
    elif valor2 < valor3 and valor2 < valor1 :
        print (valor2,'é','o menor!!')
    elif valor3 < valor2 and valor3 < valor1 :
        print (valor3,'é','o menor!!')


if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de operação que deseja realizar: ')

    if escolha == '1':
        maior()

    if escolha == '2':
         menor()

    