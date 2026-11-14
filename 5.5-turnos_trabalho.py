# Quantidade de componentes e operadores
total_componentes = int(input("Quantidade de componentes: "))
OPERADORES = 4

# Divisão de trabalho
divisao_trabalho = total_componentes // OPERADORES   

# Sobra de componentes
sobra_componentes = total_componentes % OPERADORES

# Resultado:
print(f"Cada operador deve processar {divisao_trabalho} componentes restando apenas {sobra_componentes} sem processamento")