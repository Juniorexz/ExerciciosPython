lista = []
qtd = 6
for i in range(qtd):
    elemento = int(input('Digite um numero: '))
    lista.append(elemento)

lista.sort(reverse = True) #ordena os elementos
print(lista)