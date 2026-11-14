# Carregando os logs do sistema
log_sisema = "ERRO: Falha de comunicação no sensor 04"

# Verifica se a palavra "ERRO" está presente no código
tem_erro = "ERRO" in log_sisema
print(f"Falha detectada no log? {tem_erro}")

sem_critico = "CRÍTICO" not in log_sisema
print(f"Sem nível crítico? {sem_critico}")