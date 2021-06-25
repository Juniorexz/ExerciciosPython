'''Faça um código que receba o valor de um produto
 na loja com duas casas decimais e calcule um novo 
valor do desconto progressivo desse produto.
O valor final do produto não pode chegar
a ser menor do que 40% do seu preço original. 
Caso o produto caia nessa condição deve se dar
um desconto de 65% do valor inicial apenas, 
caso contrário os produtos terão um desconto de 10% progressivo
 (descontos sobre o desconto) para cada 100 reais de custo inicial. 
'''

def menu_inicial():
    print('Programa de Desconto')

valororiginal = float(input("Digite o valor do produto : "))
precoproduto = float(input("Digite o valor do produto com desconto : "))
preco = 0

if precoproduto <= 40 /100:
         valororiginal * 65 / 100
else:
        preco = 10 / 100
print('O valor do produto com desconto  é {.:2f}'.format(precoproduto))