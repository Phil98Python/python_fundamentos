# Criando o status dos sensores
grade_fechada = False
emergencia_desativada = True

# Ambas precisam ser True para liberar o sistema
sistema_pronto = grade_fechada and emergencia_desativada
print(f"Sistema Liberado: {sistema_pronto}")