frase = 'meu ovo torto'

print(len(frase))  # informa quantas letras há na frase, contando com os espaços
print(frase.strip())  # remove os espaços indesejados dos lados
print(frase.rstrip())  # vai remover os espaços do lado direito
frase = (frase.replace('ovo', 'pé'))  # troca as palavras
print(frase.lower().find('pé'))  # coloquei a frase em minusculo e mandei achar 'pé'
print(frase)
print(len(frase))
print('letras')
torto = 'torto' in frase #vai analisar se tem 'torto' na variavel frase, a resposta vai para a variavel torto
print(torto)
print(frase.capitalize()) #transorma só a primeira letra da frase em maiuscula
print(frase.title(), '\n') #transormas todas as primeiras letras de palavras em maiuscula, realmente igual titulo

print("""Poema é um gênero textual dividido em estrofes e versos. 
Cada estrofe é constituída por versos. 
Introduzidos pelo sentido das frases -
e mais raramente em conversa - em que a poesia, 
forma de expressão estética através da língua, geralmente se manifesta.""")

n1 = input('digite um nome: ')
n2 = input('digite um nome: ')
n3 = input('digite um nome: ')

lista = n1,n2,n3.split() #O split transorma em uma lista
print(lista)

print(lista[0:3])
print(len(lista))

print(lista[2][2]) #estou pedindo mandando pegar a letra 2 da segunda palavra da lista

lst = [13, 4, 20, 15, 6, 20, 20]

print(lst.index(20)) #aqui eu estou pedindo para me mostrar o item 20 da lst, através do .index

'-'.join(lista) # aqui eu posso juntar todos os itens de uma lista em uma string, o - significa que elas serão separadas por ele.
#Mas pode ser qualquer coisa, como um espaço ou #.


