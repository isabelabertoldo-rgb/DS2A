def exibir_cabecalho():
    print("\n" + "="*30)
    print("   GERENCIADOR DE NOTAS")
    print("="*30)

def calcular_media(n1, n2):
    return (n1 + n2) / 2

# Programa Principal
exibir_cabecalho()
nota_a = float(input("Nota 1: "))
nota_b = float(input("Nota 2: "))

media_final = calcular_media(nota_a, nota_b)

if media_final >= 6:
    status = "APROVADO"
else:
    status = "REPROVADO"

print(f"Resultado final: {media_final} - Status: {status}")