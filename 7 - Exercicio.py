# Lê um número inteiro do usuário
numero = int(input("Digite um número: "))
# Inicializa o valor do fatorial
fatorial = 1
# Imprime o início da expressão de fatorial sem quebrar linha
print(f"{numero}! = ", end="")
# Percorre os valores de número até 1, em ordem decrescente
for i in range(numero, 0, -1):
    # Atualiza o valor do fatorial multiplicando pelo termo atual
    fatorial = fatorial * i
    # Imprime o termo atual da multiplicação
    print(i, end="")
    # Adiciona o símbolo de multiplicação se não for o último termo
    if i > 1:
        print(" x ", end="")
# Imprime o resultado final do fatorial
print(f" = {fatorial}")
