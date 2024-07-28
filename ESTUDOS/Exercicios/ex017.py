import math
cateto_oposto = float(input("Digite o cateto oposto: "))
cateto_adjacente = float(input("Digite o cateto adjacente: "))
hipotenusa = cateto_oposto ** 2 + cateto_adjacente ** 2 
print(f"A hipotenusa dessa porra inteira da: {math.sqrt(hipotenusa):.2f}")