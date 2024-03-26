print("Olá, estou aqui para te ajudar\n")
cont = 0
colorado = 0

while cont < 10:
    time = input("Qual o seu time?")
    if time == "inter" or time == "internacional" or time == "Inter" or time == "Internacional":
        colorado += 1
    cont += 1
print(colorado ,"são colorados!")