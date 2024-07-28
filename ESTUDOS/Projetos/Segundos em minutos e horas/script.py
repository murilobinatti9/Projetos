segundos = int(input("Digite quantos segundos você quer transformar em minutos e horas: "))
minutos = segundos / 60 
horas = minutos // 60
print(f"{segundos} segundos em minutos, da {minutos:.0f}, em horas da {horas:.0f}")