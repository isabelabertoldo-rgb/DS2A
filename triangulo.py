a, b, c = int(input("Lado A: ")), int(input("Lado B: ")), int(input("Lado C: "))
if a < b + c and b < a + c and c < a + b:
    print(f"As medidas {a}, {b} e {c} formam um triângulo válido.")
else:
    print(f"As medidas {a}, {b} e {c} não podem formar um triângulo.")