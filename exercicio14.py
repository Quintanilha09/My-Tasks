import math

angulo = float(input('\033[32mDigite o ângulo: \033[m'))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno de {} é \033[35m{:.2f}\033[m, o cosseno é \033[32m{:.2f}\033[m, a tangente é \033[34m{:.2f}\033[m'.format(angulo,seno,cosseno,tangente))
