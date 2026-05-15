# Lê o número para o qual a tabuada será gerada
num = int(input("Digite um número de 1 a 10: "))

# Imprime o cabeçalho da tabuada
print(f"Tabuada do {num}")
# Percorre os valores de 1 a 10 para a multiplicação
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
