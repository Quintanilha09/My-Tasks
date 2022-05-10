frase = str(input('\033[35mEscreva uma frase:\033[m ')).lower().strip()

print('A letra \033[33m"A"\033[m aparece \033[1;34m{}\033[m vezes'.format(frase.count('a')))
print('Sua primeira aparição é na posição \033[1;31m{}\033[m'.format(frase.find('a')+1))
print('A sua ultima aparição é na posição \033[1;35m{}\033[m'.format(frase.rfind('a')+1))

