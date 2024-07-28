#aqui eu to testando as bibliotecas
from math import ceil, floor
notafinal = 0
nota = float(input("Coloque a sua nota quebrada aqui: "))
if nota >= 4.5:
    notafinal = ceil(nota)
    print(f"sua nota ficara {notafinal}")
elif nota < 4.5:
    notafinal = floor(nota)
    print(f"sua nota ficaria {notafinal}")

#aqui é a biblioteca random
