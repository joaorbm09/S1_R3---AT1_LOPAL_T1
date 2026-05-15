# print("Sua tabela")
# tabela = {"produtos":["Salgado", "Lanche", "Suco", "Refrigereante", "Doce" ] , "precos":["R$ 4,50","R$6,50","R$ 3,00","R$ 3,50","R$ 1,00"]}
# produtos = tabela["produtos"]
# precos = tabela["precos"]
# tabela_final = [produtos, precos]
# print(tabela_final)

# acima esta o que eu tinha feito, abaixo esta uma versão com ia para deixar a listagem organizada

print("--- Sua Tabela de Preços ---")
tabela = {
    "produtos": ["Salgado", "Lanche", "Suco", "Refrigerante", "Doce"], 
    "precos": ["R$ 4,50", "R$ 6,50", "R$ 3,00", "R$ 3,50", "R$ 1,00"]
}
produtos = tabela["produtos"]
precos = tabela["precos"]

tabela_final = list(zip(produtos, precos))

for produto, preco in tabela_final:
    print(f"{produto:<15} -> {preco}")


