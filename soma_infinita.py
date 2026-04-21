soma = 0
numero = int(input("Digite um número para somar (ou 0 para sair): "))

while numero != 0:
    soma = soma + numero
    numero = int(input(f"Soma atual: {soma}. Digite o próximo (ou 0): "))

print(f"Resultado final: {soma}")