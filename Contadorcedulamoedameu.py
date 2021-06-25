def menu_inicial(num):
    print('Programa Contador cedulas e moedas')
    
    valor= float(input("Digite o valor que possui de saldo na conta :"))

    print("A quantidade em notas de R$ 200 seria : ", valor/200)
    print("A quantidade em notas de R$ 100 seria : ", valor/100)
    print("A quantidade em notas de R$ 50 seria : ", valor/50)
    print("A quantidade em notas de R$ 20 seria : ", valor/20)
    print("A quantidade em notas de R$ 10 seria : ", valor/10)
    print("A quantidade em notas de R$ 5 seria : ", valor/5)
    print("A quantidade em notas de R$ 2 seria : ", valor/2)
    print("A quantidade em notas de R$ 1 seria : ", valor/1)
    print("A quantidade em moedas de R$ 0,50 seria : ", valor/0.50)
    print("A quantidade em notas de R$ 0,25 seria : ", valor/0.25)
    print("A quantidade em notas de R$ 0,10 seria : ", valor/0.10)
    print("A quantidade em notas de R$ 0,05 seria : ", valor/0.10)
    print("A quantidade em notas de R$ 0,01 seria : ", valor/0.5)
    print("A quantidade em notas de R$ 0,1 seria : ", valor/0.1)

menu_inicial(14)