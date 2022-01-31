# As listas podem ser utilizadas para armazenar valores. Esses valores podem ser strings, tuplas,
# outras listas, dicionários, dentre outros.

lista1 = [10, 20, 30, 40]
lista2 = ['Hello World!', 10, 20, 30, [1, 2, 3], (45, 50)]
print(type(lista2))

# acessar elementos da lista
lista = ['A', 'B', 'C']
print(lista[0])

# mudar um valor dentro da lista
lista[0] = 'Z'
print(lista)

# mudar lista usando indexação negativa
b = ['a', 'b', 'c', 'd', 'h']
print(b[-1])
b[-1] = 'e'
print(b[-1])

# Máximo, mínimo, soma e tamanho de uma lista
num = [31, 914, 236, 376, 140, 705]
print(f'Valor máximo: {max(num)}')
print(f'Valor mínimo: {min(num)}')
print(f'Número de elementos: {len(num)}')
print(f'Soma dos elementos: {sum(num)}')

media = sum(num) / len(num)
print(media)

# como unir listas
uniao = lista1 + lista2 + lista
print(uniao)

# repetindo elementos

print(lista * 2)
print(lista2 * 2)
print(lista1 * 2)

# sequencia de numeros por meio da função range()
# sintaxe: range(início,fim, passo)
serie = list(range(2010, 2021, 2))
print(serie)

# convertendo uma string em uma lista
frase = 'Eu amo aprender python!'
print(frase.split(sep=' '))
print(frase)
frase2 = 'Eu%amo%aprender%python!'
print(frase2.split(sep='%'))

#########################################################################

# Métodos em listas:

# append()     Adiciona um elemento ao final da lista
# insert()     Adiciona um elemento em um índice especificado
# extend()     Adiciona os elementos de um iterável no final da lista
# pop()        Remove e retorna um elemento de um índice especificado
# remove()     Remove o primeiro elemento com o valor especificado
# clear()      Remove todos os elementos de uma lista
# copy()       Retorna uma cópia da lista selecionada
# sort()       Ordena a lista
# reverse()    Reverte a ordem dos elementos de uma lista
# index()      Reftorna o primeiro indice do elemento especificado
# count()      Conta o número de vezes que o elemento aparece na lista

############################################################################

numeros = [45, 50, 55]
numeros.append(60)
print(numeros)
numeros.append(77)
print(numeros)

numeros.extend([60, 61])
numeros.extend('abcdef')
print(numeros)

numeros.insert(1, 0)  # inceriu o número 0 no índice 1, que antes era o 50
print(numeros)

numeros.remove(50)
print(numeros)

numeros.pop()  # se não inserir índice, o útimo elemento será removido
numeros.pop(1)  # remove e retorna o elemento com índice 1
print(numeros)

letras = ['k', 'i', 'j', 'm']
print(letras)
del letras[0]  # deletamos o item de índice 0
print(letras)
del letras


letras1 = ['abc', 'ab', 'a']
print(letras1)
letras1.clear()
print(letras1)

numeros1 = [1, 1, 1, 0, 0, 0, 5, 3, 1, 2]
numeros1.count(1)     #conta o número de ocorrências do número 1
print(numeros1)
print(numeros1.count(1))

numeros2 = [10, 11, 12, 13, 14, 15]
print(numeros2)
numeros2.reverse()    #inverte a ordem da lista
print(numeros2)

numeros3 = [-10, 100, -1, 60, 76, 33, -30, 150]
print(numeros3)
numeros3.sort()       #ordena a lista
print(numeros3)

lista3 = [5, 6, 7, 8]
print(lista3)
print(lista3.index(5))

numeros4 = [1, 2, 3, 3, 3, 3, 3, 7, 7, 8, 9, 10, 10, 11, 12, 11]
print(numeros4.index(3))  #retorna o índice da primeira ocorrência do número 3
print(numeros4.index(3, 5))