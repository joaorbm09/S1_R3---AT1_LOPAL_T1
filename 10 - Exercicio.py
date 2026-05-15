
# Solicita a senha ao usuário
senha = int(input("Digite a senha: "))

# Repete enquanto a senha estiver incorreta
while senha != 676767:
    print("Senha incorreta, tente novamente.")
    senha = int(input("Digite a senha: "))
if senha == 676767:
    # Mostra mensagem de sucesso quando a senha estiver correta
    print("Acesso liberado")
else:
    # Este caso não será alcançado com a lógica atual,
    # porque o loop só sai quando a senha for correta
    print("Limite de tentativas atingido. Tente novamente mais tarde")