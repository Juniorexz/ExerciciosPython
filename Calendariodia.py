#Modifique o programa anterior e permita
#que o usuário especifique o ano e o mês a serem mostrados na tela.

import calendar
ano=int(input('Ano: '))
mes=int(input('Mês: '))
#dia=int(input('Dia: '))

print(calendar.month(ano,mes))