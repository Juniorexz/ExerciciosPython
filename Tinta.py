def calcular_latas(m):
  litros = round(m / 3)
  latas = round(litros / 18)
  valor_latas = latas * 80
  print(f"Devera utilizar {latas} latas")
  print(f"O valor total equivale a R${valor_latas:.2f}")
area = float(input("Insira a metragem quadrada da area a ser pintada: "))
calcular_latas(area)