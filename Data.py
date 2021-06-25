'''
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 
Para armazenar o valor lógico verdadeiro ou falso, vamos usar a variável booleana 'valido'. Inicialmente fazer ela ser falsa:
valido = False

O grande segredo nesse algoritmo é o mês.

Primeiro vamos testar se o mês digitado tem 31 dias.
São os meses 1, 3, 5, 7, 8, 10 ou mês 12.
Se tiver digitado um desses valores para 'mes', vamos verificar a variável 'dia' é menor ou igual a 31. Se for, a data é válida e fazemos 'valida = True'
Se não for, continua sendo False

Agora vamos testar os meses que tem 30 dias.
Eles são os meses 4, 6, 9 e o mês 11.
Nesses meses, temos que avaliar se a variável 'dia' tem um número menor ou igual a 30. Se sim, fazemos 'valida = True'.

Por fim, vamos avaliar o mês mais problemático, o mês 2, fevereiro.
Inicialmente, é preciso verificar se é ano bissexto, se for bissexto a variável 'dia' deve ser testada para saber se o valor digitado é 29 ou menos. Se sim, validamos a data com 'valida = True'

Se não for ano bissexto, testamos a variável 'dia' para saber se o valor digitado foi 28 ou menos. Se for, 'valida = True'

Caso não tenham digitado um número de 1 até 12 em mês, a variável 'valida' continua tendo valor False, pois não caiu em nenhum IF ou ELIF.

Por fim, testamos a variável booleana 'valida'. Se for True, dizemos que a data é válida, se tiver o valor lógico False nela, dizemos que é inválida:





'''

dia = int( input('Dia: ') )
mes = int( input('Mês: ') )
ano = int( input('Ano: ') )

valida = False
    
    # Meses com 31 dias
if( mes==1 or mes==3 or mes==5 or mes==7 or \
        mes==8 or mes==10 or mes==12):
        if(dia<=31):
            valida = True
    # Meses com 30 dias
elif( mes==4 or mes==6 or mes==9 or mes==11):
        if(dia<=30):
            valida = True
elif mes==2:
        # Testa se é bissexto
        if (ano%4==0 and ano%100!=0) or (ano%400==0):
            if(dia<=29):
                valida = True
        elif(dia<=28):
                valida = True

if(valida):
        print('Data válida')
else:
        print('Inválida')