# Define a lista de números
L = [5, 7, 2, 9, 4, 1, 3]
# Mostra a lista original
print(L)

# Calcula o tamanho da lista
tamanho = len(L)
print(f"O tamanho da sua lista é: {tamanho}")

# Encontra o maior e o menor valor da lista
maior = max(L)
menor = min(L)
print(f"O seu maior número é: {maior}")
print(f"O seu menor número é: {menor}")

# Calcula a soma de todos os valores
soma = sum(L)
print(f"A soma da sua lista é: {soma}")

# Ordena a lista em ordem crescente
L.sort()
print(f"Sua lista fica de forma crescente: {L}")

# Inverte a ordem da lista para decrescente
L.reverse()
print(f"Sua lista fica de forma decrescente: {L}")


