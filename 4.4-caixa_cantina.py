# --- Resolução do exercicio 1 ---
# ------ Caixa Cantina ------

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço unitário: "))
quantidade = int(input("Digite a quantidade: "))

total = preco * quantidade
total_br = f"{total: .2f}".replace(".",",")

print("\n---- MERCADO PAI E FILHO ----\n")
print("---- RESUMO DA COMPRA ----\n")
print(f"Produto: {produto.title()}")
print(f"Valor unitário: R$ {preco}")
print(f"Quantidade: {quantidade}")
print(f"Total a pagar: R$ {total_br}\n")
print("------- VOLTE SEMPRE! --------")