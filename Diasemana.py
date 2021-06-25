def menu_inicial():
    print('Programa dia da semana')
    print('1. Domingo ')
    print('2. Segunda ')
    print('3. Terça')
    print('4. Quarta ')
    print('5. Quinta ')
    print('6. Sexta ')


def domingo():
    print(f"O dia escolhido vai ser Domingo")

def segunda():
    print(f"O dia escolhido vai ser Segunda")

def terca():
    print(f"O dia escolhido vai ser Terca")

def quarta():
    print(f"O dia escolhido vai ser Quarta")

def quinta():
    print(f"O dia escolhido vai ser Quinta")

def sexta():
    print(f"O dia escolhido vai ser Sexta")

def sabado():
    print(f"O dia escolhido vai ser  Sabado")




if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de operação que deseja realizar: ')

    if escolha == '1':
        domingo()

    if escolha == '2':
         segunda()

    if escolha == '3':
        terca()

    if escolha == '4':
        quarta()

    if escolha == '5':
        quinta()

    if escolha == '6':
        sexta()
    
    if escolha == '7':
        sabado()
    
    else:
        print("Valor invalido")
    


