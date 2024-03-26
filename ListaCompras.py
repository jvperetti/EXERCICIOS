print("Olá, estou aqui para ajudar na sua lista de compras!")

quant = int(input("Quantos produtos você deseja comprar?",))
listacompras = []

for produto in range (0, quant):
    listacompras.append (input("Qual produto você deseja comprar?"))
print ("Aqui está sua lista de compras:",)

for produto in listacompras:
    print (produto)

print("Obrigado por usar nossos serviços!")