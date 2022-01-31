# Tuplas sao coleções ordenadas e imutaveis. Existem dois métodos para tuplas: count e index.
# Podemos criar tuplas com ()

tupla = (1, 2, 3, 4, 5)
print(type(tupla))           #checa o tipo de objeto criado

tupla1 = 1, 2, 3, 4, 5
print(type(tupla1))

#############
#     index()                   Retorna o índice do elemento especificado.
#     count()                   Conta o número de vezes que o elemento aparece na tupla.
################################

tupla2 = ('a', 'b', 'c', 'd')
print(f"Índice de 'a': {tupla2.index('a')}")
print(f"Índice de 'd': {tupla2.index('d')}")

tupla3 = ('a', 'z', 'z', 'z', 'w')
print(tupla3.count('z'))

##############  DICIONÁRIOS  ################
#  Tipo de dado chave-valor, ou seja, para cada chave se associa um valor correspondente.
#  Usamos dicionários para criar DataFrames na biblioteca Pandas (DataScience).

dict = {
    'chave1':'valor1',
    'chave2':'valor2'
}
print(dict)
print(type(dict))

dados = {'nome' : 'PS4', 'valor' : 2500, 'estoque' : 50, 'categoria' : 'video game',}
print(dados)
print(dados['nome'])
print(dados['valor'])

dict2 = {
    'chave1': [1, 3, 5],
    'chave2': [2, 4, 6],
    'chave3': (7, 9, 11),
    'chave4': (13, 15, 17),
}
print(dict2)
print(dict2['chave1'])

dict2['chave4'] = 14, 16, 18
print(dict2)
