def e_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

valor = int(input("Digite um número: "))
if e_par(valor):
    print(f"O número {valor} passou no teste de paridade!")
else:
    print(f"O número {valor} é ímpar.")