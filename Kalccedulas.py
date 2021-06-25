cedulas = [200.0, 100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

def qnt_cedulas(valor: float) -> None:
    '''Função que imprime a quantidade de cédulas para um dado valor.
    Argumentos:
    -- valor (float): valor informado para o cálculo da quantidade de cédulas.
    '''
    for cedula in cedulas:
        qnt, resto = int(valor/cedula), valor % cedula
        print(f'A quantidade em {"moedas" if cedula < 1 else "cédulas"} seria: {qnt} com resto {resto}')

def menu_principal():
    '''Função que imprime o menu principal'''
    valor = float(input('Digite um valor a ser calculado: '))

    qnt_cedulas(valor)

if __name__ == '__main__':
    menu_principal()