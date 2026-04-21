usuario = input("Usuário: ")
senha = input("Senha: ")
if usuario == "admin" and senha == "1234":
    print(f"Bem-vindo, {usuario}! Acesso concedido.")
else:
    print(f"Erro: O usuário {usuario} ou a senha estão incorretos.")