#Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados
#da área a ser pintada. Considere que a cobertura
#da tinta é de 1 litro para cada 3 metros quadrados
#e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00. Informe ao usuário a quantidades
#de latas de tinta a serem compradas e o preço total. 
#% == resto 
#round = arredondamento
#

metros = float(input("Valor tamanho em metros quadrados: "))
litros = round(metros/3)
latas = round(litros / 18)

if latas % 18 != 0:
    latas += 1
    
total = latas * 80

print (f"Sera utilizado: {latas} o preco total sera de R$: {total:.2f}")


#print(f'+ Salario Bruto : R$ {salariobruto:.2f}')