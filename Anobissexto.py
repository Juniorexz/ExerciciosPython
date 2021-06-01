ano=int(input("Digite um ano : "))
if (ano%4==0 and not ano%100==0):
    print('Ano é bissexto.') 
else:
    print('Ano não bissexto.')
