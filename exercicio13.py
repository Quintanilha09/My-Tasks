import math
cOpost = float(input('Digite o cateto oposto: '))
cAdj = float(input('Digite o cateto adjacente: '))

hipot = math.hypot(cOpost,cAdj)

print('A hipotenusa de {} e {} é de: \033[36;40m{:.2f}\033[m'.format(cOpost,cAdj,hipot))