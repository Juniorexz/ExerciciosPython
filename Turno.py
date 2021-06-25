#Faça um Programa que pergunte em que turno você estuda. 
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!",conforme o caso. 
#
def menun_inicial():
    print("Turma Inicial")

def matutino():
    print("Bom dia - Matutino")

def vespertino():
    print("Boa tarde - Vespertino")

def noturno():
    print("Boa noite - Noturno")
    
if __name__ == "__main__":
    menun_inicial()
    escolha = input("Escolha o melhor horario : ")
    if escolha in "Mmatutino":
        matutino()
    elif escolha in "Vvespertino":
        vespertino()
    elif escolha in "Nnoturno":
        noturno()
    else:
        print("Escolha invalida")

#M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
