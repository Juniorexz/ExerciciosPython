#Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.


'''    nota1=float(input('Nota 1: \n'))
    nota2=float(input('Nota 2: \n'))
    media=(nota1+nota2)/2
    print(f'A média das notas {nota1} e {nota2} é {media}')



Solução 2


    nota1=float(input('Nota 1: \n'))
    nota2=float(input('Nota 2: \n'))
    print(f'A média das notas {nota1} e {nota2} é {(nota1+nota2)/2}')


'''



valor1 = float(input("Digite a primeira nota : "))
valor2 = float(input("Digite a segunda nota : "))
media = (valor1 + valor2) /2
if media >= 7 and media < 10:
    print  ("Aluno aprovado")
elif media == 10:
    print  ("Aluno aprovado com Distinção")
else:
    print ("Aluno reprovado")
