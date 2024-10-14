velocidadedocarro = float(input("Digite a velocidade do carro: "))
valormultado = velocidadedocarro * 7
if velocidadedocarro <= 80:
    print(f"o carro esta totalmente na lei, pois estava a {velocidadedocarro} KM/H")
else:
    print(f"o carro vai ser multado em R${valormultado:.2f}")