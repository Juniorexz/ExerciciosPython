'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
 O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal. 
'''

def menu_inicial():
    print('Programa Multifuncional')
    print('1. Definir se valor deve ser par ou impar: ')
    print('2. Positivo ou negativo: ')
    print('3. Inteiro ou decimal: ')

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operacao = input("Qual operação voce deseja? (1, 2, 3): ")


if operacao == '1':
	resultado = num1 + num2
	if resultado % 2 == 0:
		print("O numero %d é par!" % resultado)
	else:
		print("O numero %d é impar." % resultado)
	if resultado >= 0:
		print("O numero %d é Positivo!" % resultado)
	else:
		print("O numero %d é negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d é inteiro!" % resultado)
	else:
		print("O numero %.1f é decimal." % resultado)

if operacao == '2':
	resultado = num1 - num2
	if resultado % 2 == 0:
		print("O numero %d é par!" % resultado)
	else:
		print("O numero %d é impar." % resultado)
	if resultado >= 0:
		print("O numero %d é Positivo!" % resultado)
	else:
		print("O numero %d é negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d é inteiro!" % resultado)
	else:
		print("O numero %.1f é decimal." % resultado)

if operacao == '3':
	resultado = num1 * num2
	if resultado % 2 == 0:
		print("O numero %d é par!" % resultado)
	else:
		print("O numero %d é impar." % resultado)
	if resultado >= 0:
		print("O numero %d é Positivo!" % resultado)
	else:
		print("O numero %d é negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d é inteiro!" % resultado)
	else:
		print("O numero %.1f é decimal." % resultado)



if __name__=='__main__':
    menu_inicial()
   # escolha = input('Escolha o tipo de operação que deseja realizar: ')

    if operacao == '1':
        ()

    if operacao == '2':
         ()

    if operacao == '3':
        ()
