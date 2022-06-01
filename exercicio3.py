nota1 = int(input('\033[4;34mDigite sua primeira nota:\033[m'))
nota2 = int(input('\033[4;36mDigite sua segunda nota:\033[m'))

media = (nota1 + nota2) /2

print('\033[1;30;41mA media do aluno é\033[m \033[1;33m{}'.format(media))