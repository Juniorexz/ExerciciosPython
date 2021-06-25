'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 


# Essa solução não utiliza listas
# res1 = int(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
# res2 = int(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
# res3 = int(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
# res4 = int(input("Devia para a vítima? 1/Sim ou 0/Não: "))
# res5 = int(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
# # soma o número de respostas
# soma_respostas = res1 + res2 + res3 + res4 + res5
# if (soma_respostas < 2):
# print("\nInocente")
# elif (soma_respostas == 2):
# print("\nSuspeita")
# elif (3 <= soma_respostas <= 4):
# print("\nCúmplice")
# elif (soma_respostas == 5):
# print("\nAssassino")





'''


def menu_inicial():
    print('Programa de vitimas')

res = []
res.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))

soma_respostas = 0
for i in res:
# soma o número de respostas
    soma_respostas += int(i)
if (soma_respostas < 2):
    print("\nInocente")
elif (soma_respostas == 2):
    print("\nSuspeita")
elif (3 <= soma_respostas <= 4):
    print("\nCúmplice")
elif (soma_respostas == 5):
    print("\nAssassino")