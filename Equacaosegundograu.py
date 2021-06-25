'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
 O programa deverá pedir os valores de a, b e c e fazer as consistências, 
 informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 

O primeiro teste que fazemos é em relação ao coeficiente a. Se for 0, não é uma equação do segundo grau e acaba o programa.

Se for diferente de 0, cai no else, que é onde todo nosso programa vai funcionar. Primeiro, dentro do else, pedimos o valor dos coeficientes b e c.

Agora, vamos calcular o delta.
Em Python, fica assim: delta = b*b - (4*a*c)

Agora vamos testar o delta, dentro de um if aninhado no else anterior.
Se for menor que 0, encerramos o programa dizendo que as raízes são imaginárias.

Em seguida, usamos um elif para testar se delta for 0, se sim valor da raiz será:raiz = -b / (2*a)

Por fim, se não é menor que 0 e o delta não é 0, é porque vai ser sempre maior que 0. Essa condição cai no else aninhado, onde calculamos as raízes assim:
raiz1 = (-b + math.sqrt(delta) ) / (2*a)
raiz2 = (-b  - math.sqrt(delta) ) / (2*a)








'''

import math

print('Equaçao do 2o grau da forma: ax² + bx + c')

def menu_inicial():

    a = int( input('Coeficiente a: ') )

    if(a==0):
        print('Se a=0, não é equação do segundo grau.')
    else:
        b = int( input('Coeficiente b: ') )
        c = int( input('Coeficiente c: ') )
        delta = b*b - (4*a*c)

    if delta<0:
            print('Delta menor que 0. Raízes inexistentes. ')
    elif delta==0:
            raiz = -b / (2*a)
            print('Delta=0 , raiz = ',raiz)
    else:
            raiz1 = (-b + math.sqrt(delta) ) / (2*a)
            raiz2 = (-b - math.sqrt(delta) ) / (2*a)
            print('Raizes: ',raiz1,' e ',raiz2)

