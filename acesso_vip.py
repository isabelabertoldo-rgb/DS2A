tem_convite_premium = input("Possui convite Premium? (s/n): ")
idade = int(input("Qual a sua idade? "))
na_lista = input("Seu nome está na lista? (s/n): ")

# O convite premium isolado já libera (or), ou precisa ser maior de idade e estar na lista (and)
if tem_convite_premium == "s" or (idade >= 18 and na_lista == "s"):
    print(f"Acesso liberado! Divirta-se na área VIP.")
else:
    print(f"Acesso negado. Verifique os critérios de entrada.")