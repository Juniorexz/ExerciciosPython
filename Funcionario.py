'''Escreva um programa que solicite o nome,
o sobrenome e o salário atual de um funcionário. Ao fim, 
calcule seu novo salário considerando cenários hipotéticos,
com os seguintes aumentos: 10%, 25%,30% e 50%. 
A mensagem na tela deverá seguir o seguinte padrão:
"Olá, [nome] [sobrenome]"
"Seu salário atual é : [salário]"
"Seu salário com 10% de aumento é: [salário]"
"Seu salário com 25% de aumento é: [salário]"
"Seu salário com 30% de aumento é: [salário]"
"Seu salário com 50% de aumento é: [salário]"
No campo nome e sobrenome utilize os métodos strip() e title().
Lembre-se que o primeiro método permite remover os espaços
antes e após a string, enquanto que o último permite colocar
 a string no formato titlecased (capitaliza string).'''

'''

def menu_inicial():
    print('Programa Aumento de salario')
    print('1. Aumento de 10%: ')
    print('2. Aumento de 25%: ')
    print('3. Aumento de 30%: ')
    print('4. Aumento de 50%: ')


nome=str(input('Digite o seu nome: ').strip().title()
sobrenome=str(input('Digite o seu sobrenome: ').strip().title()
salarioatual=float(input('Digite o seu salario atual'))


def aumentodez():
    soma = salarioatual + salarioatual * 0.1 
    print(f"O aumento de dez por cento seria equivalente a :  {salarioatual}+{salarioatual * 0.1} = {aumentodez}")

def aumentovinteecinco():
    soma = salarioatual + salarioatual * 0.25 
    print(f"O aumento de vinte e cinco por cento seria equivalente a :  {salarioatual}+{salarioatual * 0.25} = {aumentovinteecinco}")

def aumentotrinta():
    soma = salarioatual + salarioatual * 0.30 
    print(f"O aumento de trinta por cento seria equivalente a :  {salarioatual}+{salarioatual * 0.30} = {aumentotrinta}")

def aumentocinquenta():
    soma = salarioatual + salarioatual * 0.50
    print(f"O aumento de cinquenta por cento seria equivalente a :  {salarioatual}+{salarioatual * 0.50} = {aumentocinquenta}")



if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o aumento que o funcionario vai receber: ')

    if escolha == '1':
        aumentodez()

    if escolha == '2':
        aumentovinteecinco()

    if escolha == '3':
        aumentotrinta()

    if escolha == '4':
       aumentocinquenta()
'''

nome=input('Digite seu nome: ').strip().title()
sobrenome=input('Digite seu sobrenome: ').strip().title()
salario=float(input('Digite seu salário: '))
print(f'Olá, {nome} {sobrenome}')
print(f'Seu salário atual é: R$ {salario:.2f}')
print(f'Seu salário com 10% de aumento é: R$ {salario*1.1:.2f}')
print(f'Seu salário com 25% de aumento é: R$ {salario*1.25:.2f}')
print(f'Seu salário com 30% de aumento é: R$ {salario*1.3:.2f}')
print(f'Seu salário com 50% de aumento é: R$ {salario*1.5:.2f}')