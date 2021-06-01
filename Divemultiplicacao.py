'''
    num1=float(input('Número 1: '))
    num2=float(input('Número 2: '))
    print(f'{num1}x{num2}={num1*num2}')
    print(f'{num1}/{num2}={num1/num2}')


'''


def menu_inicial():
    print('1. Multiplicação: ')
    print('2. Divisão: ')

def mult():
    mult = var1 * var2
    print(f"A multiplicação seria {var1}*{var2} = {mult}")

def div():
    div = var1 / var2
    print(f"A divisão seria {var1}/{var2} = {div}")


var1 = float( input("Digite um numero: ") )
var2 = float( input("Digite outro numero: ") )

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de operação que deseja realizar: ')

    if escolha == '1':
        mult()

    if escolha == '2':
         div()
