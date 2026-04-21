temp = float(input("Temperatura: "))
if temp < 10 or temp > 35:
    print(f"Atenção: {temp}°C é considerado clima extremo!")
else:
    print(f"A temperatura de {temp}°C está agradável.")