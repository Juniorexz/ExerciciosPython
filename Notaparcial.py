'''Faça um programa que lê as duas notas parciais obtidas por um aluno 
numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:

      Média de Aproveitamento  Conceito
      Entre 9.0 e 10.0        A
      Entre 7.5 e 9.0         B
      Entre 6.0 e 7.5         C
      Entre 4.0 e 6.0         D
      Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, 
o conceito correspondente e a mensagem “APROVADO”
 se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E
'''

def menu_inicial():
    print('Programa Boletim Alunos')

nota1=float(input("Digite a nota do primeiro semestre: "))
nota2=float(input("Digite a nota do segundo semestre: "))

media=(nota1+nota2)/2
if media >=9:
   conceito = "A"
elif media >= 7.5:
   conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:               # Não é necessário utilizar o elif já que só resta uma opção 
    conceito = "E"
if conceito == "A" or "B" or "C":
    resultado = "Aprovado!"
else:                       #Mesma coisa aqui se conceito não é A,B,C é D ou E
    resultado = "Reprovado"
print("Nota 1: %.2f\nNota 2:%.2f"%(nota1,nota2))
print("Média: %.2f"%media)
print("Conceito: %s"%conceito)
print("Resultado: %s"%resultado)