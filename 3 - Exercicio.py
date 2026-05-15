# Pede o nome do usuário
nome = input("Escreva seu nome: ")
# Inicializa a string usada para formar a 'escada'
escada = ""

# Percorre cada caractere do nome
for letra in nome:
    # Adiciona a letra atual à string acumulada
    escada = escada + letra
    # Imprime o estado atual da escada
    print(escada)

