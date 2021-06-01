n1=float(input('Valor 1 : '))
n2=float(input('Valor 2 : '))
n3=float(input('Valor 3 : '))
if (n1>=n2) and (n1>=n3):
    print(f'Maior número: {n1}')
elif (n2>=n1) and (n2>=n3):
    print(f'Maior número: {n2}')
else:
    print(f'Maior número: {n3}')