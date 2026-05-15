# Lê três números inteiros do usuário
num1 = int(input("Escreva o sue primeiro número: "))
num2 = int(input("Escreva o seu saegundo número: "))
num3 = int(input("Agora escreva o seu terceiro e ultimo número: "))

# Cria uma lista com os três números
listagem = [num1, num2, num3]
# Ordena a lista em ordem crescente
listagem.sort()
# Imprime a lista ordenada
print(listagem)
# Maior valor fica na última posição após ordenar
maior = listagem[2]
# Menor valor fica na primeira posição após ordenar
menor = listagem[0]
print(f"O seu maior número é: {maior}")
print(f"O seu menor número é: {menor}")

