# Definindo os valores das variáveis
temperatura_critica = False
pressao_critia = False

# Realizando a checagem dos sensores
alarme_disparado = temperatura_critica  or  pressao_critia

# Apresentando disparo do alarme
print(f"Alarme Ativado: {alarme_disparado}")