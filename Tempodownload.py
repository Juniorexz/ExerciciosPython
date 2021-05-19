#Faça um programa que peça o tamanho de um arquivo
#para download (em MB) e a velocidade de um link 
#de Internet (em Mbps), calcule e informe o tempo 
#aproximado de download do arquivo usando este link (em minutos). 
#1024

#def medidor():
tamanho = float(input("Digite o tamanho do arquivo: "))
link = float (input("Digite a velocidade do link de internet em Mbps: "))
tempo = tamanho / link * 60
print(f'Tempo de download: {tempo:.0f}  Minutos ')
