# Criação das variáveis válidas
temperatura_atual = int(input("Temperatura atual: "))
LIMITE_SEGURANCA = 80
pressao_atual = 100
PRESSAO_NOMINAL = 100

# Teste relacional no terminal
print(f"Superaqueceu? {temperatura_atual > LIMITE_SEGURANCA}")
print(f"Pressão Normal? {pressao_atual == PRESSAO_NOMINAL}")
print(f"Temperaatura OK? {temperatura_atual <= LIMITE_SEGURANCA}")
