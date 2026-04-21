def converter_para_libra(reais, cotacao):
    return reais / cotacao

valor_r = float(input("Quantos reais você tem? R$ "))
valor_l = converter_para_libra(valor_r, 6.20)

print(f"Isso equivale a £ {valor_l:.2f}")