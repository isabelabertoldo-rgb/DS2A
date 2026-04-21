senha_correta = "senai123"
tentativa = input("Digite a senha de acesso: ")

while tentativa != senha_correta:
    print("Senha incorreta! Tente novamente.")
    tentativa = input("Senha: ")

print("Acesso liberado!")