peso = float(input("Digite seu peso em KG"))
altura = float(input("Digite sua altura em metros"))
imc = peso / (altura **2)
print(f"Seu IMC é {imc:.1f}")
if imc < 18.5:
    print("Classificação: Abaixo do peso.")
elif imc <25:
    print ("Classificação: Peso Ideal")
else: 
    print("Classificação: Acima do peso")