print("Olá, vou te ajudar.\nIrei imprimir os números primos até 200 e depois a soma deles.")

count = 0
soma = 0

while count <= 200:
  div = []                   #linha 7 a 10, estabelecemos os divisores inteiros dos números que queremos (primos)
  for i in range (1, count + 1):
    if count % i == 0:
      div.append(i)
  if len(div) == 2:         #Estabelecemos que nesta lista div, os numeros serão dividos por dois valores. 1 = ele & 2 = ele mesmo
    soma += count
  count += 1

print("A soma dos números primos é", soma)