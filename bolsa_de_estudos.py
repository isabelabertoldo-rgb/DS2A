nota = float(input("Digite a nota do aluno (0 a 10): "))
renda = float(input("Digite a renda familiar: R$ "))
e_atleta = input("O aluno é atleta federado? (s/n): ")

# A nota mínima é obrigatória (and), mas ele pode cumprir um dos outros dois requisitos (or)
if nota >= 9.0 and (renda <= 2000 or e_atleta == "s"):
    print(f"Resultado: Bolsa de estudos aprovada para nota {nota}!")
else:
    print(f"Resultado: Requisitos não atingidos para a bolsa.")