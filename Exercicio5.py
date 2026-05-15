# Solicita o nome do usuário
nome = input("Escreva seu nome: ")
# Requer que o nome tenha mais de 3 caracteres
while len(nome) <= 3:
    nome = input("Seu nome é curto, escreva denovo: ")

# Solicita a idade do usuário como inteiro
idade = int(input("Digite sua idade: "))
# Garante que a idade esteja entre 0 e 150
while idade < 0 or idade > 150:
    idade = int(input("Sua idade está acima ou abaixo do esperado, digite novamente a sua idade: "))

# Solicita o salário do usuário como número flutuante
salario = float(input("Escreva seu salário: "))
# Garante que o salário seja maior que zero
while salario <= 0:
    salario = float(input("Seu salário não será validado, tente novamente: "))

# Solicita o sexo e converte para minúsculas
sexo = input("Escreva seu sexo, (por ex: 'f' para feminino, 'm' para masculino): ").lower()
# Aceita apenas 'f' ou 'm'
while sexo != "f" and sexo != "m":
    sexo = input("Escreva seu sexo novamente, (por ex: 'f' para feminino, 'm' para masculino): ").lower()

# Solicita o estado civil e converte para minúsculas
estado_civil = input("Escreva seu estado civil(por ex: 's' de solteiro, 'c' de casado, 'v' de viuvo, 'd' de divorciado):").lower()
# Aceita apenas os valores s, c, v ou d
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = input("Escreva seu estado civil novamente(por ex: 's' de solteiro, 'c' de casado, 'v' de viuvo, 'd' de divorciado").lower()

# Imprime todos os dados após a validação
print("Seu cadastro ficou completo segue as informações abaixo para você verificalos (caso não esteja certo as suas informações, refaça o seu cadastro):")
print(f"Seu nome foi validado: {nome}")
print(f"Sua idade foi validada: {idade}")
print(f"Seu salário foi validado: {salario}")
print(f"Seu sexo foi validado: {sexo}")
print(f"Seu estado civil foi validado: {estado_civil}")


