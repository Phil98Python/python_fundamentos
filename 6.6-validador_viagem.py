# Solicitando dados do veículo
combustivel = float(input("Quantidade de combustível: "))
pneus = input("Os pneus estão calibrados? (sim/nao) ").lower().strip() #strip remove espaços vazios (antes e depois da expressão) e lower configura todas as letras em minusculo
documento_ok = input("A documentação está em dia? (sim/nao) ").lower().strip()

# Checagem individual (retorna True ou False)
combustivel_suficiente = combustivel >= 10.0
pneus_calibrados = pneus == "sim" 
documento_regularizado = documento_ok == "sim"

# Combinação lógica para liberação da viagem
viagem_liberada = combustivel_suficiente and pneus_calibrados and documento_regularizado

# Apresentando o status e liberação da viagem
print("\n ----- STATUS DE SEGURANÇA DA VIAGEM -----\n")
print(f"1. Combustível Suficiente (>=10L): {combustivel_suficiente}")
print(f"2. Pneus Calibrados: {pneus_calibrados}")
print(f"3. Documentação em dia: {documento_regularizado}\n")
print(f"\U0001f697 A viagem está liberada: {viagem_liberada}")