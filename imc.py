peso = float(input("Digite seu peso"))
nome = input ("Digite seu nome")
altura = float(input("Digite sua altura"))
imc = peso / (altura **2)
print(f"seu IMC é {imc:.1f}")
if imc < 18.5:
    print("Classificação: abaixo do peso")
elif imc < 25:
    print("Classificção: peso ideal")
else:
    print("Classificção: Acima do peso")