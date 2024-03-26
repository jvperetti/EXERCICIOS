print("Olá, estou aqui para te ajudar a calcular sua nota no semestre\n")

ga = float(input("Digite sua nota no grau A:",))
gb = float(input("Digite sua nota no grau B:",))

if ga >= 0 and gb >= 0:
    notafinal = 0.3 * ga + 0.7 * gb
    if notafinal >= 6:
        print ("Sua nota é:", round(notafinal), "não precisa do grau C.")
    else:
        print ("Sua nota é:", round(notafinal), "você precisa do grau C.")
else:
    print("ERRO:\nValor negativo!")
