#   Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

metros = float(input("Valor em metros: "))
cm = metros * 100
mm = metros * 1000
print("{} metros corresponde a {} cm e {} mm".format(metros, cm, mm))
