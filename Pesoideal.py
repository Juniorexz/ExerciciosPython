#Tendo como dados de entrada a altura de uma pessoa,
#  construa um algoritmo que calcule seu peso ideal,
#  usando a seguinte fórmula: (72.7*altura) - 58 

altura = float(input("Digite a altura : "))
peso = float(input("Digite o peso : "))
pesoideal = 72.7*altura - 58 
print(f"O peso ideal seria :  {pesoideal:.2f} Kg")
