#Faça um Programa que pergunte quanto você ganha por hora 
# e o número de horas trabalhadas no mês. Calcule e mostre o total
# do seu salário no referido mês, sabendo-se que são descontados 
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
# faça um programa que nos dê:
#salário bruto.quanto pagou ao INSS.quanto pagou ao sindicato.o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#{salario:.2f}
 

valorhora = float(input("Quanto vc ganha por hora ? "))
horas = int(input("Digite a quantidade horas que vc trabalhou no mês : "))


salariobruto = valorhora * horas
impostorenda = salariobruto * 0.11
inss = salariobruto * 0.08
sindicato = salariobruto * 0.05

print(f'+ Salario Bruto : R$ {salariobruto:.2f}')
print(f'- IR : R$ {impostorenda:.2f}')
print(f'- INSS : R$ {inss:.2f}')
print(f'- Sindicato : R$ {sindicato:.2f}')
print(f'= Salario Liquido : R$ {salariobruto - impostorenda - inss - sindicato:.2f}')

