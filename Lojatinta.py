#Faça um Programa para uma loja de tintas.
#  O programa deverá pedir o tamanho em metros quadrados
#  da área a ser pintada. Considere que a cobertura
#  da tinta é de 1 litro para cada 6 metros quadrados
#  e que a tinta é vendida em latas de 18 litros,
#  que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#  Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#    comprar apenas latas de 18 litros;
#    comprar apenas galões de 3,6 litros;
#    misturar latas e galões, de forma que o desperdício de tinta seja menor. 
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 


def menu_inicial():
    print('Programa para Loja de Tintas')
    print('1. Apenas latas de 18 litros')
    print('2. Apenas galões de 3,6 litros')
    print('3. Mistura de latas e galões')


def latas():
    metros = float(input("Valor tamanho em metros quadrados: "))
    litros = round(metros / 6)
    latas = round(litros / 18)
    #litros = round(metros / 6)
    #latas = round(litros / 18)
    valorlatas = latas * 80
    print(f"Devera utilizar {latas:.2f} latas")
    print(f'Valor de latas equivale a R$:{valorlatas:.2f}')


def galoes():
    metros = float(input("Valor tamanho em metros quadrados: "))
    litros = round(metros / 6)
    galao = round(litros / 3.6)
    #litros = round(metros/6)
    #galao = round(litros / 3.6)
    valorgalao = galao * 25
    print(f"Devera utilizar {galao::.2f} latas")
    print(f'Valor de galões equivale a R$:{valorgalao:.2f}')


def mistura():
    metros = float(input("Valor tamanho em metros quadrados: "))
    litros = round(metros/6) 
    mistura = round(litros * 0.10)
    #mistura = round((litros / 18) + (litros))
    print(f'Devera utilizar {mistura:.2f} de latas')

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de compra que deseja realizar: ')

    if escolha == '1':
        latas()

    if escolha == '2':
        galoes()

    
    if escolha == '3':
        mistura()
