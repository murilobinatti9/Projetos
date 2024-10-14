primeirosalario = int(input("Vamos aumetar o seu salario, qual seria ele atualmente? "))
if primeirosalario > 1250:
    primeirosalario = primeirosalario + primeirosalario * 0.10
    print(f"Ok, o seu salario com o aumento vai ficar {primeirosalario}")
else:
    primeirosalario = primeirosalario + (primeirosalario * 0.15)
    print(f"Seu salario é baixo, vou aumentar ele para {primeirosalario}")
