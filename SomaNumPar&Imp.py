print("Olá, vou te ajudar.\nVou somar os numeros pares e os numeros impares entre dois valores.")

val1 = int(input("Digite o valor 1, por favor:\n"))
val2 = int(input("Digite o valor 2, por favor:\n"))
pares = 0
impares = 0
if val1 >= 0 and val2 >= 0:
  menor = val1
  maior = val2
  if val1 > val2:
    maior = val1
    menor = val2
  cont = menor
  while cont <= maior:
      if cont % 2 == 0:
        pares += cont
      elif cont % 2 != 0:
        impares += cont
       
      cont += 1
  print ("Soma dos valor pares:", pares)
  print ("Soma dos valor impares:", impares)
else:
  print ("Valor invalido")