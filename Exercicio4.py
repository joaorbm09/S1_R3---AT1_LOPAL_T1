# Lê quantos termos da sequência de Fibonacci exibir
n = int(input("Até qual termo você quer gerar a série de Fibonacci? "))
# Inicializa os dois primeiros termos da sequência
a, b = 1, 1
# Cria a lista que receberá os termos da sequência
sequencia = []
if n <= 0:
    print("0 não da...")
elif n == 1:
    print("Série de Fibonacci até o 1º termo: [1]")
else:
    # Inicia a contagem para gerar os termos da sequência
    count = 0
    while count < n:
        # Adiciona o termo atual (a) à lista
        sequencia.append(a)
        # Atualiza os valores de a e b para o próximo termo de Fibonacci
        a, b = b, a + b
        # Incrementa o contador de termos gerados
        count += 1
    # Imprime a descrição e a sequência gerada
    print(f"Série de Fibonacci até o {n}º termo:")
    print(sequencia)