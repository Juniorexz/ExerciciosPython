def menu_inicial():
    print('Programa Caixa Eletrônico ')

#print('Qual valor deseja sacar')
valorconta = float(input("Digite o valor que possui de saldo na conta :"))
variavel= float(input("Digite o valor que deseja sacar [10-1000] : "))
#valorquersacar = variavel - 
conta = valorconta - variavel
print(conta)

duzentos = int(variavel / 200)
variavel = variavel - (duzentos*200)
 
cem = int(variavel / 100)
variavel = variavel - (cem*100)
    
cinquenta = int(variavel/50)
variavel = variavel - (variavel*50)

vinte = int(variavel/20)
variavel = variavel - (vinte*20)

dez = int(variavel/10)
variavel = variavel - (dez*10)

cinco = int(variavel/5)
variavel = variavel - (cinco*5)

dois = int(variavel/2)
variavel = variavel - (dois*2)

um = int(variavel/1)
variavel = variavel - (um*1)

cinquentacents = float(variavel/0,50)
variavel = variavel - (cinquentacents*0,50)

vintecincocents = float(variavel/0,25)
variavel = variavel - (vintecincocents*0,25)

dezcents = float(variavel/0,10)
variavel = variavel - (dezcents*0,10)

cincocents = float(variavel/0,5)
variavel = variavel - (cinquenta*0,5)

umcents = float(variavel/0,1)
variavel = variavel - (umcents*0,1)

#dois = variavel
print('Notas R$200,00 = ',duzentos)
print('Notas R$100,00 = ',cem)
print('Notas R$ 50,00 = ',cinquenta)
print('Notas R$20,00 = ',vinte)
print('Notas R$ 10,00 = ',dez)
print('Notas R$  5,00 = ',cinco)
print('Notas R$  2,00 = ',dois)
print('Notas R$  1,00 = ',um)
print('Moedas R$ 0,50 = ',cinquentacents)
print('Moedas R$  0,25 = ',vintecincocents)
print('Moedas R$  0,10 = ',dezcents)
print('Moedas R$  0,05 = ',cincocents)
print('Moedas R$  0,01 = ',umcents)

print('Saldo atual = ', conta)