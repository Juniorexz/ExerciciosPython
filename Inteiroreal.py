#Faça um Programa que peça 2 números inteiros e um número real.
#  Calcule e mostre:
#  o produto do dobro do primeiro com metade do segundo .
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo. 



valor1 = int(input("Digite o valor1 : "))
valor2 = int(input("Digite o valor2 : "))
valor3 = float(input("Digite o valor3 : "))
#print ('\n a)O produto do dobro do primeiro com a metade do segundo:\n')
print ("Valor: ", int(valor1 * 2 * valor2/2))
print ('\n b)A soma do triplo do primeiro com o terceiro:\n')
 if type(valor3) == "int":
         print("Valor: ", int (valor1 * 3 + valor3))
    else:
        print("Valor: ", valor1 * 3 + valor3)
    print ('\n c)O terceiro elevado ao cubo:\n')
    if type(valor3) = "int":
         print("Valor: ", int(valor3 ** 3))
    else:
    print ("Valor: ", valor3 ** 3)