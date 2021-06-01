def menu_inicial():
    print('Programa Calculadora')
    print('1. Somar: ')
    print('2. Subtrair: ')
    print('3. Multiplicação: ')
    print('4. Divisão: ')
    print('5. Exponenciação: ')
    print('6. Resto da divisão: ')


def soma():
    soma = var1 + var2
    print(f"A soma seria {var1}+{var2} = {soma}")

def subtracao():
    subtracao = var1 - var2
    print(f"A subtração seria {var1}-{var2} = {subtracao}")


def mult():
    mult = var1 * var2
    print(f"A multiplicação seria {var1}*{var2} = {mult}")

def div():
    div = var1 / var2
    print(f"A divisão seria {var1}/{var2} = {div}")


def expo():
    expo = var1 ** var2
    print(f"O expoente seria {var1}**{var2} = {expo}")


def resto():
    resto = var1 % var2
    print(f"O resto seria {var1}%{var2} = {resto}")


var1 = float( input("Digite um numero: ") )
var2 = float( input("Digite outro numero: ") )


if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de operação que deseja realizar: ')

    if escolha == '1':
        soma()

    if escolha == '2':
         subtracao()

    if escolha == '3':
        mult()

    if escolha == '4':
        div()

    if escolha == '5':
        expo()

    if escolha == '6':
        resto()
    
    


