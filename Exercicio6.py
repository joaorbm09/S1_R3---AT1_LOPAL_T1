# Lê um número inteiro do usuário
num = int(input("Digite seu número: "))
# Contador de divisores encontrados
div = 0

# Verifica todos os números de 1 até o próprio número
for i in range(1, num + 1):
    # Se o número for divisível por i, conta como divisor
    if num % i == 0:
        div += 1
# Um número primo tem exatamente dois divisores: 1 e ele mesmo
if div == 2:
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")
