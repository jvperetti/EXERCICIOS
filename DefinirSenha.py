print("Olá, vou te ajudar.\nEu ajudarei a definir uma senha para você.\nMas lembre-se, você devera escolher entre 5 a 10 números, e tera 6 tentativas!")

tentativa = 5


for i in range(0,6):
  senha = input("Defina sua senha:")
  if(senha.isdigit() and len(senha) >= 5 and len(senha) <=10):
    print("Senha cadastrada com sucesso!")
    break
  else:
    print("Senha inválida. Número de tentativas restantes:", tentativa)
    tentativa -= 1
if tentativa <= 0:
  print("Quantidade de tentativas excedida!")