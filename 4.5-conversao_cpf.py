# Solicitando o CPF ao usuário

cpf = input("Digite o seu CPF: ")

# Realizando a remoção do ponto e traço e armazenando o CPF limpo
cpf_limpo = cpf.replace(".","").replace("-","")

# Apresentando resultado do CPF limpo
print(f"CPF limpo: {cpf_limpo}")