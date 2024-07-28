#aqui é para importar só os comandos expecificos
from math import radians, sin, cos, tan
angulo_normal = int(input("Digite o seu angulo: "))

#para transformar o angulo normar em radiano (sla oque significa)
angulo_radiano = radians(angulo_normal)
angulo_seno = sin(angulo_radiano)
angulo_cosseno = cos(angulo_radiano)
angulo_tangente = tan(angulo_radiano)
print(f"seno é {angulo_seno:.2f} cosseno é {angulo_cosseno:.2f} tangente é {angulo_tangente:.2f}")