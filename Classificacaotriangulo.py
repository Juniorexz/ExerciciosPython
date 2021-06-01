
def menu_inicial():
    print('Programa  classificador de triangulo')


valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 == valor2 and valor1 == valor3 :
    print("O triangulo possui todos os lados iguais portanto é equilatero: ", valor1)
elif valor1 == valor2 or valor1 == valor3 : 
    print('O triângulo é isósceles os lados possuem medidas diferentes;')
else:
     print('O triângulo é isósceles: pois tem dois lados com o mesmo tamanho.')

    