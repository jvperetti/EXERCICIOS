print("Olá, vou te ajudar.\nDigite um numero positivo, e eu lhe darei seu fatorial.")

num = int(input("Digite o numero: "))
if num >= 0:           
  if num == 0 or num == 1:
    print ("O fatorial de" ,num, "é 1.")
  else:
    cont = num 
  vezes = 1
  while cont > 1:
    vezes *= cont
    cont -= 1
  print ("O fatorial de" ,num, "é" ,vezes, ".")
else:
  print ("O numero deve ser positivo.")