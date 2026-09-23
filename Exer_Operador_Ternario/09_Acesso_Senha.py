senha_correta = "senha123"
senha_digitada = "abc123"

acesso = "Acesso permitido" if senha_digitada == senha_correta else "Acesso negado"

print(f"Tentativa de login: {acesso}")