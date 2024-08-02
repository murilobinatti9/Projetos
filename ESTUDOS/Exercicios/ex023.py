# Solicita ao usuário um número entre 0 e 9999
numero = input("Escolha um número de 0 a 9999: ")

# Garante que o número seja formatado com 4 dígitos, preenchendo com zeros à esquerda se necessário
numero_formatado = f"{int(numero):04d}"

# Exibe cada dígito individualmente
print(f"Milhar: {numero_formatado[0]}")
print(f"Centena: {numero_formatado[1]}")
print(f"Dezena: {numero_formatado[2]}")
print(f"Unidade: {numero_formatado[3]}")
