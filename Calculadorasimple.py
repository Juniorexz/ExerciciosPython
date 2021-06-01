operacao=input('Escolha a operação deseja: (+,-,*,/): ')
if operacao in ['+','-','*','/']:
        num1=float(input('Número 1: '))
        num2=float(input('Número 2: '))
        if operacao=='+':
            print(f'{num1}+{num2}={num1+num2}')
        elif operacao=='-':
            print(f'{num1}-{num2}={num1-num2}')
        elif operacao=='*':
            print(f'{num1}*{num2}={num1*num2}')
        else:
            if num2==0:
                print('O denominador precisa ser diferente de zero.')
            else:
                print(f'{num1}/{num2}={num1/num2}')
else:
        print('Opção inválida.')