#Faça um Programa que pergunte quanto você ganha 
# por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
#2f = As casas decimais


valorhora = float(input("Quanto vc ganha por hora ? "))
horas = int(input("Digite a quantidade horas que vc trabalhou no mês : "))
salario = valorhora * horas
print(f"O valor do salario ao mês seria R$ {salario:.2f}")
#print(salario)